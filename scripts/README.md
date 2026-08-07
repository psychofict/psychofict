# Profile maintenance runbook

## Claude Code usage badges

```bash
python3 scripts/refresh-stats.py   # then commit + push README.md
```

Reads `~/.config/claude-token-tracker/history.db` (the claude-token-tracker widget's
accumulated store) and rewrites the shields.io badge block between the
`<!-- CLAUDE-STATS:START/END -->` markers in README.md. It replaces the whole block,
so it always converges to current data. Never edit those numbers by hand.

## Stats / streak cards

The README embeds two self-hosted card services (Vercel account `psychofict`):

| Card | Vercel project | URL | Token env var |
|------|----------------|-----|---------------|
| GitHub stats + top languages | `grs` | grs-iota.vercel.app | `PAT_1` |
| Streak | `streak` | streak-kappa.vercel.app | `TOKEN` |

**If a card shows "Something went wrong"**, its GitHub token has died. Both died
2026-08-06 when a 30-day PAT expired — and the endpoints still returned HTTP 200 +
`image/svg+xml`, so check the SVG *text*, not the status code.

Fix (per project):

```bash
vercel link --project grs        # or streak
vercel env rm PAT_1 production   # TOKEN for streak
vercel env add PAT_1 production  # paste a classic PAT, scopes: repo + read:user, no expiry
vercel redeploy https://grs-iota.vercel.app
```

As of 2026-08-07 both hold the gh CLI's OAuth token as a stopgap — `gh auth logout`
will kill the cards until a dedicated PAT is swapped in.

## Contribution snake

`.github/workflows/snake.yml` runs daily and pushes to the `output` branch. If the
snake image breaks, check the Actions tab first.

## Pinned repos

No public API. Reorder via the profile page ("Customize your pins" + move buttons).
The reorder POSTs are async and can race — after reordering, verify twice a minute
apart:

```bash
gh api graphql -f query='{ user(login: "psychofict") { pinnedItems(first: 6, types: REPOSITORY) { nodes { ... on Repository { nameWithOwner } } } } }' --jq '[.data.user.pinnedItems.nodes[].nameWithOwner]'
```

Intended order: PixCon, CW-BASS, FARCLUSS, hwpkit, claudehop, claude_ai_usage_widget.

## Facts that age

The HTML comment at the top of README.md lists every claim that can go stale (paper
statuses, leaderboard ranks, platform counts) and where to verify each. Sweep it when
anything ships or publishes.
