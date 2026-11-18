class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []
        if len(strs) == 1:
            return [strs]
        collection_dict = defaultdict(list)
        for item in strs:
            key = ''.join(sorted(item))
            collection_dict[key].append(item)
        return list(collection_dict.values())