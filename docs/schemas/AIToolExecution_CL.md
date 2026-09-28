# `AIToolExecution_CL` Schema Contract

`AIToolExecution_CL` is a repository-defined custom table for agent, plugin, connector, and function execution. It is not a built-in Microsoft Sentinel table.

## Required columns

| Column | Type | Purpose |
|---|---|---|
| `TimeGenerated` | `datetime` | Execution time |
| `UserPrincipalName_s` | `string` | Requesting user or workload |
| `SourceIP_s` | `string` | Source address |
| `AgentId_s` | `string` | Agent identifier |
| `ToolName_s` | `string` | Tool, connector, plugin, or function |
| `Result_s` | `string` | Success, failure, or denial result |
| `RiskLevel_s` | `string` | Environment-defined tool risk |
| `ApprovalStatus_s` | `string` | Human or policy approval state |

## Recommended columns

Include a correlation ID, target resource, parameters after secret redaction, execution duration, policy decision, data classification, output size, and originating AI session ID.

Do not ingest secrets, authorization headers, full access tokens, or sensitive tool parameters. Preserve a tamper-resistant correlation trail from the AI session to approval, execution, and result.
