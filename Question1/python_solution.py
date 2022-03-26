class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use the double loop to check the numbers in the 
        # the file
        output = [];
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j] == target):
                    output.append(i);
                    output.append(j);
                    return output
                else:
                    j+=1;
            i+=1
