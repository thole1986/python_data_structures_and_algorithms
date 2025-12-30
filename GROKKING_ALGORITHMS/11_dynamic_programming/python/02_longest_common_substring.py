blue = ["b", "l", "u", "e"]
clues = ["c", "l", "u", "e", "s"]

# tạo bảng (len(clues)+1) x (len(blue)+1)
dp = [[0 for _ in range(len(blue) + 1)]
      for _ in range(len(clues) + 1)]

max_len = 0

for i in range(1, len(clues) + 1):
    for j in range(1, len(blue) + 1):
        if clues[i-1] == blue[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            max_len = max(max_len, dp[i][j])
        else:
            dp[i][j] = 0

for row in dp:
    print(row)

print("Longest Common Substring length:", max_len)
