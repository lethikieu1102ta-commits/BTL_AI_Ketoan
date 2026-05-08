import math

# ==========================================
# PHẦN 1: TÍNH GIAI THỪA (ĐỆ QUY)
# ==========================================
def tinh_giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * tinh_giai_thua(n - 1)

# ==========================================
# PHẦN 2: TÍNH TRUNG BÌNH CỘNG
# ==========================================
def tinh_trung_binh(day_so):
    if len(day_so) == 0:
        return 0
    return sum(day_so) / len(day_so)

# ==========================================
# PHẦN 3: TÍNH LỢI NHUẬN LÃI KÉP (12 THÁNG)
# ==========================================
def tinh_loi_nhuan_12_thang(von_goc, lai_suat_thang):
    # Công thức: A = P * (1 + r)^n
    tong_tien = von_goc * (1 + lai_suat_thang)**12
    loi_nhuan = tong_tien - von_goc
    return loi_nhuan

# ==========================================
# PHẦN 4: CHẠY THỬ VÀ IN KẾT QUẢ (PHẢI CÓ PRINT MỚI HIỆN)
# ==========================================
print("--- KẾT QUẢ BÀI TẬP CƠ BẢN ---")

# 1. Chạy giai thừa
n = 5
print(f"1. Giai thừa của {n} là: {tinh_giai_thua(n)}")

# 2. Chạy trung bình cộng
doanh_thu_quy = [120, 150, 90, 200, 180]
print(f"2. Doanh thu trung bình các tháng: {tinh_trung_binh(doanh_thu_quy)}")

# 3. Chạy lãi kép
von = 100000000  # 100 triệu
lai = 0.005      # 0.5% mỗi tháng
loi_nhuan = tinh_loi_nhuan_12_thang(von, lai)
print(f"3. Với vốn {von:,} VNĐ, lãi {lai*100}%, lợi nhuận 1 năm là: {loi_nhuan:,.0f} VNĐ")