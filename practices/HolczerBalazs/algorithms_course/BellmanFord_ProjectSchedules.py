"""
    1️⃣ Ý tưởng

    Mỗi công việc là một đỉnh (Node).
    Thời gian thực hiện công việc là trọng số cạnh (Edge) từ công việc trước → công việc sau.
    Nếu một mối quan hệ thời gian bị mâu thuẫn (ví dụ phải hoàn thành trước nhưng bị trễ), có thể biểu diễn bằng trọng số âm.

    Bellman-Ford giúp:
    Tìm thời gian sớm nhất hoàn thành từng công việc.
    Phát hiện mâu thuẫn lịch trình (negative cycle).

    2️⃣ Ví dụ

    Giả sử dự án có các công việc:
    A → B → C
    A → D
    B → D
    C → E
    D → E

    Với thời gian thực hiện (cạnh = thời gian cần cho công việc sau khi hoàn thành công việc trước):

    Từ	Đến	Thời gian
    A	B	3
    A	D	2
    B	C	4
    B	D	1
    C	E	2
    D	E	3
    E	B	-10 (mâu thuẫn, tạo chu trình âm)

    Trọng số âm mô phỏng mâu thuẫn lịch trình, ví dụ “E phải hoàn thành trước B” nhưng không thể.
"""

class Task:
    def __init__(self, name):
        self.name = name
        self.min_time = float('inf')
        self.predecessor = None

class Dependency:
    def __init__(self, start_task, end_task, duration):
        self.start_task = start_task
        self.end_task = end_task
        self.duration = duration

class ProjectSchedule:
    def __init__(self, tasks, dependencies, start_task):
        self.tasks = tasks
        self.dependencies = dependencies
        self.start_task = start_task
        self.has_conflict = False

    def find_earliest_times(self):
        self.start_task.min_time = 0

        # Bellman-Ford: V-1 iterations
        for _ in range(len(self.tasks)-1):
            for dep in self.dependencies:
                u = dep.start_task
                v = dep.end_task
                time = u.min_time + dep.duration
                if time < v.min_time:
                    v.min_time = time
                    v.predecessor = u

        # Check negative cycle (mâu thuẫn lịch trình)
        for dep in self.dependencies:
            if dep.start_task.min_time + dep.duration < dep.end_task.min_time:
                print("⚠️ Mâu thuẫn lịch trình (negative cycle) phát hiện!")
                self.has_conflict = True
                return

    def print_schedule(self):
        if self.has_conflict:
            print("Dự án không khả thi do mâu thuẫn lịch trình.")
            return
        print("Thời gian sớm nhất hoàn thành từng công việc:")
        for task in self.tasks:
            print(f"  {task.name}: {task.min_time}")

        # Truy ngược đường đi từ task cuối cùng
        print("\nĐường đi tối ưu:")
        for task in self.tasks:
            path = []
            t = task
            while t is not None:
                path.append(t.name)
                t = t.predecessor
            path.reverse()
            print(f"{task.name}: {' → '.join(path)}")

# Khởi tạo công việc
A = Task("A")
B = Task("B")
C = Task("C")
D = Task("D")
E = Task("E")

tasks = [A, B, C, D, E]

# Khởi tạo phụ thuộc
dependencies = [
    Dependency(A, B, 3),
    Dependency(A, D, 2),
    Dependency(B, C, 4),
    Dependency(B, D, 1),
    Dependency(C, E, 2),
    Dependency(D, E, 3),
    # Dependency(E, B, -10)  # Mâu thuẫn
]

# Chạy thuật toán
project = ProjectSchedule(tasks, dependencies, A)
project.find_earliest_times()
project.print_schedule()
