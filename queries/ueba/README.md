# UEBA Queries

These queries use Microsoft Sentinel User and Entity Behavior Analytics to combine behavioral anomalies with identity context. They are starting points, not universal production detections.

## Prerequisites

- Enable UEBA in Microsoft Sentinel.
- Connect supported identity providers and relevant activity sources.
- Confirm that `BehaviorAnalytics` and `IdentityInfo` contain recent records.
- Inspect available columns and dynamic insight fields in the target workspace.

## Query Catalog

| Query | Purpose |
|---|---|
| `high-investigation-priority-activity.kql` | Review the most anomalous recent behavior |
| `anomalous-privileged-user-activity.kql` | Prioritize anomalies involving privileged identities |
| `dormant-account-anomalous-activity.kql` | Find anomalous use of identities absent from the recent baseline |
| `service-account-behavior-anomaly.kql` | Review high-priority service-account anomalies |
| `unusual-user-location-or-device.kql` | Surface location or device deviations |
| `anomaly-before-role-assignment.kql` | Correlate anomalous behavior with role-management activity |
| `mass-download-with-ueba-context.kql` | Enrich mass downloads with behavioral risk |
| `user-risk-investigation-timeline.kql` | Produce a compact anomaly timeline for one user |

See [`docs/architecture/ueba-enrichment-flow.md`](../../docs/architecture/ueba-enrichment-flow.md) for the operating model.

## Tuning guidance

Start with hunting queries at an `InvestigationPriority` threshold of 5. Production rules should normally require a stronger condition such as a score of 7 or more, privileged identity context, a sensitive action, or correlation with the original event source. Validate field names because identity and activity enrichments vary by connected source.
