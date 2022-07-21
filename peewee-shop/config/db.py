from peewee import PostgresqlDatabase

postgres_db = PostgresqlDatabase(
    database="peewee_shop",
    user="edil",
    password="9722",
    host="localhost",
    port="5432"
)