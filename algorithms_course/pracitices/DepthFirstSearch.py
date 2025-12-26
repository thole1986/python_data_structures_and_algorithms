
"""
    Depth-First Search (Duyệt theo chiều sâu):
    - Bắt đầu từ 1 nút gốc.
    - Duyệt sâu xuống một nhánh trước khi quay lại nhánh khác.
    - Dùng stack (LIFO: Last In First Out) để nhớ các nút cần duyệt tiếp.
"""

# Lớp Node đại diện cho một nút trong đồ thị
class Node:
    def __init__(self, name):
        self.name = name # tên node
        self.adjacency_list = [] # Danh sách các nút kề
        self.visited = False # Đánh dấu đã duyệt hay chưa


# Hàm DFS dùng STACK
def depth_first_search(start_node):

    # Stack LIFO: nút thêm vào cuối sẽ được lấy trước
    stack = [start_node]
    
    # Lặp cho đến khi stack trống.
    while stack:
        # Lấy nút cuối cùng trong stack và xoá nó.
        actual_node = stack.pop()
        print(actual_node.name)

        # Duyệt các nút kề
        for node in actual_node.adjacency_list:
            # nếu chưa duyệt
            if not node.visited:
                actual_node.visited = True # Đánh dấu đã duyệt
                # Thêm vào stack để duyệt sau
                stack.append(node)

if __name__ == '__main__':

    # Tạo các nút
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    # Thiết lập các cạnh
    node1.adjacency_list.append(node2)  # A -> B
    node1.adjacency_list.append(node3)  # A -> C
    node2.adjacency_list.append(node4)  # B -> D
    node4.adjacency_list.append(node5)  # D -> E

    # Chạy DFS từ nút A
    depth_first_search(node1)
