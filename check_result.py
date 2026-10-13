import chdb

query = """
SELECT *
FROM file('/work/curated/city_revenue/*.parquet', Parquet)
ORDER BY revenue DESC
"""

print(chdb.query(query, "Pretty"))

