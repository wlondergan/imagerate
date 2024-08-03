import os
from fastpi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    