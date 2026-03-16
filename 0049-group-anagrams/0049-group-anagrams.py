class Solution(object):
    def groupAnagrams(self, strs):
        map = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in map:
                map[key] = []
            map[key].append(word)
        return list(map.values())
        