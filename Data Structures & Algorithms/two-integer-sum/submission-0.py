class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resultat=[]
        for i in range(len(nums)) : 
            for j in range(i+1,len(nums)) : 
                if nums[i]+nums[j]==target :
                    resultat.append(i)
                    resultat.append(j)
        return resultat
    
        
        