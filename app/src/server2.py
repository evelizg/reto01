from fastapi import FastAPI
import psycopg2

app = FastAPI()


@app.get("/retoibm/sumar/{sumando01}/{sumando02}")
async def read_item(sumando01 : int,sumando02 : int):
    return {"resultado": sumando01 + sumando02}

try:
   connection = psycopg2.connect(user="docker",
                                  password="docker",
                                  host="172.22.0.3",
                                  port="5432",
                                  database="docker")
   cursor = connection.cursor()

   postgres_insert_query = """ INSERT INTO sumar (num_uno, num_dos) VALUES (%s,%s)"""
   record_to_insert = (10, 20)
   cursor.execute(postgres_insert_query, record_to_insert)

   connection.commit()
   count = cursor.rowcount
   print (count, "Record inserted successfully into sumar table")

except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into  sumar", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

