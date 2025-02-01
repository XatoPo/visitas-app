from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Permitir solicitudes desde tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

visitas = 0

@app.get("/visitas")
async def get_visitas():
    global visitas
    visitas += 1
    return JSONResponse({"visitas": visitas})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
