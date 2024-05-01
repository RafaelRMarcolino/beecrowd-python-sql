"""
The sales industry wants to make a promotion for all clients that are legal entities. 
For this you must display the name of the customers that are legal entity.
"""

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark.sql.functions import col


spark = SparkSession.builder.appName("customers").getOrCreate()


customersSchema = StructType(fields=[
    StructField('id', IntegerType(), True),
    StructField('name', StringType(), True),
    StructField('street', StringType(), False),
    StructField('city', StringType(), False),
    StructField('state', StringType(), False),
    StructField('credit_limit', IntegerType(), False),
])


customersData = [
    (1, "Nicolas Diogo Cardoso", "Acesso Um", "Porto Alegre", "RS", 475),
    (2, "Cecília Olivia Rodrigues", "Rua Sizuka Usuy", "Cianorte", "PR", 3170),
    (3, "Augusto Fernando Carlos Eduardo Cardoso", "Rua Baldomiro Koerich", "Palhoça", "SC", 1067),
    (4, "Nicolas Diogo Cardoso", "Acesso Um", "Porto Alegre", "RS", 475),
    (5, "Sabrina Heloisa Gabriela Barros", "Rua Engenheiro Tito Marques Fernandes", "Porto Alegre", "RS", 4312),
    (6, "Joaquim Diego Lorenzo Araújo", "Rua Vitorino", "Novo Hamburgo", "RS", 2314),
]


customers = spark.createDataFrame(customersData, schema=customersSchema)


legal_personSchema = StructType(fields=[
    StructField('id_customers', IntegerType(), True),
    StructField('cnpj', StringType(), False),
    StructField('contact', StringType(), True),
])


legal_person_data = [
    (1, '85883842000191', '99767-0562'),
    (2, '47773848000117', '99100-8965'),
]


legal_person = spark.createDataFrame(legal_person_data, schema=legal_personSchema)


resultado = customers.alias('A').join(legal_person.alias('B'), col('A.id') == col('B.id_customers'), 'left_outer')


clientes_pessoa_juridica = resultado.filter(col('B.id_customers').isNotNull())


clientes_pessoa_juridica.select('A.name').show()
