class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapper = dict()
        mapped_symbols = set()
        for left, right in zip(s, t):
            replacement = mapper.get(left)
            if replacement is None:
                if right in mapped_symbols:
                    return False
                mapper[left] = right
                mapped_symbols.add(right)
            elif replacement != right:
                return False
        return True
