from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Nếu không cần đổi tiền
        if amount == 0:
            return 0
        
        # Giá trị "vô cực" (coi như không đổi được)
        INF = amount + 1
        
        # dp[i] = số đồng xu ít nhất để đổi được số tiền i
        dp = [INF] * (amount + 1)
        
        # Đổi 0 tiền cần 0 đồng xu
        dp[0] = 0
        
        # Duyệt qua từng số tiền từ 1 → amount
        for money in range(1, amount + 1):
            # Thử từng đồng xu
            for coin in coins:
                # Nếu dùng được đồng xu này
                if coin <= money:
                    dp[money] = min(
                        dp[money],           # không dùng coin này
                        dp[money - coin] + 1 # dùng coin này
                    )
        
        # Nếu không đổi được thì trả -1
        return dp[amount] if dp[amount] != INF else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount <= 0:
            return 0
        
        if min(coins) > amount:
            return -1

        INT_MAX = 1<<32
        dp = [INT_MAX] * (amount +1)
        
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min((dp[i-coin] + 1), dp[i])
                    
        return dp[amount] if dp[amount] != INT_MAX else -1
