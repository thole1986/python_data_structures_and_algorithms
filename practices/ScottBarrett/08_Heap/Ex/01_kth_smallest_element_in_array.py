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


def find_kth_smallest(nums, k):
    # Tạo một Max Heap (tưởng tượng như một chuồng gà,
    # trong đó con gà mập nhất luôn đứng ở cửa)
    max_heap = MaxHeap()

    # Duyệt từng số trong danh sách nums
    for num in nums:
        # Thêm số hiện tại vào Max Heap
        # (cho một con gà mới vào chuồng)
        max_heap.insert(num)

        # Nếu số lượng phần tử trong heap vượt quá k
        # nghĩa là chuồng gà có quá nhiều hơn k con
        if len(max_heap.heap) > k:
            # Loại bỏ phần tử lớn nhất trong heap
            # (đuổi con gà mập nhất ra khỏi chuồng)
            max_heap.remove()

    # Sau khi duyệt xong tất cả các phần tử:
    # Max Heap chỉ còn lại k số nhỏ nhất
    # Phần tử lớn nhất trong heap (heap[0])
    # chính là số nhỏ thứ k cần tìm
    return max_heap.heap[0]



if __name__ == '__main__':
    # Test cases
    nums = [[3,2,1,5,6,4], [6,5,4,3,2,1], [1,2,3,4,5,6], [3,2,3,1,2,4,5,5,6]]
    ks = [2, 3, 4, 7]
    expected_outputs = [2, 3, 4, 5]

    for i in range(len(nums)):
        print(f'Test case {i+1}...')
        print(f'Input: {nums[i]} with k = {ks[i]}')
        result = find_kth_smallest(nums[i], ks[i])
        print(f'Output: {result}')
        print(f'Expected output: {expected_outputs[i]}')
        print(f'Test passed: {result == expected_outputs[i]}')
        print('---------------------------------------')

    """
        EXPECTED OUTPUT:
        ----------------
        Test case 1...
        Input: [3, 2, 1, 5, 6, 4] with k = 2
        Output: 2
        Expected output: 2
        Test passed: True
        ---------------------------------------
        Test case 2...
        Input: [6, 5, 4, 3, 2, 1] with k = 3
        Output: 3
        Expected output: 3
        Test passed: True
        ---------------------------------------
        Test case 3...
        Input: [1, 2, 3, 4, 5, 6] with k = 4
        Output: 4
        Expected output: 4
        Test passed: True
        ---------------------------------------
        Test case 4...
        Input: [3, 2, 3, 1, 2, 4, 5, 5, 6] with k = 7
        Output: 5
        Expected output: 5
        Test passed: True
        ---------------------------------------

    """
