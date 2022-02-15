def countOnes(n):
    numOnes = 0
    while n != 0:
        n &= n - 1
        numOnes += 1
    return numOnes
class Solution:
    def countBits(self, n: int) -> List[int]:
        answerArr = []
        for i in range(n+1):
            answerArr.append(countOnes(i))
        return answerArr