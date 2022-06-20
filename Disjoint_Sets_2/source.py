class Disjoint_Sets:
    def __init__(self, all_sets):
        self.all_sets = all_sets

    def get_set_representative(self, element):

        rank = 0
        while self.all_sets[element] is not None:
            element = self.all_sets[element]
            rank += 1

        return element, rank

    def find(self, element1, element2):

        # Get the representative of the set where element1 is in.
        representative1, _ = self.get_set_representative(element1)

        # Get the representative of the set where element2 is in.
        representative2, _ = self.get_set_representative(element2)

        # See if they belong to the same set.
        return representative1 == representative2

    def union(self, element1, element2):

        representative1, rank1 = self.get_set_representative(element1)

        representative2, rank2 = self.get_set_representative(element2)

        # For optimization purpose, we should merge the set with lower
        # rank into the set with the higher rank. The combined set will
        # be represented by the representative of the higher rank set.
        if rank1 < rank2:
            self.all_sets[representative1] = representative2
        else:
            self.all_sets[representative2] = representative1

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
print(disjoint_set.union(1, 5))
print(disjoint_set.find(1, 4))
print(disjoint_set.find(5, 7))