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
