# Contributing

Contributions should improve detection value without overstating production readiness. Never include credentials, tenant identifiers, real incident data, personal data, or unredacted prompts and responses.

## Query Contribution Requirements

Each KQL contribution should include:

- Clear name
- Description
- Data source
- Use case
- False positive notes
- Tuning guidance
- Response guidance if detection-oriented
- Validation status and evidence
- Related analytics rule when one exists

Use `templates/query-template.kql` as the standard format.

## Workflow

1. Create a focused branch.
2. Add or update the query, documentation, and associated analytics rule together.
3. Add positive, negative, and boundary test cases when practical.
4. Run `python3 scripts/validate_content.py`.
5. Explain schema assumptions and validation evidence in the pull request.

## Validation status

- **Example** — structurally reviewed but not run against representative telemetry.
- **Lab Tested** — executed with controlled positive and negative cases.
- **Production Validated** — operated against representative production telemetry with documented results.

Do not label content `Lab Tested` or `Production Validated` without preserving the test method, date, and expected results.

## Analytics rules

Rules must include a stable GUID, semantic version, connector requirements, MITRE mappings where applicable, `TimeGenerated` in the final output, entity mappings, custom details, grouping, false-positive context, and response guidance. Every mapped field, custom detail, and dynamic alert placeholder must remain in the final query output.

Increment the rule version when detection logic, thresholds, mapped entities, required tables, or operational behavior changes. Documentation-only changes do not require a rule version increase.

## Custom schemas

Custom tables require a schema contract under `docs/schemas/`. Document required columns, types, collection method, privacy constraints, and schema evolution. Prefer normalization with DCR transformations or parsers over repeating field compatibility logic in every query.

## Pull-request checklist

- [ ] Query header is complete.
- [ ] Lookback and thresholds are documented.
- [ ] False positives and tuning guidance are specific.
- [ ] Query returns the expected entity fields.
- [ ] Scheduled rules return `TimeGenerated`.
- [ ] Positive, negative, and boundary behavior was reviewed.
- [ ] No sensitive information is included.
- [ ] Repository validation passes.
