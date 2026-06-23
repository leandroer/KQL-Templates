# KQL Style Guide

A consistent style makes queries easier to review, tune, and operationalize.

## Recommended Query Header

```kql
// Name: Suspicious Failed Sign-ins
// Description: Detects users with abnormal failed sign-in volume.
// Data Sources: SigninLogs
// Tactic: Credential Access
// Severity: Medium
// False Positives: Password reset, new device, travel
// Response: Validate user activity and review source IP reputation
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

## Naming Conventions

| Item | Convention |
|---|---|
| Files | `descriptive-query-name.kql` |
| Variables | `PascalCase` or descriptive names |
| Detection name | Clear behavior-based name |
| Severity | Informational, Low, Medium, High, Critical |
| Time windows | `Lookback`, `ThresholdWindow` |
