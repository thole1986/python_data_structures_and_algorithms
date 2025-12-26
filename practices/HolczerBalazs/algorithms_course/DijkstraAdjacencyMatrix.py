import sys
"""
    1️⃣ Sơ đồ đồ thị

    Ma trận kề:
    m = [
        [0, 7, 5, 2, 0, 0],  # 0
        [7, 0, 0, 0, 3, 8],  # 1
        [5, 0, 0, 10, 4, 0], # 2
        [2, 0, 10, 0, 0, 2], # 3
        [0, 3, 4, 0, 0, 6],  # 4
        [0, 8, 0, 2, 6, 0]   # 5
    ]
    Các đỉnh: 0, 1, 2, 3, 4, 5
    Số liệu là trọng số cạnh giữa 2 đỉnh.

    Nếu 0 → không có cạnh.

    2️⃣ Các cạnh với trọng số

    0 ↔ 1 : 7

    0 ↔ 2 : 5

    0 ↔ 3 : 2

    1 ↔ 4 : 3

    1 ↔ 5 : 8

    2 ↔ 3 : 10

    2 ↔ 4 : 4

    3 ↔ 5 : 2

    4 ↔ 5 : 6

    3️⃣ Đường đi ngắn nhất từ đỉnh 1 (theo Dijkstra)

    Bắt đầu từ 1, cập nhật khoảng cách theo vòng lặp:

    Đỉnh	Khoảng cách từ 1	Đường đi ngắn nhất
    0	10	1 → 4 → 2 → 0
    1	0	1
    2	7	1 → 4 → 2
    3	7	1 → 5 → 3
    4	3	1 → 4
    5	8	1 → 5

    Lưu ý: có nhiều đường có cùng trọng số tối thiểu, ví dụ từ 1→0 có thể qua 4→2→0 hoặc 1→5→3→0, nhưng Dijkstra chọn đường được cập nhật trước.

    4️⃣ Sơ đồ minh họa
            (7)
    0 ---------- 1
    | \         / \
    (5)|  \(10)/    \(8)
    |    2         5
    |   / \       /
    (2) /   \     / (2)
        3 ----- 4
            (6)


    Các số trong ngoặc là trọng số cạnh.

    Mũi tên đi từ đỉnh 1 (start) đến các đỉnh cho thấy đường đi ngắn nhất:

    1 → 4 → 2 → 0
    1 → 4 → 2
    1 → 5 → 3
    1 → 4
    1 → 5
"""

class DijkstraAlgorithm:
    def __init__(self, adjacency_matrix, start_vertex):
        self.adjacency_matrix = adjacency_matrix
        self.start_vertex = start_vertex
        self.v = len(adjacency_matrix)
        # Đánh dấu đã xét hay chưa
        self.visited = [False] * self.v

        # Khoảng cách ngắn nhất từ start tới các đỉnh
        self.distances = [float('inf')] * self.v
        self.distances[start_vertex] = 0

        print("=== KHỞI TẠO ===")
        print("Start vertex:", start_vertex)
        print("Visited  :", self.visited)
        print("Distances:", self.distances)
        print()

    def get_min_vertex(self):
        min_value = sys.maxsize
        min_index = -1

        print(">> Tìm đỉnh chưa xét có distance nhỏ nhất")
        for i in range(self.v):
            print(f"   - Đỉnh {i}: visited={self.visited[i]}, distance={self.distances[i]}")
            if not self.visited[i] and self.distances[i] < min_value:
                min_value = self.distances[i]
                min_index = i

        print(f"   => Chọn đỉnh {min_index} (distance={min_value})\n")
        return min_index

    def calculate(self):
        for step in range(self.v):
            print(f"========== VÒNG LẶP {step + 1} ==========")

            current = self.get_min_vertex()

            print(f"Đánh dấu đỉnh {current} là đã xét")
            self.visited[current] = True
            print("Visited:", self.visited)

            print(f"Xét các đỉnh kề với đỉnh {current}")

            for neighbor in range(self.v):
                weight = self.adjacency_matrix[current][neighbor]
                if weight > 0:
                    print(f"  - Có cạnh {current} → {neighbor} (trọng số {weight})")
                    new_distance = self.distances[current] + weight
                    print(f"    Tính: {self.distances[current]} + {weight} = {new_distance}")
                    if new_distance < self.distances[neighbor]:
                        print(f"    ✔ Cập nhật distance[{neighbor}] = {new_distance}")
                        self.distances[neighbor] = new_distance
                    else:
                        print(f"    ✖ Không cập nhật (đã có {self.distances[neighbor]})")

            print("Distances hiện tại:", self.distances)
            print()

    def print_distances(self):
        print("=== KẾT QUẢ CUỐI CÙNG ===")
        for i in range(self.v):
            print(f"Từ {self.start_vertex} → {i} = {self.distances[i]}")


if __name__ == "__main__":
    m = [
        [0, 7, 5, 2, 0, 0],  # đỉnh 0
        [7, 0, 0, 0, 3, 8],  # đỉnh 1 ← start_vertex
        [5, 0, 0, 10, 4, 0], # đỉnh 2
        [2, 0, 10, 0, 0, 2], # đỉnh 3
        [0, 3, 4, 0, 0, 6],  # đỉnh 4
        [0, 8, 0, 2, 6, 0]   # đỉnh 5
    ]   
    
    # start_vertex = 1 → Dijkstra sẽ tính từ đỉnh 1 tới 0, 2, 3, 4, 5.
    algorithm = DijkstraAlgorithm(m, 1)
    algorithm.calculate()
    algorithm.print_distances()
