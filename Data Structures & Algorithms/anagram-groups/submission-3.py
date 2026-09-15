class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_hash_code(ss):
            counter = {
                "a" : 0,
                "b" : 0,
                "c" : 0,
                "d" : 0,
                "e" : 0,
                "f" : 0,
                "g":0,
                "h":0,
                "i":0,
                "j":0,
                "k":0,
                "l":0,
                "m":0,
                "n":0,
                "o":0,
                "p":0,
                "q":0,
                "r":0,
                "s":0,
                "t":0,
                "u":0,
                "v":0,
                "w":0,
                "x":0,
                "y":0,
                "z":0
            }

            for s in ss:
               counter[s] += 1

            hash_list = []

            for i in counter:
                if counter[i] > 0:
                    hash_list.append(i+str(counter[i]))

            return "".join(hash_list)
        cat = {}
        for s in strs:
            hash_code = get_hash_code(s)
            if hash_code in cat:
                cat[hash_code].append(s)

            else:
                cat[hash_code] = [s]

        return list(cat.values())
            






