# Experiment Log

This document logs every session of the project.

---

## [2026-10-04] Session 01 - Setup + Splat! + Test Run

### Objectives
- Set up Kaggle + GitHub environment
- Install and compile Splat! (Longley-Rice)
- Download SRTM data for central Sinai
- Convert SRTM to Splat! format
- Run first test on a single radar site

### Environment
| Component | Value |
|-----------|-------|
| Platform | Kaggle Notebooks |
| GPU | 2x Tesla T4 (29.2 GB total) |
| Python | 3.13.15 |
| PyTorch | 2.11.0+cu128 |
| CUDA | True |

### Actions Taken

#### Phase 1: Setup
1. Created GitHub repo: `sinai-radar-prediction`
2. Set up Kaggle account + verified phone (for GPU access)
3. Installed Python libraries: rasterio, pyproj, geopandas, shapely, folium, elevation
4. Generated Personal Access Token (PAT) on GitHub for authentication
5. Cloned repo to Kaggle: /kaggle/working/sinai-radar-prediction
6. Removed unwanted files from previous tests

#### Phase 2: Splat! Installation
7. Downloaded Splat! v1.4.2 source (~350 KB)
8. Extracted archive
9. Discovered build uses configure + make (not prebuilt Makefile)
10. Discovered configure requires user input (max analysis region size)
11. Solution: Used printf to auto-answer configure prompts
12. Successfully compiled Splat! -> splat binary (190 KB) + splat-hd

#### Phase 3: Data Preparation
13. Downloaded 2 SRTM tiles (SRTM-1, 1 arc-second):
    - N29E033.hgt (25 MB)
    - N29E034.hgt (25 MB)
14. Cropped 50x50 km region from central Sinai (29.5N, 34.0E):
    - Output: sinai_50km.npy (1620 x 1872 pixels)
    - Elevation range: 500-1400 m
15. Determined target: 1,911 radar sites (matching paper)
16. Converted SRTM to SDF using srtm2sdf-hd:
    - 29:30:325:326-hd.sdf (50.2 MB)
    - 29:30:326:327-hd.sdf (48.2 MB)

#### Phase 4: Test Run
17. Created test radar files (QTH, LRP, AZ)
18. Configured ~/.splat_path to point to data/raw/
19. Ran Splat! successfully with Longley-Rice model

### Results

#### Splat! Test Run
| Metric | Value |
|--------|-------|
| Time | 11.8 seconds |
| Output | test_output.ppm (24.72 MB) |
| Resolution | 2400 x 3600 pixels |
| Site report | Written |

#### Time Projection for 1,911 Sites
1911 sites x 11.8 sec = 22,550 sec = 6.26 hours

#### Size Projection for 1,911 Sites
1911 sites x 24.72 MB = 47.2 GB (exceeds Kaggle limits)

### Key Discoveries

#### Splat! Flags
- -c height : Compute LoS coverage for RX
- -R km : Range in kilometers
- -metric : Metric units
- -olditm : Use Longley-Rice (NOT ITWOM default) - REQUIRED
- -dbm : Output in dBm
- -o file : Output PPM file

#### File Formats
- .hgt : SRTM raw elevation (big-endian int16)
- .sdf : Splat! terrain data
- .qth : Transmitter location (DMS format)
- .lrp : Longley-Rice parameters
- .az : Antenna pattern

### Issues Identified

#### Issue 1: PPM Output Storage
Problem: 1,911 sites x 24.72 MB = 47 GB (exceeds Kaggle)
Options:
  A) Convert PPM to PNG (~80% smaller)
  B) Extract dBm values directly (~500 KB/site)
  C) Reduce range

#### Issue 2: Missing SRTM Regions
Splat! loaded 6 regions: 2 real + 4 assumed sea-level.
Acceptable for now (site at center).

### Verified Against Paper

| Element | Paper | Our Implementation | Match |
|---------|-------|---------------------|-------|
| Area | 50x50 km | 50x50 km (central Sinai) | YES |
| Target sites | 1,911 | 1,911 (planned) | YES |
| Site spacing | ~1.15 km | ~1.16 km | YES |
| SRTM resolution | 1 arc-second | 1 arc-second HD | YES |
| Splat! | Yes | v1.4.2 | YES |
| Longley-Rice | Yes | via -olditm | YES |
| dBm output | Yes | via -dbm | YES |
| 16 levels | Yes | planned | YES |

### Next Session (Day 2) — Planned

1. Resolve storage issue (test PPM to numpy conversion)
2. Generate 1,911 radar sites (grid 44x44 with margin)
3. Create QTH/LRP/AZ files for each site
4. Batch run Splat! with checkpointing
5. Save results to Drive

### Important Notes

- Kaggle session limits: 12 hours max per session
- Recommendation: Split 1,911 sites across multiple sessions
- Splat! binary: /kaggle/working/splat/splat-1.4.2/splat
- .splat_path file: ~/.splat_path -> points to data/raw/

---

*Log created: 2026-10-04*
