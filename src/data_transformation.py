from pyspark.sql import DataFrame
from pyspark.sql.functions import count, avg
import attribute_names as an


def get_books_popularity_overtime(
    books_df: DataFrame, ratings_df: DataFrame
) -> DataFrame:
    """
    Groups and aggregates books data by year and calculates
    average ratings and review counts over time.
    """
    avg_ratings = ratings_df.groupby(an.BOOK_ID).agg(
        count(an.RATING).alias(an.REVIEWS_COUNT),
        avg(an.RATING).alias(an.AVERAGE_RATING),
    )
    books_df = books_df.select(an.BOOK_ID, an.TITLE, an.ORIGINAL_PUBLICATION_YEAR).join(
        avg_ratings, on=an.BOOK_ID, how="left"
    )

    return books_df
