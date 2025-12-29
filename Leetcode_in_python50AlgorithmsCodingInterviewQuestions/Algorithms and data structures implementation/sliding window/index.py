def max_sum_debug(arr, k):
    n = len(arr)

    if n < k:
        print("Mảng quá ngắn")
        return -1

    # Tính tổng cửa sổ đầu tiên
    current_sum = 0
    for i in range(k):
        current_sum += arr[i]

    max_sum = current_sum

    print("Cửa sổ đầu tiên:", arr[0:k])
    print("Tổng =", current_sum)
    print("-" * 40)

    # Trượt cửa sổ
    for i in range(k, n):
        so_moi = arr[i]
        so_cu = arr[i - k]

        print(f"Thêm số mới: {so_moi}")
        print(f"Bỏ số cũ : {so_cu}")

        current_sum = current_sum + so_moi - so_cu

        print("Cửa sổ hiện tại:", arr[i - k + 1 : i + 1])
        print("Tổng hiện tại =", current_sum)

        if current_sum > max_sum:
            max_sum = current_sum
            print("👉 Cập nhật max_sum =", max_sum)

        print("-" * 40)

    print("✅ Tổng lớn nhất =", max_sum)
    return max_sum



def max_sum_subarray(arr, k):
    n = len(arr)

    # Kiểm tra điều kiện hợp lệ
    if n < k:
        print("Không thể tính, mảng quá ngắn")
        return -1

    # Tính tổng của k phần tử đầu tiên
    current_sum = 0
    for i in range(k):
        current_sum += arr[i]

    # Gán tổng lớn nhất ban đầu
    max_sum = current_sum

    # Trượt cửa sổ qua mảng
    for i in range(k, n):
        # Cộng phần tử mới vào cửa sổ
        current_sum += arr[i]

        # Trừ phần tử cũ bị bỏ ra khỏi cửa sổ
        current_sum -= arr[i - k]

        # Cập nhật tổng lớn nhất
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum


def maxSum(arr, windowSize):
    arraySize = len(arr)
    # n must be greater than k
    if arraySize <= windowSize:
        print("Invalid operation")
        return -1

    # Compute sum of first window of size k
    window_sum = sum([arr[i] for i in range(windowSize)])
    max_sum = window_sum
    # Compute sums of remaining windows by
    # removing first element of previous
    # window and adding last element of
    # current window.
    for i in range(arraySize-windowSize):
        window_sum = window_sum - arr[i] + arr[i + windowSize]
        max_sum = max(window_sum, max_sum)

    return max_sum


arr = [1, 2, 100, -1, 5]
# maximum sum should be 104 => 100 + -1 + 5
# answer = maxSum(arr, 3)
# answer = max_sum_subarray(arr, 3)
answer = max_sum_debug(arr, 3)
print(answer)
