from data_ingestion import ingest_data
import pytest
from pyspark.errors.exceptions.captured import AnalysisException
from books_dataset import BooksDataset


def test_ingest_data():
    data = ingest_data(".\\data")

    assert isinstance(data, BooksDataset)
    assert data.books_df.count() == 99
    assert len(data.books_df.columns) == 23
    assert data.ratings_df.count() == 99
    assert len(data.ratings_df.columns) == 3


def test_ingest_data_invalid_path():
    with pytest.raises(AnalysisException):
        ingest_data(".\\data_invalid")
