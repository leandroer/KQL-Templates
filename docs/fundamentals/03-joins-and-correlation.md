# Joins and Correlation

Joins are essential for detection engineering because they allow analysts to connect weak signals into stronger detections.

## Common Join Types

| Join Type | Use Case |
|---|---|
| `inner` | Return only matching records |
| `leftouter` | Keep all records from the left side, add matches from the right |
| `leftanti` | Find records on the left with no match on the right |
| `innerunique` | Default KQL join; returns one match per key from left |

## Example: Failed Sign-in Followed by Successful Sign-in

```kql
let Failed =
SigninLogs
| where TimeGenerated > ago(24h)
| where ResultType != 0
| project UserPrincipalName, FailedTime=TimeGenerated, FailedIP=IPAddress;
let Success =
SigninLogs
| where TimeGenerated > ago(24h)
| where ResultType == 0
| project UserPrincipalName, SuccessTime=TimeGenerated, SuccessIP=IPAddress;
Failed
| join kind=inner Success on UserPrincipalName
| where SuccessTime between (FailedTime .. FailedTime + 30m)
| where FailedIP != SuccessIP
```

## Engineering Guidance

Use joins carefully. Always reduce each side of the join first with:

- time filters
- `project`
- `summarize`
- `distinct`

This keeps queries fast and less expensive.
