# ASIM Queries

These examples use Microsoft Sentinel Advanced Security Information Model unifying parsers so the detection logic can operate across compatible data sources. Confirm parser availability and supported parameters in the target workspace.

| Query | Parser | Native counterpart |
|---|---|---|
| Password spray | `_Im_Authentication` | `queries/identity/password-spray-indicator.kql` |
| Office application spawning a shell | `_Im_ProcessCreate` | `queries/endpoint/suspicious-powershell-execution.kql` |
| Suspicious outbound ports | `_Im_NetworkSession` | `queries/network/suspicious-outbound-connections.kql` |

Filtering parameters are passed to parsers where supported to reduce the volume normalized at query time. Treat parameter names as version-sensitive and validate them against current ASIM schema documentation.
