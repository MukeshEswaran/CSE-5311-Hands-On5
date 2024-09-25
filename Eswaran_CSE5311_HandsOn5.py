class MinHeap:
    def __init__(self, array=None):
        self.heap = array if array else []
        if self.heap:
            self.build_min_heap()

    # Using bit manipulation to calculate the parent, left, and right child indexes
    def parent(self, index):
        return (index - 1) >> 1

    def left(self, index):
        return (index << 1) + 1

    def right(self, index):
        return (index << 1) + 2

    # Build the min heap from an arbitrary array
    def build_min_heap(self):
        # Start from the last parent and heapify downwards
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify(i)

    # Heapify the node at index i (shift it down if necessary)
    def heapify(self, i):
        left = self.left(i)
        right = self.right(i)
        smallest = i

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    # Insert a new element into the heap
    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)

    # Sift up to maintain the heap property after insertion
    def sift_up(self, index):
        parent_idx = self.parent(index)
        while index > 0 and self.heap[index] < self.heap[parent_idx]:
            self.heap[index], self.heap[parent_idx] = self.heap[parent_idx], self.heap[index]
            index = parent_idx
            parent_idx = self.parent(index)

    # Remove and return the root node (the minimum element)
    def pop(self):
        if len(self.heap) == 0:
            return None
        # Swap the root with the last element and pop it
        root_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify(0)
        return root_value

    # Return the current state of the heap
    def get_heap(self):
        return self.heap


# Demonstration
if __name__ == "__main__":
    # Initializing a min heap with an arbitrary array
    array = [9, 4, 7, 1, -2, 6, 5]
    heap = MinHeap(array)

    print("Initial heap after building:", heap.get_heap())

    # Inserting a new element into the heap
    heap.insert(0)
    print("Heap after inserting 0:", heap.get_heap())

    # Removing the minimum element from the heap (root node)
    root = heap.pop()
    print("Popped root (minimum element):", root)
    print("Heap after popping root:", heap.get_heap())

    # Another pop to remove the current minimum
    root = heap.pop()
    print("Popped another root (minimum element):", root)
    print("Heap after popping second root:", heap.get_heap())
