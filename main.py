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


@app.get("/", tags=["Магазин"])
async def home():
    return {"data" : "Welcome to my Shop"}

@app.get("/products", tags=["Продукты"])
async def get_produtcs():
    return {"data" : shop_db}

@app.get("/products/{id}", tags=["Продукты"])
async def get_produtc(id: int):
    if shop_db.get(id, None):
        return {"data" : shop_db[id]}
    else:
        return {"msg" : "Товара не существует"}
    
@app.post("/products/{id}", tags=["Продукты"])
async def add_product(data: dict):
    id: int = len(shop_db.keys())
    if shop_db.get(id, None):
        shop_db[id] = data
        return {"msg" : "Данные добавлены"}
    else:
        return {"err" : "Такой товар существует!"}

