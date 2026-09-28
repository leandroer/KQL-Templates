# UEBA Enrichment Flow

Microsoft Sentinel UEBA adds behavioral context to raw activity. The most useful detections combine an anomalous activity record with current identity context and the original source event.

```mermaid
flowchart LR
    S["Security telemetry"] --> U["Sentinel UEBA analytics"]
    U --> B["BehaviorAnalytics"]
    I["Identity providers"] --> ID["IdentityInfo"]
    B --> C["KQL correlation and enrichment"]
    ID --> C
    O["Original source event"] --> C
    C --> A["Analytics rule"]
    A --> N["Entity-rich incident"]
    N --> R["Analyst investigation and response"]
```

## Design principles

- Treat `InvestigationPriority` as context, not a verdict.
- Use the latest relevant `IdentityInfo` record per identity.
- Raise confidence by correlating anomalies with sensitive roles, risky actions, or another telemetry plane.
- Project the anomaly reason and supporting insights into the alert.
- Document identity-field assumptions because schemas can vary across sources and environments.
- Keep a lower-threshold hunting version and a more selective analytics-rule version.
