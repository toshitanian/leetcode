// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}
pub struct Solution {}
impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        return head;
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    // #[test]
    // fn case1() {
    //     let array = Box::new([1, 2, 3, 4, 5]);
    //     let head: Option<Box<ListNode>> = None;
    //     let mut current: Option<Box<ListNode>> = None;
    //     for val in array.iter() {
    //         let node = Some(Box::new(ListNode::new(*val)));
    //         match head {
    //             Some(_) => {
    //                 current.unwrap().next = node;
    //                 current = node;
    //             },
    //             None => {
    //                 head = node;
    //                 current = node;
    //             }
    //         }
    //     };
    //     let n = ListNode::new(10);
    //     // println!("{:?}", head)
    // }
    #[test]
    fn case2() {
        let mut head: Option<Box<ListNode>> = None;
        let second:Option<Box<ListNode>> = Some(Box::new(ListNode::new(200)));
        head = second;
        let t:  Option<Box<ListNode>> = None;
        t = second;
        // second.unwrap().next = head.take();
        // head = second;
        // println!("{:?}", head);
        // println!("{:?}", second);

    }
}

fn main() {}
