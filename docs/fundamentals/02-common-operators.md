# Common KQL Operators

## where

Filters rows.

```kql
SigninLogs
| where ResultType != 0
```

## project

Selects columns.

```kql
SigninLogs
| project TimeGenerated, UserPrincipalName, IPAddress
```

## extend

Creates or modifies columns.

```kql
SigninLogs
| extend IsFailure = ResultType != 0
```

## summarize

Aggregates data.

```kql
SigninLogs
| summarize Count=count() by UserPrincipalName
```

## join

Correlates data across tables.

```kql
SigninLogs
| where ResultType != 0
| join kind=inner (
    AuditLogs
    | where OperationName has "password"
) on UserPrincipalName
```

## let

Creates reusable variables.

```kql
let Lookback = 24h;
SigninLogs
| where TimeGenerated > ago(Lookback)
```

## make_set

Creates a dynamic array of unique values.

```kql
SigninLogs
| summarize IPs=make_set(IPAddress, 50) by UserPrincipalName
```

Always include a max size, such as `50`, to avoid warnings and inefficient queries.

## arg_max

Returns the latest row per group.

```kql
SigninLogs
| summarize arg_max(TimeGenerated, *) by UserPrincipalName
```

## bin

Groups timestamps into fixed intervals.

```kql
SigninLogs
| summarize Count=count() by bin(TimeGenerated, 1h)
```
