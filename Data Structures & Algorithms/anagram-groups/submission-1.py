class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def create_counter(string):
            c = {}

            for s in string:
                if s in c:
                    c[s] += 1
                else:
                    c[s] = 1

            return c

        counter_list = []

        for word in strs:
            counter_list.append(create_counter(word))

        counter_groups = []
        used_indexes = set()

        for i in range(len(counter_list)):
            if i in used_indexes:
                continue
            j = i+1
            ref_counter = counter_list[i]
            tmp_group = [strs[i]]
            while j< len(counter_list):
                if j in used_indexes:
                    j+=1
                    continue
                if ref_counter == counter_list[j]:
                    tmp_group.append(strs[j])
                    used_indexes.add(j)
                j+=1

            counter_groups.append(tmp_group)
            i+=1
        
        return counter_groups




        