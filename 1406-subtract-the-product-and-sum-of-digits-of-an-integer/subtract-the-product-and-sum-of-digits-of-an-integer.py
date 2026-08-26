class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        total = 0
        product = 1

        while n > 0:
            digit = n % 10
            total += digit
            product *= digit
            n //= 10

        return product - total