"""Mini-project mức A: vẽ thẻ ASCII tĩnh bằng print()."""
import sys

# Đảm bảo hiển thị đúng tiếng Việt có dấu trong terminal Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# TODO 1: In hàng viền trên bằng + và -.
print("+----------------+")

# TODO 2: In lời chào giữa hai dấu |, giữ đúng độ rộng (18 ký tự).
print("| Xin chào Long! |")

# TODO 3: In hàng viền dưới bằng hàng trên.
print("+----------------+")

# TODO 4 (tự chọn): Thêm hình trang trí.
print("     /\\_/\\  ")
print("    ( o.o ) ")
print("     > ^ <  ")


