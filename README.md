# Sinai Radar Prediction

## 🎯 Research Objective
Develop a deep learning model that predicts MSAMS (Medium-Range Surface-to-Air Missile System) Target Engagement Radar (TER) locations based on terrain topography.

## 🧪 Methodology
1. Download SRTM elevation data for Sinai Peninsula
2. Generate radar grid points across the region
3. Compute radar coverage using Splat! (Longley-Rice model)
4. Build a supervised learning dataset (terrain → coverage)
5. Train U-Net + ResNet34 to predict coverage
6. Evaluate and compare with baseline methods

## 📊 Reproducibility
All experiments are reproducible via:
- Fixed random seeds
- Config-driven experiments (`configs/`)
- Detailed logs in `experiments/`
- Notebooks as lab journal (`notebooks/`)

## 📚 Documentation
See `docs/` for:
- Research protocol
- Data sources
- Methodology
- Experiment log
- Results

## 🚀 Quick Start
```bash
git clone https://github.com/YOUR_USER/sinai-radar-prediction.git
cd sinai-radar-prediction
pip install -r requirements.txt
