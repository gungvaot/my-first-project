"""
Module xu ly doc/ghi du lieu sach tu file dataThuVien.txt
Dinh dang moi dong: MaSach|TenSach|TacGia|SoLuong|SoLuongConLai
"""

import os

FILE_NAME = "dataThuVien.txt"


def doc_du_lieu():
    """Doc du lieu tu file dataThuVien.txt, tra ve danh sach sach (list of dict)."""
    danh_sach = []
    if not os.path.exists(FILE_NAME):
        open(FILE_NAME, "w", encoding="utf-8").close()
        return danh_sach

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        for dong in f:
            dong = dong.strip()
            if not dong:
                continue
            phan = dong.split("|")
            if len(phan) != 5:
                continue
            sach = {
                "ma": phan[0],
                "ten": phan[1],
                "tacgia": phan[2],
                "soluong": int(phan[3]),
                "conlai": int(phan[4]),
            }
            danh_sach.append(sach)
    return danh_sach


def ghi_du_lieu(danh_sach):
    """Ghi toan bo danh sach sach xuong file dataThuVien.txt (ghi de)."""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for sach in danh_sach:
            dong = f"{sach['ma']}|{sach['ten']}|{sach['tacgia']}|{sach['soluong']}|{sach['conlai']}\n"
            f.write(dong)
