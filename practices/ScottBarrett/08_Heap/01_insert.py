class MaxHeap:
    def __init__(self):
        # Khởi tạo heap rỗng (dùng list để lưu các phần tử)
        self.heap = []

    def _left_child(self, index):
        # Trả về chỉ số con trái của node tại index
        return 2 * index + 1

    def _right_child(self, index):
        # Trả về chỉ số con phải của node tại index
        return 2 * index + 2

    def _parent(self, index):
        # Trả về chỉ số node cha của node tại index
        return (index - 1) // 2

    def _swap(self, index1, index2):
        # Hoán đổi vị trí hai phần tử trong heap
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        # BƯỚC 1: Thêm giá trị mới vào cuối heap
        self.heap.append(value)
        
        # Lưu chỉ số của phần tử vừa thêm
        current = len(self.heap) - 1
        
        # BƯỚC 2: Bubble Up
        # Lặp cho đến khi phần tử không còn là root
        while current > 0:
            # Lấy chỉ số node cha
            parent_index = self._parent(current)
            
            # Nếu giá trị hiện tại lớn hơn giá trị của cha
            if self.heap[current] > self.heap[parent_index]:
                # Hoán đổi vị trí với node cha
                self._swap(current, parent_index)
                
                # Cập nhật vị trí hiện tại lên node cha
                current = parent_index
            else:
                # Nếu không vi phạm tính chất Max Heap → dừng
                break

if __name__ == '__main__':
        
    myheap = MaxHeap()
    myheap.insert(99)
    myheap.insert(72)
    myheap.insert(61)
    myheap.insert(58)

    print(myheap.heap)  


    myheap.insert(100)

    print(myheap.heap)  


    myheap.insert(75)

    print(myheap.heap)


    """
        EXPECTED OUTPUT:
        ----------------
        [99, 72, 61, 58]
        [100, 99, 61, 58, 72]
        [100, 99, 75, 58, 72, 61]

    """
        