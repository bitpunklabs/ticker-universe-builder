# Light / Medium / Heavy / Max

| Depth | Entity selection | Satellite maximum |
|---|---|---:|
| Light | Concise leader-only backbone | 0% |
| Medium | At least 70% of the declared reviewed leader roster | 0% |
| Heavy | All reviewed leaders and necessary differentiated peers | 20% |
| Max | Matching qualified Heavy, plus at least 30% entirely as Beta | 35% overall |

Light means every selected entity is a leader, not every market leader is selected. A leader
may have high measured price beta. The declared roster is the research denominator, not a
market-wide census. These percentages are design constraints, not optimal portfolio weights.

## Budgets and expansion

Declare positive, nondecreasing entity ceilings in the [coverage plan](coverage-plan.md).
References are additional. `target_count` can lower a ceiling, never raise it or discard necessary
coverage. Leave capacity unused when all gates pass; there is no bucket fallback.

Max requires `--seed heavy.json` from the same market, plan and source date. Preserve all Heavy
facts/bindings and add at least `ceil(0.30 * H)` qualified satellites. Repair necessary core
coverage in Heavy first. Follow Heavy display-group proportions with integer rounding only;
shortages do not transfer seats to another group. No group must expand individually.

Sector caps, total satellite share and export limits still bind; there is no separate growth
maximum. A ceiling below `H + ceil(0.30 * H)` is infeasible. Heavy at 20% satellites cannot add
30% entirely as Beta while keeping Max at 35%; report this conflict instead of changing labels,
removing protected members or relaxing gates. See [shortfall handling](recovery.md).

For a first Core migration, compare roughly with the supplied CN 463, US 378 and Crypto 53
security/asset/tool entries. These are historical comparison scales, not verified leader totals
or market defaults. Explain a larger economic scope before raising budgets.

## Archived replay

The 60/160/400/580 bases, breadth multipliers, theme levels and bucket targets belong to
explicit [legacy-policy.json](../assets/legacy-policy.json) replay only. They do not size current
builds. Earlier Max artifacts below 30% growth need expansion before current-contract republication.
