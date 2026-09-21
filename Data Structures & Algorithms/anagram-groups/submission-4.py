class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        a=ord('a')
        for s in strs:
             
            count = [0]*26
            
            for i in s:
                count[ord(i)-a] +=1
            
            res[tuple(count)].append(s)
            
        return list(res.values())
