from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: bool | None = None
@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    return {'file_path': file_path}


class ModelName(Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning WTF"}
    if model_name.value == 'lenet':
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}


@app.get('/')
async def root():
    return {"message": "Hello, World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# @app.put('/items/{item_id}')
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_price": item.price,"item_id": item_id}
