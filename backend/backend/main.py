from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_FILE = "db.json"

from pydantic import BaseModel, field_validator

class IzinTalep(BaseModel):
    ad: str
    izin_turu: str
    baslangic: str
    bitis: str
    aciklama: str

    @field_validator("bitis")
    @classmethod
    def check_dates(cls, v, info):
        bas = info.data.get("baslangic")
        if bas and v < bas:
            raise ValueError("Bitiş tarihi başlangıçtan önce olamaz")
        return v

# JSON dosyası yoksa oluştur
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump([], f)

def read_db():
    with open(DB_FILE, "r") as f:
        return json.load(f)

def write_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)

from fastapi import HTTPException

@app.post("/izin-talep")
def create_izin(talep: IzinTalep):
    try:
        data = read_db()
        new = talep.dict()
        new["id"] = max([i["id"] for i in data], default=0) + 1
        new["durum"] = "Bekliyor"
        data.append(new)
        write_db(data)
        return new
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/izinler")
def get_izinler():
    return read_db()

@app.put("/izin-durum/{id}")
def update(id: int, durum: str):
    try:
        data = read_db()
        for i in data:
            if i["id"] == id:
                i["durum"] = durum
                write_db(data)
                return i
        raise HTTPException(status_code=404, detail="Kayıt bulunamadı")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))