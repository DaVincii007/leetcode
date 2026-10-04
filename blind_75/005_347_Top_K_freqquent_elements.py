# https://leetcode.com/problems/top-k-frequent-elements/description/

def topKFrequent(nums: list[int], k: int) -> list[int]:
        nums_dict = {}
        freq_dict = {}

        for num in nums:
            freq = 0
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
            
            freq = nums_dict[num]
            if freq>1:
                freq_dict[freq-1].remove(num)

            if freq in freq_dict:
                freq_dict[freq].append(num)
            else:
                freq_dict[freq] = [num]
        
        ret = [] 
        sorted_freq = sorted(freq_dict.keys())
        
        while k>0:
            highest_freq_elements = freq_dict[sorted_freq.pop(-1)]
            for num in highest_freq_elements:
                ret.append(num)
                k-=1
                if k==0:
                    break
        return ret

print(topKFrequent([1,1,1,2,2,3], 2))