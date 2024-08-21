from data_ingestion import ingest_data
import pytest
from pyspark.errors.exceptions.captured import AnalysisException


def test_ingest_data():
    data = ingest_data(".\\data\\books.csv")

    assert data.count() == 99
    assert len(data.columns) == 23


def test_ingest_data_invalid_path():
    with pytest.raises(AnalysisException):
        ingest_data(".\\data\\invalid.csv")
