# Purview and Microsoft 365 Audit Assumptions

The Purview examples use `OfficeActivity` for broadly available SharePoint and OneDrive operations. Sensitivity-label fields are not guaranteed to be present with the same names in every tenant, connector, workload, or audit event.

Before deploying label-aware rules:

1. Inspect representative events for the target operations.
2. Confirm whether label information is present directly, nested in a dynamic property, or available only from another Purview data source.
3. Replace `SensitivityLabel` and `OldSensitivityLabel` compatibility expressions with the authoritative tenant fields.
4. Test labeled, unlabeled, downgraded, and unchanged events.
5. Confirm that missing fields cannot silently turn the rule into a zero-result detection.

The external-sharing hunting query intentionally detects sharing behavior without claiming that sensitivity is known. The corresponding analytics rule is an adaptable schema example until its label source has been validated in the target workspace.
