# SOC Triage Workflow with KQL

## Goal

Help analysts move from alert to scope quickly.

## Triage Questions

1. Who is involved?
2. What happened?
3. When did it start?
4. What source IPs, devices, files, or agents are involved?
5. Is this isolated or widespread?
6. Is there sensitive data exposure?
7. What response action is required?

## Recommended Query Flow

### 1. Identify the User

```kql
SigninLogs
| where UserPrincipalName =~ "user@domain.com"
| where TimeGenerated > ago(7d)
| summarize Count=count(), IPs=make_set(IPAddress, 50), Apps=make_set(AppDisplayName, 50)
```

### 2. Identify Recent File Activity

```kql
OfficeActivity
| where TimeGenerated > ago(24h)
| where UserId =~ "user@domain.com"
| summarize Operations=count(), Files=make_set(SourceFileName, 50) by Operation
```

### 3. Identify Cloud Changes

```kql
AzureActivity
| where TimeGenerated > ago(24h)
| where Caller =~ "user@domain.com"
| project TimeGenerated, OperationNameValue, ActivityStatusValue, ResourceGroup, ResourceProviderValue
```
