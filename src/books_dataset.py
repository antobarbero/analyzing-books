from dataclasses import dataclass
from pyspark.sql.dataframe import DataFrame


@dataclass
class BooksDataset:
    """It holds all the data."""

    books_df: DataFrame
    ratings_df: DataFrame
