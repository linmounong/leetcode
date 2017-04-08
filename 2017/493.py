class Solution(object):

    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = [0]

        def merge(i, j, k):
            l1 = nums[i:j]
            l2 = nums[j:k]
            i1 = i2 = 0
            n1 = j - i
            n2 = k - j
            while i1 < n1 and i2 < n2:
                if l1[i1] > l2[i2]:
                    nums[i] = l1[i1]
                    i1 += 1
                else:
                    nums[i] = l2[i2]
                    i2 += 1
                i += 1
            if i1 < n1:
                nums[i:k] = l1[i1:n1]
            if i2 < n2:
                nums[i:k] = l2[i2:n2]

        def count(i, j, k):
            i1 = i
            i2 = j
            while i1 < j and i2 < k:
                if nums[i1] > nums[i2] * 2:
                    ret[0] += k - i2
                    i1 += 1
                else:
                    i2 += 1

        def foo(i, k):
            if k - i <= 1:
                return
            j = (k + i) / 2
            foo(i, j)
            foo(j, k)
            count(i, j, k)
            merge(i, j, k)

        foo(0, len(nums))
        return ret[0]
