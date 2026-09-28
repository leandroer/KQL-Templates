# KQL Style Guide

A consistent style makes queries easier to review, tune, and operationalize.

## Recommended Query Header

```kql
// Name: Suspicious Failed Sign-ins
// Description: Detects users with abnormal failed sign-in volume.
// Query Type: Hunting | Investigation | Detection
// Platforms: Microsoft Sentinel, Microsoft Entra ID
// Tables: SigninLogs
// Required Connectors: Microsoft Entra ID
// MITRE ATT&CK: T1110 Brute Force
// Severity: Medium
// Lookback: 24h
// Entity Fields: UserPrincipalName, IPAddress
// False Positives: Password reset, new device, travel
// Tuning Guidance: Use tenant-specific failure codes and approved-source exclusions
// Response Guidance: Validate user activity and review source IP reputation
// Validation Status: Example
// Related Analytics Rule: None
```

## Best Practices

- Filter by time early.
- Project only required columns.
- Use readable variable names with `let`.
- Include comments for analysts.
- Use `make_set(Column, 50)` instead of unlimited `make_set(Column)`.
- Avoid unnecessary wildcard projection.
- Tune thresholds based on environment baselines.
- Include entity fields for Sentinel mapping.
- Separate hunting queries from production detections.
- Return `TimeGenerated` from scheduled analytics-rule queries.
- Preserve every entity, custom-detail, and alert-template field in the final output.
- Use `column_ifexists()` when documented schema evolution requires compatibility.
- Prefer ASIM unifying parsers for portable Sentinel content where appropriate.
- Treat anomaly scores and keyword matches as context rather than verdicts.

## Naming Conventions

| Item | Convention |
|---|---|
| Files | `descriptive-query-name.kql` |
| Variables | `PascalCase` or descriptive names |
| Detection name | Clear behavior-based name |
| Severity | Informational, Low, Medium, High, Critical |
| Time windows | `Lookback`, `ThresholdWindow` |
