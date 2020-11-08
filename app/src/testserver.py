from fastapi import FastAPI

app = FastAPI()

@app.get("/retoibm/sumar/{sumando01}/{sumando02}")
async def read_item(sumando01 : int,sumando02 : int):
	def test_read_item():
		assert sumando01 == int

	return {"resultado": sumando01 + sumando02}

