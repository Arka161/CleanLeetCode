class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        iterative_map = dict()
        
        for i in nums:
            if i in iterative_map:
                iterative_map[i] += 1
            else:
                iterative_map[i] = 1
                
        ans_map = collections.defaultdict(list)
        for i in range(len(nums), 0, -1):
            ans_map[i] = []
        
        for k_c, v_c in iterative_map.items():
            ans_map[v_c].append(k_c)
        
        stop_index = k
        
        final_l = list()
        for k_a, v_a in ans_map.items():
            if len(ans_map[k_a]) >= 1:
                for i in ans_map[k_a]:
                    if len(final_l) == stop_index:
                        return final_l
                    if len(final_l) < stop_index:
                        final_l.append(i)
        return final_l
        
        
        