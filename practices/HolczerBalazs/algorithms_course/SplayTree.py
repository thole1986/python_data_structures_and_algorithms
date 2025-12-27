"""
Brute Force Algorithms
"""

def naive_search(pattern, text):
    # Độ dài của chuỗi text
    n = len(text)
    # Độ dài của chuỗi pattern
    m = len(pattern)

    # Duyệt từng vị trí có thể bắt đầu của pattern trong text
    for i in range(n - m + 1):
        j = 0  # chỉ số để duyệt pattern

        # So sánh từng ký tự của pattern với text
        while j < m:
            # Nếu có ký tự không khớp thì dừng
            print("text[i + j]", text[i + j])
            print("pattern[j]", pattern[j])
            if text[i + j] != pattern[j]:
                break
            j += 1

        # Nếu đã so khớp hết pattern
        if j == m:
            print('Found a match at index %s' % i)

if __name__ == '__main__':
    naive_search('abcd', 'abcdeefabcabcd')
