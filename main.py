from fastapi import FastAPI, HTTPException
from package_sorter import Package
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Package Classification API"}


class PackageModel(BaseModel):
    width: float
    height: float
    length: float
    mass: float


@app.post("/classify")
def classify(pkg: PackageModel):
    try:
        result = Package(pkg.width, pkg.height, pkg.length,
                         pkg.mass).classify()
        return {"classification": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
