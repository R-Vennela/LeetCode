class Solution(object):
    def findDuplicates(self, nums):
        emp=set()
        ans=[]
        for q in nums:
            if q not in emp:
                emp.add(q)
            else:
                ans.append(q)

        return ans 