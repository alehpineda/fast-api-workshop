from fastapi import FastAPI

from app.models import ModelName, Pokemon

app = FastAPI()


@app.get("/")
async def root():
    """
    Regresa un mensaje de hola mundo
    """
    return {"mensaje": "Hola Mundo!"}


@app.get("/items/{item_id}")
async def get_item(item_id: int):
    """
    Path parameters - variables declaradas en el path de la url
    """
    return {"item_id": item_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    """
    Path parameters con Enum Class
    """
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "mensaje": "Deep Learning rifa!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "mensaje": "LeCNN todas las imgs!"}

    return {"model_name": model_name, "mensaje": "Ten los residuos"}


fake_items_db = []


@app.post("/items/")
async def post_items(item_name: str, item_price: int):
    fake_items_db.append(
        {"item_name": item_name, "item_price": item_price}
    )
    return fake_items_db


@app.post("/pokemon/")
async def post_pokemon(pokemon: Pokemon):
    return pokemon
