class Solution:
    def sortJumbled(self, mapping, nums) :
        def translate_integer(num) :
            digits = list(str(num))
            for i in range(len(digits)):
                digits[i] = str(mapping[int(digits[i])])
            return int("".join(digits))

        number_mapping = {}
        for num in nums:
            number_mapping[num] = translate_integer(num)
        nums.sort(key=lambda val: number_mapping[val])

        return nums