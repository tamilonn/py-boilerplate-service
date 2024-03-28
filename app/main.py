from fastapi import Depends, FastAPI
from contextlib import asynccontextmanager

import sys
import os


myDir = os.getcwd()
sys.path.append(myDir)

from pathlib import Path
path = Path(myDir)
a=str(path.parent.absolute())
sys.path.append(a)


from app.routers  import svc_routers_v1






@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load startup logic here...
    try:
        print('Before starting application....')
        yield
    finally:
    # Shut down logic here....
        print('After application is shut down....')


def create_app():

    app = FastAPI(lifespan=lifespan)

    #v1 routner mappings..
    app.include_router(svc_routers_v1.router)
    app.include_router(svc_routers_v1.router, prefix="/v1")

    return app

app= create_app()


@app.get("/")
async def root():
    return {"message": "This is py-boilerplate-service"}