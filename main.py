from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from routers import pages, auth, contact
import uvicorn

app = FastAPI(title="ОАО Крутогорье-Петковичи")

# Сессии (поменяй secret_key на свой!)
app.add_middleware(SessionMiddleware, secret_key="change-this-secret-key-in-production")

# Статика и шаблоны
app.mount("/static", StaticFiles(directory="static"), name="static")

# Подключаем роутеры
app.include_router(pages.router)
app.include_router(auth.router)
app.include_router(contact.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
