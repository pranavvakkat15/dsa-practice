class Solution:
    def reverseNumber(self, n: int) -> int:
        reverseNumber = 0
        while n > 0:
            ld = n % 10
            reverseNumber = (reverseNumber * 10) + ld
            n = n // 10
        return reverseNumber
