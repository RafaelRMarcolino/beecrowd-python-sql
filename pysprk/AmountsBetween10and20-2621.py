from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark.sql.functions import col
from decimal import Decimal




providersSchema = StructType(fields=[
    StructField('id', IntegerType(), True),
    StructField('name', StringType(), False),
    StructField('street', StringType(), False),
    StructField('city', StringType(), False),
    StructField('state', StringType(), False)  
])


providersData = [
    (1, 'Ajaxa', 'Rua Presidente Castelo Branco', 'Porto Alegre', 'RS'),
    (2, 'Sansul SA', 'AV Brasil', 'Rio de Janeiro', 'RJ'),
    (3, 'Pr Sheppard Chairso', 'Rua do Moinho', 'Santa Maria', 'RS'),
    (4, 'Elon Electro', 'Rua Apolo', 'São Paulo', 'SP'),
    (5, 'Mike Electro', 'Rua Pedro da Cunha', 'Curitiba', 'PR')
]

spark = SparkSession.builder.appName("providers").getOrCreate()
providers = spark.createDataFrame(providersData, schema=providersSchema)


providers.show()





spark = SparkSession.builder.appName("Exemplo").getOrCreate()

productsSchema = StructType(fields=[
    StructField('id', IntegerType(), False),
    StructField('name', StringType(), False),
    StructField('amount', IntegerType(), True),
    StructField('price', DecimalType(10, 2), False),
    StructField('id_providers', IntegerType(), True)
])

productsData = [
    (1, 'Blue Chair', 30, Decimal('300.00'), 5),
    (2, 'Red Chair', 50, Decimal('2150.00'), 2),
    (3, 'Disney Wardrobe', 400, Decimal('829.50'), 4),
    (4, 'Executive Chair', 17, Decimal('9.90'), 3),
    (5, 'Solar Panel', 30, Decimal('3000.25'), 4),
]

products = spark.createDataFrame(productsData, schema=productsSchema)

products.show()



# Renomeia a coluna 'name' no DataFrame 'providers'
providers = providers.withColumnRenamed("name", "provider_name")

# Filtra os produtos com quantidade entre 10 e 20 e cujo nome do fornecedor começa com 'P'
result = products.join(providers, products['id_providers'] == providers['id']).filter(
    (col("amount").between(10, 20)) & (col("provider_name").startswith("P"))
)

result.select('name').show()
