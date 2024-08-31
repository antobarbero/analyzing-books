from pyspark.sql.types import StructType
import columns as c

books_schema = StructType(
    [
        c.book_id,
        c.title,
        c.original_publication_year,
    ]
)

ratings_schema = StructType(
    [
        c.book_id,
        c.rating,
    ]
)

# ToDo: define schema for output.
