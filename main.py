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

@app.get("/products", tags=["Продукты"])
async def get_produtcs():
    return {"data" : shop_db}

@app.get("/products/{id}", tags=["Продукты"])
async def get_produtc(id: int):
    if shop_db.get(id, None):
        return {"data" : shop_db[id]}
    else:
        return {"msg" : "Товара не существует"}
    
@app.post("/products/", tags=["Продукты"])
async def add_product(data: dict):
    global id_product
    id: int = id_product
    if shop_db.get(id, None):
        shop_db[id] = data
        id_product += 1
        return {"msg" : "Данные добавлены"}
    else:
        return {"err" : "Такой товар существует!"}

@app.delete("/products/{id}", tags=["Продукты"])
async def delete_product(id: int):
    if shop_db.get(id, None):
        del shop_db[id]
        return {"msg" : f"Товар с id: {id} удален"}
    return {"err" : "Такой товар не существует!"}

@app.put("/products/{id}", tags=["Продукты"])
async def edit_product(id:int, data: dict):
    if shop_db.get(id, None):
        shop_db[id] = data
        return {"msg" : f"Товар с id: {id} обновлен"}
    return {"err" : "Такой товар не существует!"}

@app.patch("/products/{id}", tags=["Продукты"])
async def edit_product_partialy(id:int, data: dict):
    if shop_db.get(id, None):
        product = shop_db[id]
        for k, v in data.items():
            if product.get(k, None):
                shop_db[id][k] = v
                
        return {"msg" : f"Товар с id: {id} обновлен"}
    
    return {"err" : "Такой товар не существует!"}
            
        
        
