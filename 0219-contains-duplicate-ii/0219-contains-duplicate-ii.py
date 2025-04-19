class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashtable = defaultdict(list)

        for i,num in enumerate(nums):
            if num in hashtable and (i - hashtable[num][-1]) <= k:
                return True
            hashtable[num].append(i)
        return False   


            
            
            
                
        
         

         
        