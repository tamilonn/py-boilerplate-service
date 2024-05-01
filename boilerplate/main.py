import sys
import os
from pathlib import Path

from fastapi import Depends, FastAPI
from contextlib import asynccontextmanager
import logging

import uvicorn
from dotenv import load_dotenv, dotenv_values

# path.parent.absolute..why??
cwd = os.getcwd()
sys.path.append(cwd)
cwd_path = Path(cwd)
workdir_path = cwd_path.parent.absolute()
sys.path.append(str(workdir_path))
print(cwd)
print(workdir_path)

from boilerplate.routers import svc_routers_v1
from boilerplate.database import engine
from boilerplate import  models

# initialize logger
logger = logging.getLogger(__file__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Application startup logic here...
    try:
        logger.info('After application started.....now starting server startup processes..')
        ####### LOAD CONFIGURATION LOGIC HERE....

           

        yield
    finally:
        # Application Shut down logic here....
        logger.info('Before application is shut down or closed....')


def create_app():
    app = FastAPI(lifespan=lifespan)

    # v1 router mappings..
    app.include_router(svc_routers_v1.router, prefix="/v1")

    # create config table and setup table
    models.Base.metadata.create_all(engine)

    return app


app = create_app()


@app.get("/")
async def root():
    return {"message": "This is boilerplate-service"}


# if __name__ == '__main__':
#     uvicorn.run(app, host='0.0.0.0', port=8000)
