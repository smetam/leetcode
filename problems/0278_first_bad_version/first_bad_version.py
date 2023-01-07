# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int, isBadVersion) -> int:
        good_version = 0
        bad_vesion = n
        while good_version + 1 != bad_vesion:
            version = (good_version + bad_vesion) // 2
            bad = isBadVersion(version)
            if bad:
                bad_vesion = version
            else:
                good_version = version
        return bad_vesion
            
        

