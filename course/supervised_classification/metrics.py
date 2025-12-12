import pandas as pd
import plotly.express as px
from sklearn.metrics import classification_report
from course.utils import find_project_root
from pathlib import Path
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


VIGNETTE_DIR = Path('data_cache') / 'vignettes' / 'supervised_classification'


def metric_report(y_test_path, y_pred_path, report_path):
    y_test = pd.read_csv(y_test_path)
    y_pred = pd.read_csv(y_pred_path)
    """Create a pandas data frame called report which contains your classifier results"""
    classifier_results = classification_report(y_test, y_pred, output_dict=True)
    report = pd.DataFrame(classifier_results)
    report.transpose().to_csv(report_path, index=True)


def metric_report_lda():
    base_dir = find_project_root()
    y_test_path = base_dir / 'data_cache' / 'energy_y_test.csv'
    y_pred_path = base_dir / 'data_cache' / 'models' / 'lda_y_pred.csv'
    report_path = base_dir / 'data_cache' / 'vignettes' / 'supervised_classification' / 'lda.csv'
    metric_report(y_test_path, y_pred_path, report_path)


def metric_report_qda():
    base_dir = find_project_root()
    y_test_path = base_dir / 'data_cache' / 'energy_y_test.csv'
    y_pred_path = base_dir / 'data_cache' / 'models' / 'qda_y_pred.csv'
    report_path = base_dir / 'data_cache' / 'vignettes' / 'supervised_classification' / 'qda.csv'
    metric_report(y_test_path, y_pred_path, report_path)


def plot_confmat(y_test_path, y_pred_path, outpath):
    y_test = pd.read_csv(y_test_path).squeeze()
    y_pred = pd.read_csv(y_pred_path).squeeze()
    labels = sorted(y_test.unique())
    cm = confusion_matrix(y_test, y_pred, labels=labels)
    fig = px.imshow(
        cm,
        text_auto=True,
        x=labels,
        y=labels,
        color_continuous_scale="Blues",
        labels=dict(x="Predicted", y="Actual"),
        title="Confusion Matrix"
    )
    fig.update_layout(width=600, height=600)
    fig.write_html(outpath)


def confusion_matrix_report(y_test_path, y_pred_path, cm_path):
    y_test = pd.read_csv(y_test_path)
    y_pred = pd.read_csv(y_pred_path)
    cm = confusion_matrix(y_test, y_pred)
    cm_df = pd.DataFrame(cm)
    cm_df.to_csv(cm_path, index=False)
    
    
def confusion_matrix_lda():
    base_dir = find_project_root()
    y_test_path = base_dir / "data_cache" / "energy_y_test.csv"
    y_pred_path = base_dir / "data_cache" / "models" / "lda_y_pred.csv"
    outpath = base_dir / VIGNETTE_DIR / "lda_confmat.html"
    plot_confmat(y_test_path, y_pred_path, outpath)


def confusion_matrix_qda():
    base_dir = find_project_root()
    y_test_path = base_dir / "data_cache" / "energy_y_test.csv"
    y_pred_path = base_dir / "data_cache" / "models" / "qda_y_pred.csv"
    outpath = base_dir / VIGNETTE_DIR / "qda_confmat.html"
    plot_confmat(y_test_path, y_pred_path, outpath)
