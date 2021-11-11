from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"Message": "Welcome to FastApi and Docker by Lux Academy"}

@app.get("/login")
def login(username,password):
    return {"username":username, "password":password}

@app.get("/signup")
def signup(username,password,email,country):
    return{
        "username":username,
        "password":password,
        "email":email,
        "country":country
    }


