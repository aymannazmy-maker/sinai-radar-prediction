# Day 2 — 10 Sites Test (v2)

## Purpose

Verify that Splat! produces varied results with different radar sites,
after fixing the SDF/binary/colormap issues.

## Configuration

- **Splat! binary:** standard `splat` (not `splat-hd`)
- **SDF files:** standard mode (5.5 MB each)
- **Colormap:** 16 dBm levels (official Splat! colors)
- **LRP:** SA-27 GOLLUM (9500 MHz, Vertical, 1000W)
- **Range:** 50 km
- **RX height:** 100 m

## Results

| Site | Row | Col | Lat | Lon | Time (s) | Coverage (%) | Max L | Size (KB) |
|------|-----|-----|-----|-----|----------|--------------|-------|-----------|
| 5 | 0 | 5 | 29.275 | 33.801 | 14.2 | 1.32 | 16 | 7.9 |
| 40 | 0 | 40 | 29.275 | 34.223 | 14.1 | 12.48 | 16 | 93.0 |
| 440 | 10 | 5 | 29.380 | 33.801 | 14.1 | 1.28 | 16 | 7.6 |
| 475 | 10 | 41 | 29.380 | 34.235 | 13.8 | 13.36 | 16 | 106.5 |
| 876 | 20 | 5 | 29.484 | 33.801 | 15.8 | 0.89 | 16 | 10.6 |
| 911 | 20 | 40 | 29.484 | 34.223 | 15.2 | 8.51 | 16 | 109.2 |
| 1309 | 30 | 5 | 29.589 | 33.801 | 13.7 | 1.36 | 16 | 7.8 |
| 1344 | 30 | 41 | 29.589 | 34.235 | 14.0 | 12.96 | 16 | 105.0 |
| 1740 | 40 | 5 | 29.694 | 33.801 | 13.8 | 2.04 | 16 | 13.2 |
| 1775 | 40 | 40 | 29.694 | 34.223 | 13.9 | 10.77 | 16 | 86.8 |

## Key Findings

- **Coverage range:** 0.89% → 13.36%
  (range: 12.47 pp)
- **Time per site:** ~14.3s (consistent)
- **File size:** 7.6 → 109.2 KB
- **Variation confirmed:** West sites (Col 5) have lower coverage than East sites (Col 40)

## Full Run Estimate

- 1,911 sites × 14.3s = 7.6 hours
- Total storage: ~102.2 MB

## Files

- `levels/*.npy.gz` — Compressed level arrays (10 sites)
- `results.csv` — Summary of results
