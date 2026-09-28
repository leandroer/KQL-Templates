#!/usr/bin/env python3
"""Validate KQL metadata, Sentinel rule structure, and local Markdown links."""

from __future__ import annotations

import re
import sys
import uuid
from pathlib import Path

try:
    import yaml
except ImportError:  # YAML parsing is optional locally and installed in CI.
    yaml = None


ROOT = Path(__file__).resolve().parents[1]
STRICT_QUERY_ROOTS = (ROOT / "queries",)
REQUIRED_QUERY_HEADERS = (
    "Name",
    "Description",
    "Query Type",
    "Platforms",
    "Tables",
    "Required Connectors",
    "MITRE ATT&CK",
    "Severity",
    "Lookback",
    "Entity Fields",
    "False Positives",
    "Tuning Guidance",
    "Response Guidance",
    "Validation Status",
    "Related Analytics Rule",
)
REQUIRED_RULE_FIELDS = (
    "id",
    "name",
    "description",
    "severity",
    "status",
    "requiredDataConnectors",
    "queryFrequency",
    "queryPeriod",
    "triggerOperator",
    "triggerThreshold",
    "tactics",
    "relevantTechniques",
    "query",
    "entityMappings",
    "customDetails",
    "eventGroupingSettings",
    "incidentConfiguration",
    "version",
    "kind",
)


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def validate_queries(errors: list[str]) -> None:
    for root in STRICT_QUERY_ROOTS:
        for path in sorted(root.glob("*.kql")):
            text = path.read_text(encoding="utf-8")
            for header in REQUIRED_QUERY_HEADERS:
                if not re.search(rf"^// {re.escape(header)}:\s*\S", text, re.MULTILINE):
                    errors.append(f"{relative(path)}: missing or empty header '{header}'")
            if "make_set(" in text and re.search(r"make_set\(\s*[^(),\n]+\s*\)", text):
                errors.append(f"{relative(path)}: make_set() must specify a maximum size")
            if "TimeGenerated" in text and "ago(" not in text:
                errors.append(f"{relative(path)}: expected an explicit lookback using ago()")


def validate_rules(errors: list[str], warnings: list[str]) -> None:
    ids: dict[str, Path] = {}
    for path in sorted((ROOT / "analytics-rules").rglob("*.yaml")):
        text = path.read_text(encoding="utf-8")
        if "REPLACE-WITH" in text or "T0000" in text:
            errors.append(f"{relative(path)}: unresolved template placeholder")
        if yaml is None:
            warnings.append("PyYAML is not installed; YAML structure checks were skipped")
            continue
        try:
            rule = yaml.safe_load(text)
        except yaml.YAMLError as exc:
            errors.append(f"{relative(path)}: invalid YAML: {exc}")
            continue
        for field in REQUIRED_RULE_FIELDS:
            if field not in rule:
                errors.append(f"{relative(path)}: missing required field '{field}'")
        rule_id = str(rule.get("id", ""))
        try:
            uuid.UUID(rule_id)
        except ValueError:
            errors.append(f"{relative(path)}: id is not a valid GUID")
        if rule_id in ids:
            errors.append(f"{relative(path)}: duplicate id also used by {relative(ids[rule_id])}")
        ids[rule_id] = path
        query = str(rule.get("query", ""))
        projects = list(re.finditer(r"(?ms)^\s*\|\s*project\s+(.+?)(?=^\s*\||\Z)", query))
        final_output = projects[-1].group(1) if projects else query
        if not re.search(r"\bTimeGenerated\b", final_output):
            errors.append(f"{relative(path)}: final query output must include TimeGenerated")
        for mapping in rule.get("entityMappings", []):
            for field_mapping in mapping.get("fieldMappings", []):
                column = field_mapping.get("columnName")
                if column and not re.search(rf"\b{re.escape(str(column))}\b", final_output):
                    errors.append(
                        f"{relative(path)}: mapped column '{column}' is not present in the final output"
                    )
        for detail, column in rule.get("customDetails", {}).items():
            if column and not re.search(rf"\b{re.escape(str(column))}\b", final_output):
                errors.append(
                    f"{relative(path)}: custom detail '{detail}' column '{column}' is not in the final output"
                )
        override = rule.get("alertDetailsOverride", {})
        override_text = " ".join(str(value) for value in override.values())
        for column in re.findall(r"\{\{\s*([A-Za-z_][A-Za-z0-9_]*)\s*\}\}", override_text):
            if not re.search(rf"\b{re.escape(column)}\b", final_output):
                errors.append(
                    f"{relative(path)}: alert placeholder '{column}' is not in the final output"
                )
        frequency = parse_duration(rule.get("queryFrequency"))
        period = parse_duration(rule.get("queryPeriod"))
        if frequency is not None and period is not None and frequency > period:
            errors.append(f"{relative(path)}: queryFrequency must not exceed queryPeriod")


def parse_duration(value: object) -> int | None:
    match = re.fullmatch(r"(\d+)([mhd])", str(value))
    if not match:
        return None
    amount = int(match.group(1))
    return amount * {"m": 1, "h": 60, "d": 1440}[match.group(2)]


def validate_markdown_links(errors: list[str]) -> None:
    link_pattern = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:|#)([^)]+)\)")
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for target in link_pattern.findall(text):
            clean_target = target.split("#", 1)[0]
            if not clean_target:
                continue
            resolved = (path.parent / clean_target).resolve()
            if not resolved.exists():
                errors.append(f"{relative(path)}: broken relative link '{target}'")


def validate_fixtures(errors: list[str]) -> None:
    fixtures = sorted((ROOT / "tests" / "fixtures").glob("*.test.kql"))
    if not fixtures:
        errors.append("tests/fixtures: expected at least one KQL fixture")
    for path in fixtures:
        text = path.read_text(encoding="utf-8")
        if "datatable(" not in text:
            errors.append(f"{relative(path)}: fixture must be self-contained with datatable()")
        if "TestPassed" not in text:
            errors.append(f"{relative(path)}: fixture must return a TestPassed result")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    validate_queries(errors)
    validate_rules(errors, warnings)
    validate_markdown_links(errors)
    validate_fixtures(errors)
    for warning in sorted(set(warnings)):
        print(f"WARNING: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"Validation failed with {len(errors)} error(s).")
        return 1
    print("Content validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
