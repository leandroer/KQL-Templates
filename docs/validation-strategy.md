# Validation Strategy

Repository validation is layered because static checks cannot prove that a KQL detection works against a tenant's live schemas.

## Layer 1 — static repository validation

`scripts/validate_content.py` checks metadata, YAML structure, GUID uniqueness, scheduling, required `TimeGenerated`, final output columns, alert placeholders, fixtures, and links.

## Layer 2 — self-contained logic fixtures

Queries under `tests/fixtures/` use `datatable()` to exercise positive, negative, and boundary behavior. A passing fixture must return `TestPassed=true` in a KQL-capable workspace.

## Layer 3 — schema compilation

Compile every query in a test workspace containing the declared tables and parsers. Confirm field types, function parameters, connector availability, and custom schema versions.

## Layer 4 — Sentinel rule smoke test

Deploy rules disabled or in a controlled lab. Verify entity mappings, custom details, dynamic alert text, event grouping, incident grouping, lookback overlap, and ingestion latency.

## Layer 5 — operational validation

Measure alert volume, precision, investigation value, false-negative hypotheses, ownership, and review dates. Promote content to `Production Validated` only after documenting representative results.

Workspace-backed testing is intentionally not enabled in the public GitHub workflow because it requires a tenant, workspace, credentials, populated connectors, and controlled test data. Add a protected manual workflow only after those resources and secret-management controls exist.
