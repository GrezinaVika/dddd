from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
from src.api.products import router as products_router


app = FastAPI(title="MyShop", version="0.0.1")
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.get("/", tags=["Магазин"])
async def home():
    return {"data" : [
        "Welcome to my Shop",
        "Распродажа воды",
        "У нас самые низкие цены"
        ]}

app.include_router(products_router)




 



    
