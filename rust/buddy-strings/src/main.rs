use std::collections::HashSet;

struct Solution {}
impl Solution {
    pub fn buddy_strings(a: String, b: String) -> bool {
        if a.len() != b.len() {
            return false;
        }
        if a == b {
            let mut seen: HashSet<&u8> = HashSet::new();
            for a_char in a.as_bytes() {
                let ok = seen.insert(a_char);
                if !ok {
                    return true;
                }
            }
        }
        let a_bytes = a.as_bytes();
        let b_bytes = b.as_bytes();
        let mut pairs: Vec<(u8, u8)> = Vec::new();
        for i in 0..a.len() {
            let a_char = a_bytes[i];
            let b_char = b_bytes[i];
            if  a_char != b_char {
                let pair = (a_char, b_char);
                pairs.push(pair);

            }
        }
        if pairs.len() != 2 {
            return false;
        }
        if pairs[0].0 == pairs[1].1 && pairs[0].1 == pairs[1].0 {
            return true;
        }
        return false
    }
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn case1() {
        let a = String::from("aa");
        let b = String::from("aa");
        let r = Solution::buddy_strings(a, b);
        assert_eq!(r, true);
    }
    #[test]
    fn case2() {
        let a = String::from("abc");
        let b = String::from("a");
        let r = Solution::buddy_strings(a, b);
        assert_eq!(r, false);
    }
    #[test]
    fn case3() {
        let a = String::from("aaaabc");
        let b = String::from("aaaacb");
        let r = Solution::buddy_strings(a, b);
        assert_eq!(r, true);
    }
}
fn main() {}
