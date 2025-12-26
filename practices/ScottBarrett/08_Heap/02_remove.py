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

    def _sink_down(self, index):
        """
        Tại mỗi bước:
            So sánh node hiện tại với con trái
            So sánh node lớn nhất hiện tại với con phải
            Chọn ra node lớn nhất trong 3 node
            Nếu node lớn nhất không phải node hiện tại → swap
            Tiếp tục kiểm tra ở vị trí mới
        """
        # Lưu lại chỉ số của node có giá trị lớn nhất
        max_index = index

        # Lặp vô hạn cho đến khi không còn vi phạm Max Heap
        while True:
            # Lấy chỉ số con trái
            left_index = self._left_child(index)
            
            # Lấy chỉ số con phải
            right_index = self._right_child(index)

            # Nếu con trái tồn tại và lớn hơn node hiện tại
            if (left_index < len(self.heap) and 
                    self.heap[left_index] > self.heap[max_index]):
                
                # Cập nhật node lớn nhất là con trái
                max_index = left_index

            # Nếu con phải tồn tại và lớn hơn node lớn nhất hiện tại
            if (right_index < len(self.heap) and 
                    self.heap[right_index] > self.heap[max_index]):
                # Cập nhật node lớn nhất là con phải
                max_index = right_index

            # Nếu node lớn nhất không phải node hiện tại
            if max_index != index:
                # Hoán đổi node hiện tại với node lớn nhất
                self._swap(index, max_index)
                
                # Cập nhật vị trí mới để tiếp tục sink down
                index = max_index
            else:
                # Nếu không cần hoán đổi nữa → heap đã hợp lệ
                return

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

    def remove(self):
        # Heap rỗng
        if len(self.heap) == 0:
            return None
        # Heap chỉ có 1 pahần tử
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # Lưu lại giá trị lớn nhất.
        max_value = self.heap[0]
        # Đưa phần tử cuối lên root
        self.heap[0] = self.heap.pop()
        # Sink down để khôi phục max heap
        self._sink_down(0)
        return max_value
    

if __name__ == '__main__':
    myheap = MaxHeap()
    myheap.insert(95)
    myheap.insert(75)
    myheap.insert(80)
    myheap.insert(55)
    myheap.insert(60)
    myheap.insert(50)
    myheap.insert(65)

    print(myheap.heap)

    myheap.remove()
    print(myheap.heap)

    myheap.remove()
    print(myheap.heap)


    """
        EXPECTED OUTPUT:
        ----------------
        [95, 75, 80, 55, 60, 50, 65]
        [80, 75, 65, 55, 60, 50]
        [75, 60, 65, 55, 50]
    """
        