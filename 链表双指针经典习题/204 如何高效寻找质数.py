# 常规思路 通过枚举对因数进行判断
def countPrimes(n):
    count = 0
    for i in range(2, n):
        if isPrime(i):
            count += 1
    return count

# 判断整数 n 是否是素数
def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            # 有其他整除因子
            return False
    return True
# 上述思路遇到数字较大的情况时间容易超时

# print(countPrimes(1000))

# 素数筛选法
class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * n
        for i in range(2, int(n**0.5)+1):
            if isPrime[i]:
                for j in range(i * i,n, i):
                    isPrime[j] = False

        count = 0
        for i in range(2, n):
            if isPrime[i]:
                count += 1

        return count
solution = Solution()
print(solution.countPrimes(10))