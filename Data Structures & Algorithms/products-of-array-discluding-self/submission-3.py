class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        # for loop through the list
        # in each iteration, fill a list with every value except 
        # i
        # another for loop to multiply all those together and add to a 
        # final list

        final_list = []
        for i in range(len(nums)):
            product_list = []
            product = 1
            for j in range(len(nums)):
                if j != i: #if it's not the current num (nums[i])
                    product_list.append(nums[j])
            for i in product_list:
                product = i*product
            final_list.append(product)
        return final_list

        


        
