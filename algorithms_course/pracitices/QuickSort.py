"""
QuickSort là thuật toán sắp xếp theo chia để trị (divide and conquer):
    Chọn một pivot (trung tâm, đầu, cuối…)
    Chia mảng thành:
        Các phần tử nhỏ hơn hoặc bằng pivot bên trái
        Các phần tử lớn hơn pivot bên phải
        Đệ quy sắp xếp mảng bên trái và mảng bên phải
        Nối kết quả → mảng đã sắp xếp

        ---------------------------------------------
                        [1, -4, 0, 10, 5, 4, 3, 100]
                                pivot=5
                    /                         \
        [1, -4, 0, 4, 3]                     [10, 100]
        pivot=0                              pivot=100
        /       \                             /      \
    [-4]       [1,3,4]                     [10]      []
            pivot=3
            /     \
            [1]     [4]

"""

class QuickSort:
    def __init__(self, data):
        self.data = data

    # Hàm gọi Quicksort
    def sort(self):
        self.quick_sort(0, len(self.data) - 1)
    
    # Hàm QuickSort đệ quy
    def quick_sort(self, low, high):
        # Nếu mảng chỉ có 1 hoặc 0 phần tử -> dừng.
        if low >= high:
            return
        
        # Chia mảng và lấy chỉ số pivot
        pivot_index = self.partition(low, high)
        print("pivot_index: ", pivot_index)
        # Đệ quy sắp xếp mảng bên trái pivot
        self.quick_sort(low, pivot_index - 1)
        
        # Đệ quy sắp xếp mảng bên phải pivot
        self.quick_sort(pivot_index + 1, high)
    
    # Hàm partition: đặt pivot vào vị trí đúng và chia mảng
    def partition(self, low, high):
        
        # Chọn pivot là phần tử ở giữa
        pivot_index = (low + high) // 2
        self.data[pivot_index], self.data[high] = self.data[high], self.data[pivot_index]

        # Lặp qua các phần tử từ low -> high-1
        for j in range(low, high):
            # Nếu phần tử <= pivot
            if self.data[j] <= self.data[high]:
                # Đổi vị trí với phần tử ở low
                self.data[low], self.data[j] = self.data[j], self.data[low]
                low += 1 # Tăng con trỏ low.
        
        # Đặt pivot vào vị trí đúng.
        self.data[low], self.data[high] = self.data[high], self.data[low]
        # Trả về số pivot
        return low

# Áp dụng sắp xếp mảng các dict theo giá:
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Monitor", "price": 300},
    {"name": "Keyboard", "price": 50},
    {"name": "USB Drive", "price": 15}
]

def quicksort_products(arr, low, high):
    if low >= high:
        return

    pivot_index = (low + high) // 2
    pivot = arr[pivot_index]["price"]
    
    # đổi pivot về cuối
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    i = low
    for j in range(low, high):
        if arr[j]["price"] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]

    quicksort_products(arr, low, i-1)
    quicksort_products(arr, i+1, high)


if __name__ == '__main__':

    x = [1, -4, 0, 10, 5, 4, 3, 100]

    algorithm = QuickSort(x)
    algorithm.sort()
    print(x)

    quicksort_products(products, 0, len(products)-1)

    for p in products:
        print(p)
