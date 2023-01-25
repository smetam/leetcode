from operator import itemgetter


# O(n) time, O(n) space
class Solution:

    @staticmethod
    def manacher(s: str, bogus='#'):
        s = bogus + bogus.join(list(s)) + bogus
        n = len(s)
        # radius of the longest palindrome with center at each index 
        dp = [0 for _ in range(n)]
        radius, center = 0, 0
        while center < n:

            # find the longest palindrome for current center
            while (
                0 <= center - radius - 1
                and center + radius + 1 < n
                and s[center - radius - 1] == s[center + radius + 1]
            ):
                radius += 1
            dp[center] = radius

            # for other centers inside found palindrome
            old_center, old_radius = center, radius
            center, radius = center + 1, 0
            while center <= old_center + old_radius:
                # since it lies inside a palindrome it has a mirrored value
                mirrored_center = old_center - (center - old_center)
                max_mirrored_radius = old_center + old_radius - center

                if dp[mirrored_center] < max_mirrored_radius:
                    # if mirrored palindrome is entirely inside old palindrome
                    dp[center] = dp[mirrored_center]
                    center += 1
                elif dp[mirrored_center] > max_mirrored_radius:
                    # if mirrored palindrome is outside of old palindrome 
                    # then new palindrome ends at the edge of old palindrome
                    # otherwise old palindrome radius would be bigger
                    dp[center] = max_mirrored_radius
                    center += 1
                else:
                    # dp[mirrored_center] == max_mirrored_radius

                    # since mirrored palindrome ended at old palindrome's edge
                    # new palindrome might be bigger
                    radius = max_mirrored_radius
                    # exit while loop
                    break
        center, radius = max(enumerate(dp), key=itemgetter(1))
        return s[center - radius:center + radius + 1].replace(bogus, "")
    
    def longestPalindrome(self, s: str) -> str:
        return self.manacher(s)


# O(n^2) time, O(1) space
class Solution1:
    @staticmethod
    def _expand(s: str, left: int, right: int) -> int:
        n = len(s)
        while (
            left >=0 
            and right < n 
            and s[left] == s[right]
        ):
            left -= 1
            right += 1
        return right - left - 1

    def longestPalindrome(self, s: str) -> str:
        left, right = 0, 0
        for i in range(len(s)):
            even_len = self._expand(s, i, i+1)
            odd_len = self._expand(s, i, i)
            new_len = max(even_len, odd_len)
            if new_len > right - left + 1:
                left = i - (new_len - 1) // 2
                right = i + new_len // 2
            
        return s[left:right+1]
