def shell_sort(nums):
    
    # Bắt đầu với gap = chiều dài mảng // 2
    gap = len(nums) // 2

    # Lặp cho đến khi gap > 0
    while gap > 0:

        # Lặp như Insertion Sort nhưng so sánh các phần tử cách nhau 'gap'
        for i in range(gap, len(nums)):

            j = i
            # So sánh và hoán đổi các phần tử cách nhau gap nếu cần
            while j >= gap and nums[j - gap] > nums[j]:
                nums[j], nums[j - gap] = nums[j - gap], nums[j]
                j -= gap  # di chuyển về phía trước

        # Giảm gap
        gap = gap // 2


if __name__ == '__main__':
    x = [10, -4, 0, 3, 2, 1, 100, -8]
    shell_sort(x)
    print(x)
