class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        s=0
        e=len(nums)-1

        if len(nums)==1 or len(nums)==0:
            return nums

        def partition(nums,s,e):
            mid = (s + e) // 2
            nums[s], nums[mid] = nums[mid], nums[s]
            pivot = nums[s]
            cnt=0
            for i in nums[s+1:e+1]:
                if i <= pivot:
                    cnt+=1

            index=s+cnt
            nums[index],nums[s]=nums[s],nums[index]
            
            i=s
            j=e

            while i<index and j>index:
                while i < index and nums[i] <= pivot:
                    i += 1

                while j > index and nums[j] > pivot:
                    j -= 1

                if i<index and j>index:
                    nums[i],nums[j]=nums[j],nums[i]
                    i+=1
                    j-=1


            return index



            

        def quicksort(nums,s,e):
            if s>=e:
                return
            
            p=partition(nums,s,e)
            quicksort(nums,s,p-1)
            quicksort(nums,p+1,e)
            

        quicksort(nums,s,e)
        return nums


        