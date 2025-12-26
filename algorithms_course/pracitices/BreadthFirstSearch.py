
class Node:
    def __init__(self, name):
        self.name = name
        self.adjacency_list = [] # danh sách các nút kề (neighbors)
        self.visited = False # Đánh dấu đã duyệt hay chưa.


# Hàm BFS: duyệt đồ thị theo chiều rộng.
def breadth_first_search(start_node):
    # Hàng đợi FIFO
    # Nút đầu tiên được thêm vào sẽ là nút đầu tiên lấy ra
    queue = [start_node]

    # Lặp cho đến khi hàng đợi trống
    while queue:
        # Lấy và xoá nút đầu tiên trong hàng đợi
        actual_node: Node = queue.pop(0)
        actual_node.visited = True # đánh dấu đã duyệt
        print(actual_node.name)  # in tên Node

        # Duyệt các nút kề của nút hiện tại.
        for node in actual_node.adjacency_list:
            if not node.visited:  # nếu chưa duyệt/gặp
                queue.append(node) # thêm vào hàng đợi



if __name__ == '__main__':

    # Tạo các nút
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    # Thiết lập các cạnh (neighbors)
    node1.adjacency_list.append(node2)  # A -> B
    node1.adjacency_list.append(node3)  # A -> C
    node2.adjacency_list.append(node4)  # B -> D
    node4.adjacency_list.append(node5)  # D -> E

    # Chạy BFS từ nút A
    breadth_first_search(node1)
