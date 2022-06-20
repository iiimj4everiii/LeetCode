class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list, k: int, t: int) -> bool:

        # Not yet implemented.

        # Strategy:
        # 1) Create a list of pointer mirroring nums ordering. We will use this
        #    to find the oldest node later on. This will take O(n) time.

        # Use a self-balancing tree (red-black tree) as our primary structure.
        # 2) Initialize the RB tree with the first k elements in nums.
        # 3) Check to see if we can find any nearby-almost-duplicate nodes.
        # These 2 steps will take k log k + k = O(k log k) time.

        # 4) For each new node from index k to len(history) in history,
        #    1) Insert the new node into the sorted RB tree. This takes log(k)
        #       time.
        #    2) Find the node's predecessor and the successor. Then compare
        #       their value to the new node's. If the values are within t, then
        #       we are done. Return True. It takes O(log k) time to find the
        #       predecessor and successor.
        #    3) Otherwise, get the oldest node pointer from history and remove
        #       it from the RB tree. This also takes O(log k) time.

        # The total time complexity for this algorithm takes:
        # an + bk + ck log k + dn log k = O(n log k) times.

        return False


n = [3, 1, 7, 5, 3, 1, 5, 7]
sol = Solution().containsNearbyAlmostDuplicate(n, 3, 1)
print(sol)
