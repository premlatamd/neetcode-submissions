class Solution:
    def reverseBits(self, n: int) -> int:
        m=bin(n)[2:]
        m=m.zfill(32)
        m=m[::-1]
        ans=int(m,2)
        return ans