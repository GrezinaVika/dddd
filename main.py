from fastapi import FastAPI

app = FastAPI(title="MyShop", version="0.0.1")

shop_db ={
    0 : {
        "name" : "Шампунь",
        "quantity": 3,
        "price" : 50
    },
    1 : {
        "name" : "Пицца",
        "quantity": 30,
        "price" : 500
    },
    2 : {
        "name" : "Вода",
        "quantity": 10,
        "price" : 50
    },
}

id_product = 3


@app.get("/", tags=["Магазин"])
async def home():
    return {"data" : "Welcome to my Shop"}

@app.get("/products/", tags=["Продукты"])
async def get_produtcs():
    return {"data" : shop_db}

@app.post("/products/", tags=["Продукты"])
async def create_product(data: dict):
    global id_product
    shop_db[id_product] = data
    id_product += 1
    return {"msg" : "Товар добавлен"}

@app.get("/products/{id}", tags=["Продукты"])
async def get_produtc(id: int):
    if shop_db.get(id, None):
        return {"data" : shop_db[id]}
    else:
        return {"msg" : "Товара не существует"}

@app.delete("/products/{id}", tags=["Продукты"])
async def delete_product(id: int):
    if shop_db.get(id, None):
        del shop_db[id]
        return {"msg" : "Товар удален"}
    else:
        return {"msg" : "Товара не существует"}


