import sys
sys.stdout.reconfigure(encoding="utf-8")

# Deck values (from Slide 2 chart, as presented)
deck_nl = 1936026
deck_nd = 480599
deck_ig = 737788
deck_total = deck_nl + deck_nd + deck_ig

# Deck swapped (invert New Logo and New Door labels)
swap_nl = deck_nd  # 480,599
swap_nd = deck_nl  # 1,936,026
swap_ig = deck_ig  # 737,788

# Deck swapped minus Independents (remove $226,218 from New Logo)
indep_ar = 226218
swap_adj_nl = swap_nl - indep_ar  # 480,599 - 226,218 = 254,381
swap_adj_nd = swap_nd
swap_adj_ig = swap_ig
swap_adj_indep = indep_ar

# Our calculation
our_nl = 572605
our_nd = 1721482
our_ig = 887336
our_total = our_nl + our_nd + our_ig

# Our calculation minus Independents
our_adj_nl = our_nl - indep_ar  # 572,605 - 226,218 = 346,387
our_adj_indep = indep_ar

print("=" * 100)
print("JAN + FEB SALE TYPE — FOUR-WAY COMPARISON")
print("=" * 100)
print()
print(f"  {'Sale Type':<14} {'Deck':>14} {'Deck Swapped':>14} {'Swapped -Indep':>14} {'Our Analysis':>14}")
print(f"  {'-'*14} {'-'*14} {'-'*14} {'-'*14} {'-'*14}")
print(f"  {'New Logo':<14} ${deck_nl:>13,.0f} ${swap_nl:>13,.0f} ${swap_adj_nl:>13,.0f} ${our_adj_nl:>13,.0f}")
print(f"  {'Independent':<14} {'':>14} {'':>14} ${swap_adj_indep:>13,.0f} ${our_adj_indep:>13,.0f}")
print(f"  {'New Door':<14} ${deck_nd:>13,.0f} ${swap_nd:>13,.0f} ${swap_adj_nd:>13,.0f} ${our_nd:>13,.0f}")
print(f"  {'Integration':<14} ${deck_ig:>13,.0f} ${swap_ig:>13,.0f} ${swap_adj_ig:>13,.0f} ${our_ig:>13,.0f}")
print(f"  {'-'*14} {'-'*14} {'-'*14} {'-'*14} {'-'*14}")
print(f"  {'TOTAL':<14} ${deck_total:>13,.0f} ${deck_total:>13,.0f} ${deck_total:>13,.0f} ${our_total:>13,.0f}")
print()

# Percentages
print(f"  {'Sale Type':<14} {'Deck':>14} {'Deck Swapped':>14} {'Swapped -Indep':>14} {'Our Analysis':>14}")
print(f"  {'-'*14} {'-'*14} {'-'*14} {'-'*14} {'-'*14}")
print(f"  {'New Logo':<14} {deck_nl/deck_total*100:>13.1f}% {swap_nl/deck_total*100:>13.1f}% {swap_adj_nl/deck_total*100:>13.1f}% {our_adj_nl/our_total*100:>13.1f}%")
print(f"  {'Independent':<14} {'':>14} {'':>14} {swap_adj_indep/deck_total*100:>13.1f}% {our_adj_indep/our_total*100:>13.1f}%")
print(f"  {'New Door':<14} {deck_nd/deck_total*100:>13.1f}% {swap_nd/deck_total*100:>13.1f}% {swap_adj_nd/deck_total*100:>13.1f}% {our_nd/our_total*100:>13.1f}%")
print(f"  {'Integration':<14} {deck_ig/deck_total*100:>13.1f}% {swap_ig/deck_total*100:>13.1f}% {swap_adj_ig/deck_total*100:>13.1f}% {our_ig/our_total*100:>13.1f}%")

# Deltas between Swapped-Indep and Our Analysis
print()
print("=" * 100)
print("DELTA: DECK SWAPPED (minus Indep) vs OUR ANALYSIS")
print("=" * 100)
print()
print(f"  {'Sale Type':<14} {'Swapped -Indep':>14} {'Our Analysis':>14} {'Delta':>14}")
print(f"  {'-'*14} {'-'*14} {'-'*14} {'-'*14}")
print(f"  {'New Logo':<14} ${swap_adj_nl:>13,.0f} ${our_adj_nl:>13,.0f} ${our_adj_nl-swap_adj_nl:>13,.0f}")
print(f"  {'Independent':<14} ${swap_adj_indep:>13,.0f} ${our_adj_indep:>13,.0f} ${our_adj_indep-swap_adj_indep:>13,.0f}")
print(f"  {'New Door':<14} ${swap_adj_nd:>13,.0f} ${our_nd:>13,.0f} ${our_nd-swap_adj_nd:>13,.0f}")
print(f"  {'Integration':<14} ${swap_adj_ig:>13,.0f} ${our_ig:>13,.0f} ${our_ig-swap_adj_ig:>13,.0f}")
print(f"  {'-'*14} {'-'*14} {'-'*14} {'-'*14}")
print(f"  {'TOTAL':<14} ${deck_total:>13,.0f} ${our_total:>13,.0f} ${our_total-deck_total:>13,.0f}")
