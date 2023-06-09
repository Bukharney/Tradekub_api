from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import (
    user,
    auth,
    account,
    stock,
    broker,
    bank_tsc,
    order,
    news,
    turnover,
    dividend,
    portfolio,
    nolti,
    analytics,
)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user.router)
app.include_router(auth.router)
app.include_router(account.router)
app.include_router(stock.router)
app.include_router(broker.router)
app.include_router(bank_tsc.router)
app.include_router(order.router)
app.include_router(news.router)
app.include_router(turnover.router)
app.include_router(dividend.router)
app.include_router(portfolio.router)
app.include_router(nolti.router)
app.include_router(analytics.router)


@app.get("/")
def root():
    return "Hello World, from tradekub!"
