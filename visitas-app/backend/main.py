from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()
visitas = 0

@app.get("/visitas")
async def get_visitas():
    global visitas
    visitas += 1
    return JSONResponse({"visitas": visitas})
