# Incident Response Runbook

## Secret exposure

1. Revoke the key immediately.
2. Remove it from files, archives, screenshots, and Git history.
3. Replace it with a restricted key.
4. Run a repository secret scan.
5. Record the incident without copying the secret.

## Unsafe response

1. Stop live use.
2. Preserve the prompt category and execution metadata, not patient identifiers.
3. Add a red-team regression case.
4. Update deterministic safety rules.
5. Re-run all evaluations before release.

## Incorrect inventory output

1. Stop operational recommendations.
2. Validate the source CSV.
3. Compare calculations with a manual reference.
4. Correct data or code.
5. Re-run local and unit tests.

## External-tool compromise

1. Disable the MCP/A2A connection.
2. Revoke credentials.
3. Review tool calls and accessed resources.
4. Restore from trusted configuration.
5. Re-enable only after least-privilege review.
