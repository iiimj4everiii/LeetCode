class Disjoint_Sets:
    def __init__(self, all_sets):
        self.all_sets = all_sets

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


# Using a dictionary/or something other random access data structure.
all_sets = {
    1:  2,
    2:  3,
    3:  None,
    4:  5,
    5:  6,
    6:  None,
    7:  None
}

disjoint_set = Disjoint_Sets(all_sets)
print(disjoint_set.find(2, 3))
print(disjoint_set.find(1, 4))

print("")

disjoint_set.union(1, 5)
print(disjoint_set.find(1, 4))
print(disjoint_set.find(5, 7))

print("")

disjoint_set.union(1, 7)
print(disjoint_set.find(5, 7))
