from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import psycopg2

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Permitir solicitudes desde tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Conexión a la base de datos
def get_db_connection():
    conn = psycopg2.connect(
        dbname="visitas_db",
        user="postgres",
        password="developer22",
        host="localhost",
        port="5432"
    )
    return conn

@app.get("/visitas")
async def get_visitas():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO visitas (ip_cliente) VALUES ('127.0.0.1')")
    conn.commit()
    cur.execute("SELECT COUNT(*) FROM visitas")
    visitas = cur.fetchone()[0]
    cur.close()
    conn.close()
    return JSONResponse({"visitas": visitas})

@app.post("/entorno")
async def set_entorno(tipo: str):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO entorno (tipo) VALUES (%s)", (tipo,))
    conn.commit()
    cur.close()
    conn.close()
    return JSONResponse({"status": "entorno registrado"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
