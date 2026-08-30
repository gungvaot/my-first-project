"""
Module xu ly chuc nang muon sach va tra sach
"""

from data_handler import ghi_du_lieu


def muon_sach(danh_sach):
    print("\n--- MUON SACH ---")
    ma = input("Nhap ma sach can muon: ").strip()

    for sach in danh_sach:
        if sach["ma"] == ma:
            if sach["conlai"] <= 0:
                print(f"Sach '{sach['ten']}' da het, khong the muon.")
                return
            sach["conlai"] -= 1
            ghi_du_lieu(danh_sach)
            print(f"Muon sach '{sach['ten']}' thanh cong! Con lai: {sach['conlai']}")
            return

    print(f"Khong tim thay sach co ma '{ma}'.")


def tra_sach(danh_sach):
    print("\n--- TRA SACH ---")
    ma = input("Nhap ma sach can tra: ").strip()

    for sach in danh_sach:
        if sach["ma"] == ma:
            if sach["conlai"] >= sach["soluong"]:
                print("Tat ca sach nay deu da co san, khong the tra them.")
                return
            sach["conlai"] += 1
            ghi_du_lieu(danh_sach)
            print(f"Tra sach '{sach['ten']}' thanh cong! Con lai: {sach['conlai']}")
            return

    print(f"Khong tim thay sach co ma '{ma}'.")
