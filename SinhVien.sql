use master;
go
create database AppSinhVien
go
use AppSinhVien;

create table SinhVien (
    MaSV NVARCHAR(20) PRIMARY KEY,
    TenSV NVARCHAR(100) NOT NULL,
    Lop NVARCHAR(50) NOT NULL
);

create table Lop (
	MaLop varchar(10) primary key,
	TenLop nvarchar (255) 
	)

	INSERT INTO Lop (MaLop, TenLop)
VALUES 
('L01', N'CNTT 16-01'),
('L02', N'CNTT 16-02'),
('L03', N'CNTT 16-03'),
('L04', N'KHMT 16-01');

SELECT * FROM SinhVien;

