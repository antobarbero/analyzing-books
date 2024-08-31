from pyspark.sql import SparkSession

import pytest


@pytest.fixture(scope="session")
def spark():
    """
    SparkSession to be reused across all tests.
    This SparkSession is optimised for processing small data on a single machine for testing.
    """
    spark = (
        SparkSession.builder.master(
            "local[1]"
        )  # specifies that spark is running on a local machine with one thread
        .appName("local-tests")
        .config("spark.executor.cores", "1")  # set cores to one
        .config("spark.executor.instances", "1")  # set executors to one
        .config(
            "spark.sql.shuffle.partitions", "1"
        )  # set the maximum number of partitions to 1
        .config(
            "spark.driver.bindAddress", "127.0.0.1"
        )  # Explicitly specify the driver bind address. Useful if your machine has also has a live connection to a remote cluster.
        .getOrCreate()
    )
    yield spark  # Yield instead of return to execute teardown code after the yield.
    spark.stop()
