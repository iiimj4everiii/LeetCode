# Augmented Doubly Linked List.
class LRUCacheNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:

        if key in self.cache.keys():

            self.update_relevancy(key)

            return self.head.val

        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache.keys():
            node = self.cache[key]
            node.val = value
            self.update_relevancy(key)

        else:
            if len(self.cache) == self.capacity:
                tail_key = self.tail.key
                self.cache.pop(tail_key)

                self.tail = self.tail.left

                if self.tail is not None:
                    self.tail.right = None

            # Create the new node and bring it to the front of the
            # linked list as it is the most recently used node.
            new_node = LRUCacheNode(key, value, None, self.head)

            # Handling corner cases: If new_node is the first node
            # to be inserted, we set the tail node to it as well as
            # the head node.
            if len(self.cache) == 0:
                self.tail = new_node

            # Otherwise, point the original head node's left to this
            # new node.
            else:
                self.head.left = new_node

            # Update the cache and the head node to this new node.
            self.cache[key] = new_node
            self.head = new_node

    def update_relevancy(self, key):

        node = self.cache[key]

        left_node = node.left
        right_node = node.right

        if left_node is None:
            return
        else:
            left_node.right = right_node

        if right_node is None:
            self.tail = self.tail.left
            self.tail.right = None
        else:
            right_node.left = left_node

        node.left = None
        self.head.left = node
        node.right = self.head

        self.head = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(2)
# obj.put(1,1)
# obj.put(2,2)
# print(obj.get(1))
# obj.put(3,3)
# print(obj.get(2))
# obj.put(4,4)
# print(obj.get(1))
# print(obj.get(3))
# print(obj.get(4))

# obj = LRUCache(2)
# obj.put(2,1)
# obj.put(2,2)
# print(obj.get(2))
# obj.put(1,1)
# obj.put(4,1)
# print(obj.get(2))

obj = LRUCache(1)
obj.put(2,1)
print(obj.get(2))
obj.put(3,2)
print(obj.get(2))
print(obj.get(3))
