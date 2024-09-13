from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"data": "This API manages your own pokemon collection!"}