"""
In the past the studio has made an event where several movies were on sale,
 we want to know what movies these were.

Your job to help us is to select the ID and name of movies whose price is less than 2.00.

"""


from pyspark.sql.functions import *
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructField, StructType, IntegerType, StringType

moviesSchema = StructType(fields=[
    StructField('id', IntegerType(), True),
    StructField('name', StringType(), True),
    StructField('id_prices ', IntegerType(), True)
])

moviesData = [
    (1,	'Batman', 3),
    (2, 'The Battle of the Dark River',	3),
    (3,	'White Duck', 5),
    (4,	'Breaking Barriers', 4),
    (5,	'The Two Hours', 2)
]

movies = spark.createDataFrame(moviesData, moviesSchema)

pricesSchema = StructType(fields=[
    StructField('id', IntegerType(), True),
    StructField('categorie', StringType(), True),
    StructField('value', FloatType(), True)
])

pricesData = [
    (1,	"Releases",	3.50),
    (2,	"Bronze Seal", 2.00),
    (3,	"Silver Seal", 2.50),
    (4,	"Gold Seal", 3.00),
    (5,	"Promotion", 1.50)
]

prices = spark.createDataFrame(pricesData, pricesSchema)

resultado =  prices.alias('A').join(movies.alias('B'), col('A.id') == col('B.id'), 'inner').where(col('A.value') < 2.0)
resultado.select(col('A.id'), col('B.name')).show()

