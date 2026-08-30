"""
Module xu ly cac chuc nang: them, xem, tim kiem, sua, xoa sach
"""

from data_handler import ghi_du_lieu


def them_sach(danh_sach):
    print("\n--- THEM SACH MOI ---")
    ma = input("Nhap ma sach: ").strip()

    for sach in danh_sach:
        if sach["ma"] == ma:
            print(f"Loi: Ma sach '{ma}' da ton tai!")
            return

    ten = input("Nhap ten sach: ").strip()
    tacgia = input("Nhap tac gia: ").strip()

    try:
        soluong = int(input("Nhap so luong: ").strip())
        if soluong < 0:
            print("So luong khong hop le!")
            return
    except ValueError:
        print("So luong phai la so nguyen!")
        return

    sach_moi = {
        "ma": ma,
        "ten": ten,
        "tacgia": tacgia,
        "soluong": soluong,
        "conlai": soluong,
    }
    danh_sach.append(sach_moi)
    ghi_du_lieu(danh_sach)
    print(f"Da them sach '{ten}' thanh cong!")


def xem_danh_sach(danh_sach):
    print("\n--- DANH SACH SACH TRONG THU VIEN ---")
    if not danh_sach:
        print("Thu vien chua co sach nao.")
        return

    print(f"{'Ma':<10}{'Ten sach':<30}{'Tac gia':<20}{'SL':<6}{'Con lai':<8}")
    print("-" * 74)
    for sach in danh_sach:
        print(f"{sach['ma']:<10}{sach['ten']:<30}{sach['tacgia']:<20}"
              f"{sach['soluong']:<6}{sach['conlai']:<8}")


def tim_kiem_sach(danh_sach):
    print("\n--- TIM KIEM SACH ---")
    tu_khoa = input("Nhap ma sach hoac ten sach can tim: ").strip().lower()

    ket_qua = [
        sach for sach in danh_sach
        if tu_khoa in sach["ma"].lower() or tu_khoa in sach["ten"].lower()
    ]

    if not ket_qua:
        print("Khong tim thay sach phu hop.")
        return

    print(f"{'Ma':<10}{'Ten sach':<30}{'Tac gia':<20}{'SL':<6}{'Con lai':<8}")
    print("-" * 74)
    for sach in ket_qua:
        print(f"{sach['ma']:<10}{sach['ten']:<30}{sach['tacgia']:<20}"
              f"{sach['soluong']:<6}{sach['conlai']:<8}")


def sua_sach(danh_sach):
    print("\n--- SUA THONG TIN SACH ---")
    ma = input("Nhap ma sach can sua: ").strip()

    for sach in danh_sach:
        if sach["ma"] == ma:
            print(f"Thong tin hien tai: {sach['ten']} - {sach['tacgia']} - SL: {sach['soluong']}")
            ten_moi = input(f"Ten sach moi (Enter de giu nguyen '{sach['ten']}'): ").strip()
            tacgia_moi = input(f"Tac gia moi (Enter de giu nguyen '{sach['tacgia']}'): ").strip()
            soluong_moi = input(f"So luong moi (Enter de giu nguyen '{sach['soluong']}'): ").strip()

            if ten_moi:
                sach["ten"] = ten_moi
            if tacgia_moi:
                sach["tacgia"] = tacgia_moi
            if soluong_moi:
                try:
                    sl_moi = int(soluong_moi)
                    da_muon = sach["soluong"] - sach["conlai"]
                    sach["soluong"] = sl_moi
                    sach["conlai"] = max(0, sl_moi - da_muon)
                except ValueError:
                    print("So luong khong hop le, giu nguyen gia tri cu.")

            ghi_du_lieu(danh_sach)
            print("Cap nhat thanh cong!")
            return

    print(f"Khong tim thay sach co ma '{ma}'.")


def xoa_sach(danh_sach):
    print("\n--- XOA SACH ---")
    ma = input("Nhap ma sach can xoa: ").strip()

    for i, sach in enumerate(danh_sach):
        if sach["ma"] == ma:
            xac_nhan = input(f"Ban co chac muon xoa '{sach['ten']}'? (y/n): ").strip().lower()
            if xac_nhan == "y":
                danh_sach.pop(i)
                ghi_du_lieu(danh_sach)
                print("Da xoa sach thanh cong!")
            else:
                print("Da huy thao tac xoa.")
            return

    print(f"Khong tim thay sach co ma '{ma}'.")
