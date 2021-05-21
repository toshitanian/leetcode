class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False
        if a == b:
            # if chars can be swapped inside a, return True
            seen = set()
            for a_char in a:
                if a_char in seen:
                    return True
                seen.add(a_char)
            return False
        pairs = []
        for i in range(len(a)):
            a_char = a[i]
            b_char = b[i]
            if a_char != b_char:
                pairs.append((a_char, b_char))
        if len(pairs) != 2:
            return False
        if pairs[0][0] == pairs[1][1] and pairs[0][1] == pairs[1][0]:
            return True

        return False

if __name__ == '__main__':
    s = Solution()
    assert s.buddyStrings("ab", "ba") == True
    assert s.buddyStrings("ab", "ab") == False
    assert s.buddyStrings("aaaaaaabc", "aaaaaaacb") == True
