# KQL Templates

A professional, practical KQL reference library for Microsoft Sentinel, Microsoft Defender XDR, Microsoft Entra ID, Microsoft Purview, Azure, Microsoft 365, and AI Security detection engineering.

This repository is designed for security engineers, SOC analysts, detection engineers, incident responders, threat hunters, and architects who want to learn, write, tune, and operationalize KQL queries.

## What This Repository Provides

- Beginner-friendly KQL learning path
- Real-world Microsoft Sentinel and Defender query templates
- Detection engineering patterns
- Threat hunting examples
- Investigation queries
- Microsoft Purview data security queries
- AI Security and Agentic AI detections
- Query tuning and performance guidance
- Reusable query templates
- Sentinel analytics rule examples
- Analyst-focused explanations for each query

## Who This Is For

| Role | How to Use This Repo |
|---|---|
| SOC Analyst | Run triage and investigation queries during alerts and incidents |
| Detection Engineer | Convert hunting logic into Sentinel analytics rules |
| Incident Responder | Scope users, hosts, IPs, files, and cloud activity |
| Security Architect | Understand telemetry requirements and detection coverage |
| KQL Beginner | Learn query patterns with explained examples |

## Repository Structure

```text
.
├── docs/
│   ├── fundamentals/
│   ├── reference/
│   └── use-cases/
├── templates/
├── queries/
│   ├── identity/
│   ├── endpoint/
│   ├── network/
│   ├── cloud/
│   ├── email/
│   ├── ai-security/
│   ├── purview/
│   └── sentinel-operations/
├── analytics-rules/
├── workbooks/
└── scripts/
```

## Recommended Learning Path

1. Start with `docs/fundamentals/01-kql-basics.md`
2. Review `docs/fundamentals/02-common-operators.md`
3. Use `templates/query-template.kql`
4. Practice with `queries/identity/failed-logons-by-user.kql`
5. Learn joins with `docs/fundamentals/03-joins-and-correlation.md`
6. Convert hunting logic into analytics rules using `analytics-rules/README.md`

## Core KQL Concepts Covered

- `where`
- `project`
- `extend`
- `summarize`
- `join`
- `let`
- `parse`
- `mv-expand`
- `make_set()`
- `arg_max()`
- `bin()`
- `distinct`
- `union`
- `materialize()`
- time windows
- entity mapping
- detection tuning

## Recommended Topics

Use these GitHub topics:

```text
kql
microsoft-sentinel
defender-xdr
threat-hunting
detection-engineering
incident-response
security-operations
microsoft-purview
azure-security
entra-id
soc
siem
```

## Repository Notice

This repository is maintained as a professional cybersecurity portfolio and research project focused on detection engineering, incident response, threat hunting, security automation, and AI security.
Content is published for educational, technical, and professional reference purposes. This repository is not currently accepting community contributions, pull requests, issue submissions, or feature requests.
All content is provided as-is and should be reviewed, tested, and validated before use in production environments.

## Disclaimer

These queries are intended for defensive security operations, threat hunting, and detection engineering. Always validate and tune thresholds before production deployment.

requests are not currently being accepted.

