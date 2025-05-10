class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        isprime = [True] * n

        for i in range(2, int(n ** 0.5) + 1):
            if isprime[i]:
                for j in range(i * i, n, i):
                    isprime[j] = False

        count = 0
        for i in range(2, n):
            if isprime[i]:
                count += 1
        return count

n=10
print(Solution().countPrimes(n))