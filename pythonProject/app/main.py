from fastapi import FastAPI

from pythonProject.app.adapters.inadpt.login_api import login_router
from pythonProject.app.adapters.inadpt.user_api import user_router
from pythonProject.app.adapters.inadpt.purchase_api import purchase_router
app = FastAPI()
app.include_router(user_router)
app.include_router(purchase_router)
app.include_router(login_router)


@app.get("/")
def read_root():
    return {"data": "This API manages your own pokemon collection!"}