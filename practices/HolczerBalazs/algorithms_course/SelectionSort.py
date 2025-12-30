
def selection_sort(nums):
    
    # Duyệt từng vị trí trong mảng (trừ phần tử cuối)
    for i in range(len(nums) - 1):
        # Giả sử phần tử nhỏ nhất nằm ở vị trí i
        min_index = i
        for j in range(i, len(nums)):
            # Nếu tìm được số nhỏ hơn số đang cho là nhỏ nhất
            if nums[j] < nums[min_index]:
                min_index = j   # Cập nhật vị trí nhỏ nhất
        
        # Sau khi kết thúc vòng lặp trong
        # index là vị trí của số nhỏ nhất trong đoạn chưa sắp xếp
        # Nếu số nhỏ nhất không nằm đúng vị trí i
        if min_index != i:
            # Đổi chỗ phần tử nhỏ nhất về đúng vị trí
            nums[i], nums[min_index] = nums[min_index], nums[i]

if __name__ == '__main__':
    # n = [5, 4, 3, 2, 1]
    n = [5, 4, 3]
    selection_sort(n)
    print(n)
