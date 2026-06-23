# KQL Basics

Kusto Query Language is used across Microsoft Sentinel, Defender XDR Advanced Hunting, Azure Monitor, Log Analytics, and several Microsoft security platforms.

## Basic Query Shape

```kql
TableName
| where TimeGenerated > ago(24h)
| where Condition == "value"
| project TimeGenerated, UserPrincipalName, IPAddress
```

## Important Concepts

### Table

A table stores telemetry.

Examples:

- `SigninLogs`
- `AuditLogs`
- `SecurityEvent`
- `DeviceProcessEvents`
- `OfficeActivity`
- `AzureActivity`

### Pipe Operator

The pipe operator `|` sends the result of one step into the next step.

```kql
SigninLogs
| where TimeGenerated > ago(24h)
| summarize Count=count() by ResultType
```

### Time Filtering

Always filter by time early.

```kql
| where TimeGenerated > ago(24h)
```

This improves performance and avoids expensive queries.

### Projection

Use `project` to choose only the columns needed.

```kql
| project TimeGenerated, UserPrincipalName, IPAddress, ResultType
```

### Extend

Use `extend` to create new calculated fields.

```kql
| extend RiskLevel = iff(ResultType != 0, "Failed", "Success")
```

### Summarize

Use `summarize` to aggregate data.

```kql
SigninLogs
| where TimeGenerated > ago(24h)
| summarize FailedLogons=count() by UserPrincipalName
```

## Analyst Tip

Start simple. Build one line at a time, run it, validate the output, then add the next operator.
