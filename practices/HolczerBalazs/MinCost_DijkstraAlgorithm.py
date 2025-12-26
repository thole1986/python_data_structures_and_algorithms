import heapq  # Thư viện heap để dùng priority queue (lấy node min_cost nhanh)

# Lớp Edge biểu diễn 1 cạnh (từ node hiện tại tới node khác)
class Edge:
    def __init__(self, weight, target):
        self.weight = weight  # Chi phí/ khoảng cách đi qua cạnh này
        self.target = target  # Node mà cạnh này đi tới


# Lớp Node biểu diễn 1 điểm/địa điểm
class Node:
    def __init__(self, name):
        self.name = name      # Tên node (A, B, Kho…)
        self.edges = []       # Danh sách các cạnh kề (Edge)
        self.min_cost = float('inf')  # Chi phí nhỏ nhất từ điểm start tới node này
        self.prev = None      # Node trước đó trong đường đi ngắn nhất

    # Cho heapq biết cách so sánh 2 Node
    def __lt__(self, other):
        return self.min_cost < other.min_cost

def apply_dijkstra(start: Node):
    start.min_cost = 0
    heap = [start]

    while heap:
        current = heapq.heappop(heap) # lấy node có chi phí nhỏ nhất.

        # Duyệt tất cả các cạnh kề của node này
        for edge in current.edges:
            # Chi phí mới nếu đi qua current
            new_cost = current.min_cost + edge.weight

            # Nếu chi phí này nhỏ hơn chi phí đã lưu cho node đích
            if new_cost < edge.target.min_cost:
                edge.target.min_cost = new_cost # Cập nhật chi phí nhỏ nhất
                edge.target.prev = current   # Ghi lại node trước đó
                heapq.heappush(heap, edge.target) # Đưa node vào heap để xét tiếp

# Hàm in đường đi ngắn nhất từ start tới node cuối
def print_path(node):
    path = []
    while node:            # Truy ngược từ node cuối về start
        path.append(node.name)
        node = node.prev
    print(" → ".join(reversed(path)))  # In theo thứ tự start → end


if __name__ == '__main__':
    # Tạo các node (địa điểm)
    K = Node("Kho")
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")

    # Tạo các cạnh và chi phí
    K.edges = [Edge(2, A), Edge(5, B)]   # Kho → A = 2, Kho → B = 5
    A.edges = [Edge(1, B), Edge(4, C)]   # A → B = 1, A → C = 4
    B.edges = [Edge(2, C), Edge(6, D)]   # B → C = 2, B → D = 6
    C.edges = [Edge(1, D)]               # C → D = 1

    # Chạy thuật toán Dijkstra từ kho
    apply_dijkstra(K)

    # In chi phí và đường đi tới từng node
    for node in [A, B, C, D]:
        print(f"Chi phí từ Kho → {node.name} = {node.min_cost}")
        print("Đường đi:", end=" ")
        print_path(node)
        print("-" * 30)

    """
    Kho → A trực tiếp rẻ nhất = 2
    Kho → B đi qua A = 3 (rẻ hơn 5 trực tiếp)
    Kho → C đi qua A → B = 5
    Kho → D đi qua A → B → C = 6
    """
