# `AIApp_CL` Schema Contract

`AIApp_CL` is a repository-defined custom table for AI application activity. It is not a built-in Microsoft Sentinel table. Implement it with a Data Collection Rule or adapt the queries to an existing schema.

## Required columns

| Column | Type | Purpose |
|---|---|---|
| `TimeGenerated` | `datetime` | Event time |
| `UserPrincipalName_s` | `string` | User or workload identity |
| `SourceIP_s` | `string` | Source address |
| `SessionId_s` | `string` | AI interaction session |
| `Application_s` | `string` | AI application or interface |
| `Prompt_s` | `string` | Submitted prompt or instruction |
| `Response_s` | `string` | Model response |

## Optional columns

| Column | Type | Purpose |
|---|---|---|
| `SensitivityClassification_s` | `string` | Output data classification |
| `Model_s` | `string` | Model or deployment identifier |
| `ContentSafetyResult_s` | `string` | Safety or prompt-shield result |
| `TokenCount_d` | `real` | Token consumption |

## Privacy and security

Prompts and responses can contain personal data, credentials, proprietary content, or regulated information. Minimize collection, apply access controls and retention, redact secrets where possible, and document the lawful and operational purpose before ingestion.

Legacy custom-log suffixes are used by the examples. For DCR-created columns without suffixes, normalize at ingestion or provide a parser using `column_ifexists()`.
