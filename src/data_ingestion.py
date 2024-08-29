from pyspark.sql import SparkSession
from books_dataset import BooksDataset


def ingest_data(file_path: str) -> BooksDataset:
    """
    Loads the data from the given `file_path` into a PySpark dataframe.

    :param file_path: Path of the file to be loaded.

    """
    # ToDo: settings for file names.
    spark = SparkSession.builder.appName("DataIngestion").getOrCreate()
    book_df = spark.read.csv(
        file_path + "\\books.csv", header=True, inferSchema=True
    )  # ToDo: define schema
    ratings_df = spark.read.csv(
        file_path + "\\ratings.csv", header=True, inferSchema=True
    )  # ToDo: define schema

    return BooksDataset(books_df=book_df, ratings_df=ratings_df)
