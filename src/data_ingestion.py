from pyspark.sql import SparkSession, DataFrame


def ingest_data(file_path: str) -> DataFrame:
    """
    Loads the data from the given `file_path` into a PySpark dataframe.

    :param file_path: Path of the file to be loaded.

    """
    spark = SparkSession.builder.appName("DataIngestion").getOrCreate()
    df = spark.read.csv(file_path, header=True, inferSchema=True)

    return df
