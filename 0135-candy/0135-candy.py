class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        # Step 1: Give every child at least 1 candy
        candies = [1] * n
        
        # Step 2: Left-to-right pass
        # Ensure children with higher rating than the left neighbor get more candies
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Step 3: Right-to-left pass
        # Ensure children with higher rating than the right neighbor get more candies
        # We use max() to keep the higher value from previous pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        # Step 4: Return total sum
        return sum(candies)
