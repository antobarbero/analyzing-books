import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope="session")
def spark():
    yield SparkSession.builder.appName("Test").getOrCreate()
