# app1.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pyodbc

app = FastAPI()

# Kết nối SQL Server
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=HUY-LT\\HUY;'
    'DATABASE=AppSinhVien;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

# Model lớp
class Lop(BaseModel):
    MaLop: str
    TenLop: str
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # hoặc ["http://127.0.0.1:5500"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/lop/")
def them_lop(lop: Lop):
    try:
        cursor.execute(
            "INSERT INTO Lop (MaLop, TenLop) VALUES (?, ?)",
            lop.MaLop, lop.TenLop
        )
        conn.commit()
        return {"message": "Đã thêm lớp thành công"}
    except pyodbc.IntegrityError:
        raise HTTPException(status_code=400, detail="Mã lớp đã tồn tại")


@app.get("/lop/")
def lay_danh_sach_lop():
    cursor.execute("SELECT MaLop, TenLop FROM Lop")
    rows = cursor.fetchall()
    return [{"MaLop": row[0], "TenLop": row[1]} for row in rows]
class SinhVien(BaseModel):
    MaSV: str
    TenSV: str
    Lop: str

@app.post("/sinhvien/")
def them_sinhvien(sv: SinhVien):
    try:
        cursor.execute(
            "INSERT INTO SinhVien (MaSV, TenSV, Lop) VALUES (?, ?, ?)",
            sv.MaSV, sv.TenSV, sv.Lop
        )
        conn.commit()
        return {"message": "Đã thêm sinh viên"}
    except pyodbc.IntegrityError:
        raise HTTPException(status_code=400, detail="Mã SV đã tồn tại")

@app.get("/sinhvien/{masv}")
def lay_sinhvien(masv: str):
    cursor.execute("SELECT MaSV, TenSV, Lop FROM SinhVien WHERE MaSV = ?", masv)
    row = cursor.fetchone()
    if row:
        return {"MaSV": row[0], "TenSV": row[1], "Lop": row[2]}
    raise HTTPException(status_code=404, detail="Không tìm thấy sinh viên")
@app.get("/sinhvien/")
def lay_danh_sach_sinhvien():
    cursor.execute("SELECT MaSV, TenSV, Lop FROM SinhVien")
    rows = cursor.fetchall()
    return [{"MaSV": row[0], "TenSV": row[1], "Lop": row[2]} for row in rows]
