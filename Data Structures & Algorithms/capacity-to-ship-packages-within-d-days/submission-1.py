class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l = max(weights)
        h = sum(weights)

        ans = h

        while l <= h:

            mid = (l + h) // 2

            left = 0
            d = 0

            while left < len(weights):

                w = weights[left]
                right = left + 1

                while right < len(weights) and w + weights[right] <= mid:
                    w += weights[right]
                    right += 1

                d += 1
                left = right

            if d <= days:
                ans = mid
                h = mid - 1
            else:
                l = mid + 1

        return ans