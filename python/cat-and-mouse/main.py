
from typing import List

"""

https://leetcode.com/problems/cat-and-mouse/

Input: graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
Output: 0

Input: graph = [[1,3],[0],[3],[0,2]]
Output: 1
"""


def _breadth_first_search(start_node: int, target_node: int, graph: List[List[int]], ignore_nodes=[]):
    queue = []
    # current_node, visited_nodes
    queue.append((start_node, []))

    while len(queue) > 0:
        current_node, prev_visited_nodes = queue.pop(0)
        visited_nodes = prev_visited_nodes + [current_node]
        if current_node == target_node:
            return visited_nodes
        next_nodes = graph[current_node]
        possible_nodes = [_ for _ in next_nodes if _ not in visited_nodes + ignore_nodes]

        for n in possible_nodes:
            queue.append((n, visited_nodes))
    return []


def _cat_possible_nodes(current_node: int, visited_node: List[int], graph: List[List[int]]):
    next_nodes = graph[current_node]
    possible_nodes = [_ for _ in next_nodes if _ not in visited_node + [0]]
    return possible_nodes

def _both_move(graph: List[List[int]]):
    """TODO: mouse don't move cat's next possible node
    """

    current_mouse_node = 1
    current_cat_node = 2

    mouse_target_node = 0
    cat_target_node = current_cat_node

    mouse_visited_nodes = [current_mouse_node]
    cat_visited_nodes = [current_cat_node]

    while True:
        print(f"mouse current: {current_mouse_node}")
        cat_possible_nodes = _cat_possible_nodes(current_cat_node, cat_visited_nodes, graph)
        print(f"cat possible nodes: {cat_possible_nodes}")
        next_possible_mouse_node = None

        tried_mouse_node = []
        while True:
            mouse_path = _breadth_first_search(current_mouse_node, mouse_target_node, graph, ignore_nodes=tried_mouse_node)
            print(f"possible mouse path {mouse_path}, possible_cat_nodes: {cat_possible_nodes}")
            if len(mouse_path) == 0:
                print("** cat win / no possible mouse node")
                return 2

            next_possible_mouse_node = mouse_path[1]
            if next_possible_mouse_node not in cat_possible_nodes:
                break
            tried_mouse_node.append(next_possible_mouse_node)
        print(f"mouse path {mouse_path}")
        current_mouse_node = next_possible_mouse_node

        if current_mouse_node in mouse_visited_nodes:
            print(f"** mouse repeased: {current_mouse_node} in {mouse_visited_nodes}")
            return 0
        mouse_visited_nodes.append(current_mouse_node)
        print(f"mouse moved to: {current_mouse_node}, visited: {mouse_visited_nodes}")

        if current_mouse_node == 0:
            print("** mouse win")
            return 1

        cat_target_node = current_mouse_node
        print(f"cat current: {current_cat_node}")
        cat_path = _breadth_first_search(current_cat_node, cat_target_node, graph, ignore_nodes=[0])
        print(f"cat path {cat_path}")
        current_cat_node = cat_path[1]

        if current_cat_node in cat_visited_nodes:
            print(f"** cat repeased: {current_cat_node} in {cat_visited_nodes}")
            return 0

        cat_visited_nodes.append(current_cat_node)
        print(f"cat moved to: {current_cat_node}, visited: {cat_visited_nodes}")

        if current_cat_node == current_mouse_node:
            print("** cat win")
            return 2
    print("** unexpected end")
    return 0

class Solution:
    """
    - mouse starts at node 1 (Goes first)
    - cat starts at node 2

    Mouse has to move to node 0 (return 1 for win)
    Cat has to move to node where mouse is (return 2 for win)
    Draw (return 0 for win)
    """

    def catMouseGame(self, graph: List[List[int]]) -> int:
        return _both_move(graph)


def test_mouse_bfs():
    start_node = 1
    target_node = 0
    graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
    visited_nodes = []
    l = _breadth_first_search(start_node, target_node, graph)
    print(l)

def test_cat_bfs():
    start_node = 2
    target_node = 3
    graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
    visited_nodes = []
    l = _breadth_first_search(start_node, target_node, graph, ignore_nodes=[0])
    print(l)

def test_both_move():
#     graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
#    graph = [[1,3],[0],[3],[0,2]]
#    _both_move(graph)
    graph = [[3,4],[3,5],[3,6],[0,1,2],[0,5,6],[1,4],[2,4]] # return 0
    s = Solution()
    s.catMouseGame(graph)

if __name__ == "__main__":
#    test_mouse_bfs()
#    test_cat_bfs()
    test_both_move()
