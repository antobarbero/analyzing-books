import attribute_names as an
from pyspark.sql.types import StructField, IntegerType, StringType, DoubleType, LongType

book_id = StructField(an.BOOK_ID, IntegerType())
title = StructField(an.TITLE, StringType())
original_publication_year = StructField(an.ORIGINAL_PUBLICATION_YEAR, IntegerType())
rating = StructField(an.RATING, IntegerType())
average_rating = StructField(an.AVERAGE_RATING, DoubleType())
reviews_count = StructField(an.REVIEWS_COUNT, LongType())
