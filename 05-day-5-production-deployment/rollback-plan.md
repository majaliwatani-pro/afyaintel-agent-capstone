# Rollback Plan

## Release strategy

1. Run all local evaluations.
2. Build an immutable versioned image.
3. Deploy to a non-production environment.
4. Test health, stock, Swahili, and safety paths.
5. Route limited approved traffic.
6. Expand only after review.

## Rollback triggers

- Safety regression
- Incorrect inventory calculations
- Authentication failure
- Secret exposure
- High error rate
- Unapproved external tool access

## Rollback action

- Route traffic to the last known-good revision.
- Disable model and external integrations.
- Preserve privacy-safe logs.
- Add a regression test.
- Re-release only after all gates pass.
