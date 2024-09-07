from data_transformation import get_books_popularity_overtime
from pyspark.testing import assertDataFrameEqual
from schemas import books_schema, ratings_schema
from pyspark.sql.types import StructType
import columns as c


def test_get_books_popularity_overtime(spark):

    books_df = spark.createDataFrame(
        data=[
            (1, "Alice in Wonderland", 1800),
            (2, "The room", 1990),
            (3, "The house", 1996),
            (4, "Five dogs", 2020),
            (5, "Dracula", 1820),
            (6, "Bible", 1980),
            (7, "Bubble", 1980),
            (8, "The Caramel", 2020),
            (9, "The Cellphone", 1996),
        ],
        schema=books_schema,
    )
    ratings_df = spark.createDataFrame(
        data=[
            (1, 5),
            (1, 4),
            (1, 10),
            (2, 5),
            (2, 1),
            (2, 3),
            (3, 10),
            (3, 9),
            (4, 6),
            (5, 5),
            (5, 4),
            (5, 10),
            (5, 5),
            (5, 1),
            (6, 3),
            (6, 10),
            (7, 9),
            (8, 6),
            (8, 5),
            (8, 4),
            (8, 10),
            (8, 5),
            (9, 1),
            (9, 3),
            (9, 10),
            (9, 9),
            (9, 6),
        ],
        schema=ratings_schema,
    )

    df = get_books_popularity_overtime(books_df, ratings_df)

    expected_df = spark.createDataFrame(
        data=[
            (1, "Alice in Wonderland", 1800, 3, 6.333333333333333),
            (2, "The room", 1990, 3, 3.0),
            (3, "The house", 1996, 2, 9.5),
            (4, "Five dogs", 2020, 1, 6.0),
            (5, "Dracula", 1820, 5, 5.0),
            (6, "Bible", 1980, 2, 6.5),
            (7, "Bubble", 1980, 1, 9.0),
            (8, "The Caramel", 2020, 5, 6.0),
            (9, "The Cellphone", 1996, 5, 5.8),
        ],
        schema=StructType(
            [
                c.book_id,
                c.title,
                c.original_publication_year,
                c.reviews_count,
                c.average_rating,
            ]
        ),
    )

    assertDataFrameEqual(df, expected_df)


# ToDo: Add negative test cases
