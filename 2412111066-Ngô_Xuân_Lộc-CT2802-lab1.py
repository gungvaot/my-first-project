
from data_handler import doc_du_lieu
from sach_operations import them_sach, xem_danh_sach, tim_kiem_sach, sua_sach, xoa_sach
from muon_tra import muon_sach, tra_sach
from menu import hien_thi_menu


def main():
    danh_sach = doc_du_lieu()

    while True:
        hien_thi_menu()
        lua_chon = input("Chon chuc nang: ").strip()

        if lua_chon == "1":
            them_sach(danh_sach)
        elif lua_chon == "2":
            xem_danh_sach(danh_sach)
        elif lua_chon == "3":
            tim_kiem_sach(danh_sach)
        elif lua_chon == "4":
            sua_sach(danh_sach)
        elif lua_chon == "5":
            xoa_sach(danh_sach)
        elif lua_chon == "6":
            muon_sach(danh_sach)
        elif lua_chon == "7":
            tra_sach(danh_sach)
        elif lua_chon == "0":
            print("Cam on da su dung chuong trinh. Tam biet!")
            break
        else:
            print("Lua chon khong hop le, vui long chon lai.")


if __name__ == "__main__":
    main()