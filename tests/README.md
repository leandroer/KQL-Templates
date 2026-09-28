# KQL Test Fixtures

The files in `tests/fixtures/` are self-contained KQL checks built with `datatable()`. Paste a fixture into a KQL-capable test workspace and confirm that it returns `TestPassed=true`.

Fixtures provide fast logic checks but do not replace integration testing against real connector schemas. Production promotion should also verify table availability, field types, ingestion delay, representative benign activity, entity mappings, alert details, and incident grouping in a Microsoft Sentinel workspace.

| Fixture | Coverage |
|---|---|
| `password-spray.test.kql` | Threshold boundary and multi-user aggregation |
| `success-after-failures.test.kql` | Temporal correlation selects the first qualifying success |
| `prompt-injection.test.kql` | Repeated suspicious prompts cross the alert threshold |

Add at least one positive, negative, and boundary condition when extending a fixture.
