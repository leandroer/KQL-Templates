# Common Microsoft Security Tables

| Table | Platform | Typical Use |
|---|---|---|
| `SigninLogs` | Microsoft Entra ID | Interactive sign-ins |
| `AADNonInteractiveUserSignInLogs` | Microsoft Entra ID | Token and non-interactive sign-ins |
| `AuditLogs` | Microsoft Entra ID | Directory changes, role changes, app consent |
| `SecurityEvent` | Windows / Sentinel | Windows security events |
| `DeviceProcessEvents` | Defender XDR | Process execution |
| `DeviceNetworkEvents` | Defender XDR | Endpoint network activity |
| `DeviceFileEvents` | Defender XDR | File activity |
| `EmailEvents` | Defender XDR | Email delivery and threat data |
| `EmailUrlInfo` | Defender XDR | URLs in emails |
| `OfficeActivity` | Microsoft 365 / Purview | SharePoint, Exchange, Teams, OneDrive activity |
| `AzureActivity` | Azure | Control-plane Azure operations |
| `AzureDiagnostics` | Azure | Resource diagnostic logs |
| `SecurityAlert` | Sentinel / Defender | Security alerts |
| `SecurityIncident` | Sentinel | Sentinel incident data |
| `BehaviorAnalytics` | Microsoft Sentinel UEBA | Behavior anomalies and investigation priority |
| `IdentityInfo` | Microsoft Sentinel UEBA | User, group, role, and identity context |
| `Anomalies` | Microsoft Sentinel | Anomaly-rule results and supporting context |

## UEBA prerequisites

`BehaviorAnalytics` and `IdentityInfo` require Microsoft Sentinel UEBA to be enabled and connected to supported identity and activity sources. Field availability can vary by source and tenant configuration. Inspect the schema in the target workspace before promoting an example to production.
