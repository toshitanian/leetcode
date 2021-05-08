use std::collections::HashMap;

pub struct Solution {}

impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let mut map: HashMap<i32, i32> = HashMap::new();
        for n in nums {
            let prev_count: i32 = match map.get(&n) {
                Some(c) => *c,
                None => 0,
            };
            let count = prev_count + 1;
            map.insert(n, prev_count + count);
        }
        let mut target: i32 = -1;
        for (k, v) in map {
            if v == 1 {
                target = k;
            }
        }
        return target;
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn case1() {
        let vec = vec![2, 2, 1];
        assert_eq!(Solution::single_number(vec), 1);
    }
    #[test]
    fn case2() {
        let vec = vec![4, 1, 2, 1, 2];
        assert_eq!(Solution::single_number(vec), 4);
    }
    #[test]
    fn case3() {
        let vec = vec![1];
        assert_eq!(Solution::single_number(vec), 1);
    }
}

fn main() {}
