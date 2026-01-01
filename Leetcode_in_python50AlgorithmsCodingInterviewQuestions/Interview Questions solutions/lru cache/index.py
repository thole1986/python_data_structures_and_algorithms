from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.m = dict()
        self.deq = deque()

    def get(self, key: int) -> int:
        if key in self.m:
            value = self.m[key]
            self.deq.remove(key)
            self.deq.append(key)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)
        if key not in self.m:
            if len(self.deq) == self.c:
                oldest = self.deq.popleft()
                del self.m[oldest]
        else:
            self.deq.remove(key)

        self.m[key] = value
        self.deq.append(key)


from collections import deque

# Tạo class LRUCache
class LRUCache:
    def __init__(self, capacity: int):
        """
        Khởi tạo cache với dung lượng cố định.
        self.c: dung lượng tối đa
        self.m: dict để lưu key → value
        self.deq: deque để lưu thứ tự sử dụng (cũ nhất ở đầu, mới nhất ở cuối)
        """
        self.c = capacity
        self.m = dict()
        self.deq = deque()

    def get(self, key: int) -> int:
        """
        Lấy giá trị của key từ cache.
        Nếu key tồn tại:
            - Lấy value
            - Đánh dấu key là vừa dùng → đưa lên cuối deque
        Nếu key không tồn tại:
            - Trả về -1
        """
        if key in self.m:              # kiểm tra key có trong cache không
            value = self.m[key]        # lấy giá trị
            self.deq.remove(key)       # xóa key khỏi vị trí cũ trong deque
            self.deq.append(key)       # đưa key lên cuối → mới dùng nhất
            return value               # trả giá trị
        else:
            return -1                  # key không tồn tại

    def put(self, key: int, value: int) -> None:
        """
        Thêm hoặc cập nhật key-value vào cache.
        Nếu key đã tồn tại:
            - Cập nhật value
            - Đánh dấu key vừa dùng
        Nếu key chưa tồn tại:
            - Nếu cache đầy: loại bỏ key cũ nhất
            - Thêm key mới vào
        """
        if key not in self.m:                   # key mới
            if len(self.deq) == self.c:        # cache đầy
                oldest = self.deq.popleft()    # lấy key cũ nhất
                del self.m[oldest]             # xóa khỏi dict
        else:
            self.deq.remove(key)               # key đã tồn tại → xóa khỏi vị trí cũ

        self.m[key] = value                     # thêm hoặc cập nhật value
        self.deq.append(key)                     # đưa key lên cuối → mới dùng nhất

# ---------------------------
# Ví dụ chạy thử từng bước
# ---------------------------

cache = LRUCache(2)  # tạo cache dung lượng = 2

print("Put (1, 'A')")
cache.put(1, 'A')      # cache = [1]
print("Cache dict:", cache.m)
print("Cache deque:", list(cache.deq))
print()

print("Put (2, 'B')")
cache.put(2, 'B')      # cache = [1, 2]
print("Cache dict:", cache.m)
print("Cache deque:", list(cache.deq))
print()

print("Get 1")
print("Result:", cache.get(1))  # trả về 'A', cache = [2, 1]
print("Cache dict:", cache.m)
print("Cache deque:", list(cache.deq))
print()

print("Put (3, 'C')")
cache.put(3, 'C')      # cache đầy, bỏ 2 → cache = [1, 3]
print("Cache dict:", cache.m)
print("Cache deque:", list(cache.deq))
print()

print("Get 2")
print("Result:", cache.get(2))  # 2 đã bị loại, trả về -1
print("Cache dict:", cache.m)
print("Cache deque:", list(cache.deq))
print()

print("Get 3")
print("Result:", cache.get(3))  # trả về 'C', cache = [1, 3] (3 mới dùng nhất)
print("Cache dict:", cache.m)
print("Cache deque:", list(cache.deq))
