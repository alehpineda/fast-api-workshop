from fastapi import FastAPI

from app.models import ModelName

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
    Path parameters
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
