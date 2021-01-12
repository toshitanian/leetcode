from typing import List

# !! I googled how to xor decimal binary

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decoded = [first]
        left = first
        for elem in encoded:
            next = int(bin(elem),2) ^ int(bin(left), 2)
            # next = elem ^ left is okay

            decoded.append(next)
            left = next
        return decoded

def t():
    s = Solution()
#    encoded = [6,2,7,3]
#    first = 4
    # Output: [4,2,0,7,4]

#    encoded = [1,2,3]
#    first = 1
    # Output: [1,0,2,1]

    encoded = [6]
    first = 1
    # [1,7]
    o = s.decode(encoded, first)
    print(o)

t()