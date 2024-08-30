from pyspark.sql import SparkSession
from books_dataset import BooksDataset
from schemas import books_schema, ratings_schema


def ingest_data(files_path: str) -> BooksDataset:
    """
    Loads the data from the given `file_path` into a PySpark dataframe.

    :param files_path: Path of the file to be loaded.

    """
    # ToDo: settings for file names.
    spark = SparkSession.builder.appName("DataIngestion").getOrCreate()
    book_df = spark.read.csv(
        files_path + "\\books.csv", header=True, schema=books_schema
    )  # ToDo: define schema
    ratings_df = spark.read.csv(
        files_path + "\\ratings.csv", header=True, schema=ratings_schema
    )  # ToDo: define schema

    return BooksDataset(books_df=book_df, ratings_df=ratings_df)
