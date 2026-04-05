# PatrolIQ Smart Safety Analytics

PatrolIQ is a Streamlit-based analytics dashboard for exploring Chicago crime patterns with geographic, temporal, and dimensionality-reduction visualizations.

## Features

- Dataset overview with key metrics and top crime categories
- Geographic hotspot visualization using map-based clustering output
- Temporal analysis (hourly trends and day-hour heatmap)
- Clustering algorithm comparison view
- PCA and t-SNE 2D projection visualizations

## Project Structure

- `streamlit_app/app.py` - main Streamlit entry point
- `streamlit_app/pages/` - multipage dashboard views
- `streamlit_app/utils.py` - shared data loading and safe sampling helpers
- `data/processed/` - prepared CSV files consumed by the app
- `src/save_models.py` - utility script to save scaler/PCA models

## Requirements

Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Run the App

From the project root:

```bash
cd streamlit_app
python -m streamlit run app.py
```

Then open the local URL shown in the terminal (typically `http://localhost:8501`).

## Data Files Expected

The app expects these files under `data/processed/`:

- `Crime_Clean.csv`
- `crime_hotspot_clusters.csv`
- `crime_pca_2d.csv`
- `crime_tsne_2d.csv`

## Notes

- Temporal analysis auto-derives `Hour` and `Day_of_Week` from `Date` if those columns are not present.
- Large chart pages use safe sampling to avoid errors when the dataset has fewer rows than expected.
