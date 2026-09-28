# Sentinel Analytics Rules

This folder contains deployable examples for converting validated KQL into Microsoft Sentinel scheduled analytics rules. Treat thresholds, exclusions, connector identifiers, and query periods as starting points that must be tested against the target environment.

## Rule Catalog

| Domain | Rule | Primary tables |
|---|---|---|
| Identity | Password spray against multiple users | `SigninLogs` |
| Endpoint | Suspicious PowerShell execution | `DeviceProcessEvents` |
| Cloud | Successful Azure resource deletion | `AzureActivity` |
| Purview | Mass SharePoint or OneDrive downloads | `OfficeActivity` |
| AI security | Prompt injection indicators | `AIApp_CL` |
| UEBA | High-priority anomaly for a privileged identity | `BehaviorAnalytics`, `IdentityInfo` |

## Query-to-Incident Flow

```mermaid
flowchart LR
    Q["KQL result"] --> E["Entity mappings"]
    Q --> C["Custom details"]
    E --> A["Sentinel alert"]
    C --> A
    A --> G["Event grouping"]
    G --> I["Incident"]
    I --> P["Investigation playbook"]
```

## Analyst Query vs Analytics Rule

An analyst query helps with investigation. An analytics rule should be:

- precise
- tuned
- mapped to entities
- mapped to MITRE ATT&CK
- assigned a severity
- documented with false positives
- supported by response guidance

## Recommended Rule Lifecycle

1. Write a hunting query.
2. Validate results for 7-30 days.
3. Identify false positives.
4. Add allowlists or threshold tuning.
5. Add entity mapping.
6. Convert to analytics rule.
7. Create incident response guidance.
8. Review after deployment.

## Deployment Checklist

- Confirm every required connector and table is populated.
- Run the query across at least 7–30 days of representative data.
- Replace generic thresholds with environment baselines.
- Verify every entity mapping column is present in the final query output.
- Confirm ATT&CK mappings describe the detected behavior, not merely the data source.
- Review alert grouping, incident grouping, suppression, and lookback overlap.
- Test positive, negative, and expected-benign cases before enabling incidents.
- Record the validation date and evidence in the pull request or release notes.
