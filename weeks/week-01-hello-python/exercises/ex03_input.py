"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào
# Ví dụ: "Xin chào, Minh!"
ten = input("Nhập tên của bạn:Long")
print("Xin chào,", ten, "!")

# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh
# Gợi ý: Nhớ chuyển input sang int!
tuoi_nhap = input("Nhập tuổi của bạn:19 ")

if tuoi_nhap.isdigit():
    tuoi = int(tuoi_nhap)
    nam_sinh = 2026 - tuoi
    print("Bạn sinh năm:2007", nam_sinh)


# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
# Ví dụ output:
# Nhập số thứ nhất: 15
# Nhập số thứ hai: 27
# Tổng: 15 + 27 = 42
so_thu_nhat = int(input("Nhập số thứ nhất: "))
so_thu_hai = int(input("Nhập số thứ hai: "))

tong = so_thu_nhat + so_thu_hai

print("Tổng:", so_thu_nhat, "+", so_thu_hai, "=", tong)

# TODO 4 (Thử thách): Tạo Mad Libs mini
# Hỏi người dùng nhập: tên, tính từ, con vật, số
# Rồi in ra câu chuyện vui
ten = input("Nhập tên của bạn: ")
tinh_tu = input("Nhập một tính từ: ")
con_vat = input("Nhập tên con vật: ")
so = int(input("Nhập một con số: "))

print("\n===== CÂU CHUYỆN VUI =====")
print(ten, "có một chú", con_vat, "rất", tinh_tu)
print("Mỗi ngày, chú", con_vat, "chạy", so, "vòng quanh sân.")
print("Cả hai trở thành đôi bạn thân!")

"""
Bài tập 03: Trò chuyện với Python 💬
=====================================
Mục tiêu: Sử dụng input() để nhận dữ liệu từ người dùng
"""

# TODO 1: Hỏi tên người dùng và in lời chào
# Ví dụ: "Xin chào, Minh!"


# TODO 2: Hỏi tuổi người dùng, tính và in năm sinh
# Gợi ý: Nhớ chuyển input sang int!


# TODO 3: Hỏi người dùng nhập 2 số, tính và in tổng
# Ví dụ output:
# Nhập số thứ nhất: 15
# Nhập số thứ hai: 27
# Tổng: 15 + 27 = 42


# TODO 4 (Thử thách): Tạo Mad Libs mini
# Hỏi người dùng nhập: tên, tính từ, con vật, số
# Rồi in ra câu chuyện vui
