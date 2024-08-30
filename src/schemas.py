import attribute_names as an
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

book_id = StructField(an.BOOK_ID, IntegerType())
title = StructField(an.TITLE, StringType())
original_publication_year = StructField(an.ORIGINAL_PUBLICATION_YEAR, IntegerType())
rating = StructField(an.RATING, IntegerType())

books_schema = StructType(
    [
        book_id,
        title,
        original_publication_year,
    ]
)

ratings_schema = StructType(
    [
        book_id,
        rating,
    ]
)
