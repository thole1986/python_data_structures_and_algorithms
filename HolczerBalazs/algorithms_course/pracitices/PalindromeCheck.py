# Hàm kiểm tra chuỗi s có phải palindrome không
def is_palindrome(s):
    # Lưu bản gốc của chuỗi
    original_string = s

    # Đảo ngược chuỗi s
    reversed_string = reverse(s)

    # So sánh chuỗi gốc và chuỗi đảo ngược
    if original_string == reversed_string:
        return True  # Nếu giống nhau → là palindrome

    return False  # Nếu khác nhau → không phải palindrome


# Hàm đảo ngược chuỗi
def reverse(data):
    # Chuyển chuỗi thành danh sách các ký tự để dễ hoán đổi
    data = list(data)

    # Con trỏ bắt đầu: chỉ phần tử đầu
    start_index = 0
    # Con trỏ kết thúc: chỉ phần tử cuối
    end_index = len(data) - 1

    # Lặp cho đến khi 2 con trỏ gặp nhau
    while end_index > start_index:
        # Hoán đổi ký tự đầu và ký tự cuối
        data[start_index], data[end_index] = data[end_index], data[start_index]

        # Di chuyển con trỏ vào trong
        start_index += 1
        end_index -= 1

    # Chuyển danh sách ký tự trở lại chuỗi
    return ''.join(data)


if __name__ == '__main__':
    # Kiểm tra chuỗi "Kevin"
    print(is_palindrome('Kevin'))  # Kết quả sẽ là False
