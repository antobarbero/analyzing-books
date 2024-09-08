from run_pipeline import run_pipeline


def test_run_pipeline():
    """Runs full pipeline with a test dataset."""
    run_pipeline(files_path=".\\data")
