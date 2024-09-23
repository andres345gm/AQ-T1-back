from fastapi import FastAPI
from pythonProject.app.adapters.inadpt.user_api import user_router
app = FastAPI()
app.include_router(user_router)


@app.get("/")
def read_root():
    return {"data": "This API manages your own pokemon collection!"}