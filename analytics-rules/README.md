# Sentinel Analytics Rules

This folder contains examples and templates for converting KQL into Microsoft Sentinel scheduled analytics rules.

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
