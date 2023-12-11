from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_home():
    respone = {"message": "Congratulations! You've reached the homepage!"}
    return respone

@app.get("/items")
def get_items():
    respone = {"message":{"Laptops, Headsets and iPhones"}}
    return respone

@app.get("/hello")
def get_hello():
    respone = {"message":{"Hello right back at you, gorgeous"}}
    return respone