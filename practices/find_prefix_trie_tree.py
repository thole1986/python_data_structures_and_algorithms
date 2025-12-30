# =========================
# ĐỊNH NGHĨA NODE CỦA TRIE
# =========================
class TrieNode:
    def __init__(self):
        # children là dictionary:
        # key   = ký tự (a, b, c, ...)
        # value = TrieNode con tương ứng
        self.children = {}

        # is_end = True nếu node này là ký tự cuối của 1 từ
        self.is_end = False


# =========================
# ĐỊNH NGHĨA TRIE
# =========================
class Trie:
    def __init__(self):
        # root là node gốc, không chứa ký tự nào
        self.root = TrieNode()

    # =========================
    # THÊM 1 TỪ VÀO TRIE
    # =========================
    def insert(self, word):
        # Bắt đầu từ node gốc
        current = self.root

        # Duyệt từng ký tự trong từ
        for char in word:

            # Nếu ký tự chưa tồn tại trong children
            # thì tạo node mới
            if char not in current.children:
                current.children[char] = TrieNode()

            # Di chuyển xuống node con tương ứng
            current = current.children[char]

        # Sau khi thêm hết ký tự
        # đánh dấu đây là kết thúc của 1 từ
        current.is_end = True

    # =========================
    # TÌM TẤT CẢ TỪ BẮT ĐẦU BẰNG PREFIX
    # =========================
    def starts_with(self, prefix):
        current = self.root

        # Đi theo từng ký tự của prefix
        for char in prefix:

            # Nếu không có ký tự này → không có từ nào phù hợp
            if char not in current.children:
                return []

            # Di chuyển xuống node con
            current = current.children[char]

        # Sau khi đi hết prefix
        # ta đang đứng ở node cuối của prefix
        results = []

        # Dùng DFS để lấy tất cả từ bên dưới
        self._dfs(current, prefix, results)

        return results

    # =========================
    # DFS: duyệt toàn bộ nhánh bên dưới
    # =========================
    def _dfs(self, node, path, results):

        # Nếu node này là kết thúc 1 từ
        if node.is_end:
            results.append(path)

        # Duyệt tất cả node con
        for char, next_node in node.children.items():
            self._dfs(next_node, path + char, results)


if __name__ == '__main__':
    trie = Trie()

    words = ["adam", "ana", "anna", "bob", "brian", "carol"]

    for word in words:
        trie.insert(word)

    print(trie.starts_with("a"))
    print(trie.starts_with("b"))
