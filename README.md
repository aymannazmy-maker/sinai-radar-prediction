# Sinai Radar Prediction

Research project: Deep learning for radar site prediction on Sinai terrain.

## Research Objective

Reproduce and improve upon the paper:
"Enhancing precision and efficiency in a Joint Force Dynamic sensor allocation and target engagement with deep learning"

Goal: Train a U-Net model to predict MSAMS (Medium-Range Surface-to-Air Missile System) Target Engagement Radar (TER) coverage based on terrain topography.

## Methodology

1. Data source: NASA SRTM (30 m resolution)
2. Region: Central Sinai, 50x50 km around (29.5N, 34.0E)
3. Radar target: SA-27 GOLLUM (Buk-M3)
4. Coverage simulation: Splat! v1.4.2 with Longley-Rice
5. Training samples: 1,911 radar sites (matching paper)
6. Model: U-Net + ResNet34 (pretrained on ImageNet)
7. Output: Coverage maps in 16 dBm levels

## Project Structure

sinai-radar-prediction/
  README.md
  LICENSE
  requirements.txt
  .gitignore
  docs/
    04_experiment_log.md
    05_progress.md
  src/
    setup.py
    data_download.py
    splat_runner.py
  data/                 (git-ignored)
  notebooks/

## Quick Start

    git clone https://github.com/aymannazmy-maker/sinai-radar-prediction.git
    cd sinai-radar-prediction
    pip install -r requirements.txt

## Current Status

See docs/05_progress.md for detailed progress.

| Phase | Status |
|-------|--------|
| Setup | Complete |
| Data Prep | In Progress |
| Splat! Runs | Tested (1/1911) |
| Model Training | Pending |

## Links

- Splat!: https://www.qsl.net/kd2bd/splat.html
- SRTM: https://earthexplorer.usgs.gov

## License

MIT License - see LICENSE
