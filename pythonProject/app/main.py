from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pythonProject.app.adapters.inadpt.login_api import login_router
from pythonProject.app.adapters.inadpt.poke_api import poke_router
from pythonProject.app.adapters.inadpt.purchase_api import purchase_router
from pythonProject.app.adapters.inadpt.user_api import user_router

app = FastAPI()
app.include_router(purchase_router)
app.include_router(login_router)
app.include_router(user_router)
app.include_router(poke_router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"data": "This API manages your own pokemon collection!"}
