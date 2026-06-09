class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ang_map = {}

        for string in strs:
            sorted_str = ''.join(sorted(string))

            if sorted_str in ang_map:
                ang_map[sorted_str].append(string)
            else:
                ang_map[sorted_str] = [string]

        return list(ang_map.values())
        