from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine, Column, Integer, String, declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "postgresql://postgres:developer22@postgres-service:5432/visitas_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Visitas(Base):
    __tablename__ = "visitas"
    id = Column(Integer, primary_key=True, index=True)
    count = Column(Integer, default=0)
    environment = Column(String, default="development")

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Permitir solicitudes desde tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/visitas")
async def get_visitas(db: Session = Depends(get_db)):
    visitas = db.query(Visitas).first()
    if not visitas:
        visitas = Visitas(count=1)
        db.add(visitas)
    else:
        visitas.count += 1
    db.commit()
    db.refresh(visitas)
    return JSONResponse({"visitas": visitas.count, "environment": visitas.environment})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
