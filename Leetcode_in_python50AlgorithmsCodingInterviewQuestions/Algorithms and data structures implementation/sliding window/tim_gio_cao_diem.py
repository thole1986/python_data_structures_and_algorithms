
def tim_gio_cao_diem(don_hang, k):
    n = len(don_hang)

    # Tính tổng 4 giờ đầu tiên
    current_sum = sum(don_hang[0:k])
    max_sum = current_sum
    start_hour = 0
    print(f"Cửa sổ đầu tiên (0h → {k}h) - Đơn hàng:", don_hang[0:k])
    print("Tổng đơn =", current_sum)
    print("-" * 50)

    # Trượt cửa sổ
    for i in range(k, n):
        print("index: i -> ", i)
        gio_moi = don_hang[i]
        gio_cu = don_hang[i - k]
        print(f"Thêm giờ {i}h: {gio_moi} đơn")
        print(f"Bỏ giờ {i-k}h: {gio_cu} đơn")

        current_sum = current_sum + gio_moi - gio_cu
        print(
            f"Cửa sổ hiện tại ({i-k+1}h → {i+1}h) - Đơn hàng:",
            don_hang[i-k+1 : i+1]
        )
        print("Tổng đơn =", current_sum)
        
        if current_sum > max_sum:
            max_sum = current_sum
            start_hour = i - k + 1
            print("👉 Cao điểm mới!")
        
        print("-" * 50)
    
    print("✅ KẾT LUẬN")
    print(
        f"Khung giờ cao điểm nhất: {start_hour}h → {start_hour + k}h"
    )
    print("Tổng đơn:", max_sum)

    return start_hour, max_sum

don_hang = [12, 18, 25, 40, 55, 60, 45, 30, 20]
k = 4

tim_gio_cao_diem(don_hang, k)
