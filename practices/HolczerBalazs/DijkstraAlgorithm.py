import heapq

# Lớp Edge biểu diễn một cạnh trong đồ thị
class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight              # Trọng số của cạnh
        self.start_vertex = start_vertex  # Đỉnh bắt đầu
        self.target_vertex = target_vertex# Đỉnh kết thúc


# Lớp Node biểu diễn một đỉnh trong đồ thị
class Node:
    def __init__(self, name):
        self.name = name                  # Tên của node
        self.visited = False              # Đánh dấu đã thăm chưa
        self.predecessor = None           # Đỉnh trước đó
        self.adjacency_list = []          # Danh sách cạnh kề
        self.min_distance = float('inf')  # Khoảng cách ngắn nhất từ nguồn

    # Hàm so sánh để heapq hoạt động
    def __lt__(self, other):
        return self.min_distance < other.min_distance


# Lớp thực hiện thuật toán Dijkstra
class DijkstraAlgorithm:
    def __init__(self):
        self.heap = []  # Priority queue

    def calculate(self, start_vertex: Node):
        # Khoảng cách từ đỉnh bắt đầu đến chính nó = 0
        start_vertex.min_distance = 0

        # Đưa đỉnh bắt đầu vào heap
        heapq.heappush(self.heap, start_vertex)

        # Lặp cho đến khi heap rỗng
        while self.heap:
            # Lấy đỉnh có khoảng cách nhỏ nhất
            actual_vertex = heapq.heappop(self.heap)

            # Nếu đã thăm thì bỏ qua
            if actual_vertex.visited:
                continue

            # Đánh dấu đã thăm
            actual_vertex.visited = True

            # Duyệt các cạnh kề
            for edge in actual_vertex.adjacency_list:
                u = edge.start_vertex
                v = edge.target_vertex

                # Tính khoảng cách mới
                new_distance = u.min_distance + edge.weight

                # Nếu tìm được đường đi ngắn hơn
                if new_distance < v.min_distance:
                    v.min_distance = new_distance
                    v.predecessor = u
                    # Đưa v vào heap để tiếp tục xét
                    heapq.heappush(self.heap, v)

    # In đường đi ngắn nhất
    @staticmethod
    def get_shortest_path(vertex):
        print("Shortest distance:", vertex.min_distance)

        actual_vertex = vertex
        while actual_vertex:
            print(actual_vertex.name)
            actual_vertex = actual_vertex.predecessor

if __name__ == "__main__":

    # create the vertices (nodes)
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")
    node8 = Node("H")

    # create the edges (directed edges)
    edge1 = Edge(5, node1, node2)
    edge2 = Edge(8, node1, node8)
    edge3 = Edge(9, node1, node5)
    edge4 = Edge(15, node2, node4)
    edge5 = Edge(12, node2, node3)
    edge6 = Edge(4, node2, node8)
    edge7 = Edge(7, node8, node3)
    edge8 = Edge(6, node8, node6)
    edge9 = Edge(5, node5, node8)
    edge10 = Edge(4, node5, node6)
    edge11 = Edge(20, node5, node7)
    edge12 = Edge(1, node6, node3)
    edge13 = Edge(13, node6, node7)
    edge14 = Edge(3, node3, node4)
    edge15 = Edge(11, node3, node7)
    edge16 = Edge(9, node4, node7)

    # handle the neighbors
    node1.adjacency_list.append(edge1)
    node1.adjacency_list.append(edge2)
    node1.adjacency_list.append(edge3)
    node2.adjacency_list.append(edge4)
    node2.adjacency_list.append(edge5)
    node2.adjacency_list.append(edge6)
    node8.adjacency_list.append(edge7)
    node8.adjacency_list.append(edge8)
    node5.adjacency_list.append(edge9)
    node5.adjacency_list.append(edge10)
    node5.adjacency_list.append(edge11)
    node6.adjacency_list.append(edge12)
    node6.adjacency_list.append(edge13)
    node3.adjacency_list.append(edge14)
    node3.adjacency_list.append(edge15)
    node4.adjacency_list.append(edge16)

    # we just have to run the application
    algorithm = DijkstraAlgorithm()
    algorithm.calculate(node1)
    algorithm.get_shortest_path(node6)
