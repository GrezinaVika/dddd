from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="MyShop", version="0.0.1")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене указывайте конкретные домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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

count:int = 3

@app.get("/", tags=["Магазин"])
async def home():
    return {"data" : ["Welcome to my Shop"]}

@app.get("/products/", tags=["Продукты"])
async def get_products():
    return {"data" : shop_db}

@app.get("/products/{id}", tags=["Продукты"])
async def get_product(id: int):
    if shop_db.get(id, None):
        return {"data" : shop_db[id]}
    else:
        return {"msg" : "Товара не существует"}

@app.post("/products/", tags=["Продукты"])
async def add_product(data: dict):
    global count
    id = count
    if shop_db.get(id, None):
        return {"msg" : "Такой товар существует"}
    else:
        shop_db[id] = data
        count += 1
        return {"data" : data}

@app.put("/products/{id}", tags=["Продукты"])
async def edit_product(id: int, data: dict):
    if shop_db.get(id, None):
        shop_db[id] = data
        return {"data" : shop_db[id]}
    else:
        return {"msg" : "Товара не существует"}   


@app.patch("/products/{id}", tags=["Продукты"])
async def edit_partialy_product(id: int, data: dict):
    if shop_db.get(id, None):
        product = shop_db[id]
        for k, v in data.items():
            if product.get(k, None):
                shop_db[id][k] = v

        return {"data" : shop_db[id]}
    else:
        return {"msg" : "Товара не существует"}   
    
@app.delete("/products/{id}", tags=["Продукты"])
async def delete_product(id: int):
    if shop_db.get(id, None):
        product = shop_db[id]
        del shop_db[id]        
        return {"msg" : f"{product} был удален"}
    else:
        return {"msg" : "Товара не существует"}   
