class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        O(N) * O(N/2) = O(N^2)
        -> This order is not correct, order is O(N^3)
        """

        current_longest_substring = ""
        for i in range(len(s)):
            rest = s[i:]
            current_str = ""
            for char in rest:
                if char in current_str:
                    break
                current_str += char

            if len(current_str) > len(current_longest_substring):
                current_longest_substring = current_str
        print(f"ret: {current_longest_substring}")
        return len(current_longest_substring)


def t():
    sol = Solution()

    s = "pwwkew"
#    s = " "
    r = sol.lengthOfLongestSubstring(s)
    print(r)

t()
