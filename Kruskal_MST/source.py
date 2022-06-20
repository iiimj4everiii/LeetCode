class DisjointSets:

    def __init__(self, all_sets: dict):

        self.all_sets = all_sets

        return

    def get_set_rep(self, element):

        rank = 0
        while self.all_sets[element] is not None:
            element = self.all_sets[element]
            rank += 1

        return element, rank

    def find(self, element1, element2):

        rep1, _ = self.get_set_rep(element1)

        rep2, _ = self.get_set_rep(element2)

        return rep1 == rep2

    def union(self, element1, element2):

        rep1, rank1 = self.get_set_rep(element1)

        rep2, rank2 = self.get_set_rep(element2)

        if rank1 < rank2:
            self.all_sets[rep1] = rep2

        else:
            self.all_sets[rep2] = rep1

        return


class MinHeap:

    def __init__(self, complete_tree: list):

        self.min_heap = complete_tree

        self.build_heap_bottom_up()

        return

    @staticmethod
    def get_left_child_index(index):

        return 2 * index + 1

    def heapify(self, index):

        left_child_index = self.get_left_child_index(index)
        left_child = None
        if left_child_index < len(self.min_heap):
            left_child = self.min_heap[left_child_index]

        if left_child is None:
            return

        right_child_index = left_child_index + 1
        right_child = None
        if right_child_index < len(self.min_heap):
            right_child = self.min_heap[right_child_index]

        if right_child is None:
            if left_child < self.min_heap[index]:
                self.min_heap[index], self.min_heap[left_child_index] = self.min_heap[left_child_index], self.min_heap[index]
                self.heapify(left_child_index)

        else:
            [smaller_child, smaller_child_index] = min([left_child, left_child_index], [right_child, right_child_index])
            if smaller_child < self.min_heap[index]:
                self.min_heap[index], self.min_heap[smaller_child_index] = self.min_heap[smaller_child_index], self.min_heap[index]
                self.heapify(smaller_child_index)

        return

    def build_heap_bottom_up(self):

        last_non_leaf_node_index = len(self.min_heap) // 2 - 1

        for idx in range(last_non_leaf_node_index, -1, -1):

            self.heapify(idx)

        return

    def extract_min(self):

        self.min_heap[0], self.min_heap[-1] = self.min_heap[-1], self.min_heap[0]

        min_element = self.min_heap.pop()

        self.heapify(0)

        return min_element


def MST_Kruskal(v: dict, e: dict):

    edges = []

    return edges


v = {
    
}

e = {

}