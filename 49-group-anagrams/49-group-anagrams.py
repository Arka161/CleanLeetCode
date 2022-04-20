class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_dict = collections.defaultdict(list)
        
        for i in strs:
            str_t = ""
            sorted_s = sorted(i)
            str_t = "".join(sorted_s)
            ans_dict[str_t].append(i)
        
        final_arr = []
        
        pos = 0
        for k, v in ans_dict.items():
            final_arr.append(v)
        return final_arr