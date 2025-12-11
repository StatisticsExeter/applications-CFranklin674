import pandas as pd
import plotly.express as px
from pathlib import Path
from course.utils import find_project_root

VIGNETTE_DIR = Path('data_cache') / 'vignettes' / 'unsupervised_classification'


def plot_scatter():
    base_dir = find_project_root()
    df = pd.read_csv(base_dir / 'data_cache' / 'la_collision.csv')
    outpath = base_dir / VIGNETTE_DIR / 'scatterplot.html'
    title = "Crash types in each Local Authority"
    fig = _scatter(df, title)
    fig.write_html(outpath)


def _scatter(df, title):
    """When called with dataframe 'df' and a string 'title'
    Return a plotly express object which is a scatterplot of all numeric variables
    in the dataframe. The title should be as provided in the function call"""
    numeric_values = df.select_dtypes(include="number")
    fig = px.scatter_matrix(numeric_values, title=title)
    return fig


def plot_corr_matrix():
    base_dir = find_project_root()
    df = pd.read_csv(base_dir / 'data_cache' / 'la_collision.csv')
    corr = df.corr(numeric_only=True)
    outpath = base_dir / VIGNETTE_DIR / 'corr_matrix.html'
    fig = px.imshow(
                  corr,
                  text_auto=True,
                  color_continuous_scale='RdBu_r',
                  title='Correlation Matrix'
                  )
    fig.write_html(outpath)


def data_preview():
    base_dir = find_project_root()
    df = pd.read_csv(base_dir / 'data_cache' / 'la_collision.csv')
    outpath = base_dir / VIGNETTE_DIR / 'preview.html'
    df.head().to_html(outpath, index=False)
