from fastapi import FastAPI
import psycopg2

app = FastAPI()


@app.get("/retoibm/sumar/{sumando01}/{sumando02}")
async def read_item(sumando01 : int,sumando02 : int):
	connection = psycopg2.connect(user="postgres", password="docker", host="10.244.0.35", port="5432", database="docker")
	cursor = connection.cursor()
	postgres_insert_query = """ INSERT INTO sumar (num_01, num_02, resultado) VALUES (%s,%s,%s)"""
	record_to_insert = (sumando01, sumando02, sumando01 + sumando02)
	cursor.execute(postgres_insert_query, record_to_insert)
	connection.commit()
	count = cursor.rowcount
	print (count, "Record inserted successfully into sumar table")
	print (sumando01 + sumando02)
	return {"resultado": sumando01 + sumando02}
