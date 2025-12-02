
class MaxHeap:
    def __init__(self, heap = None):
        if heap == None:
            self.heap = []
        else:
            self.heap = heap
    def left_child(self,parent):
        return 2*parent+1
    def right_child(self, parent):
        return 2*parent+2
    def parent(self, child):
        return (child-1)//2
    def sift_up(self, index):
        temp = index
        key = self.heap[index]
        while temp > 0 and self.heap[self.parent(temp)] < key:
            self.heap[temp] = self.heap[self.parent(temp)]  # Move parent down
            temp = self.parent(temp)
        self.heap[temp] = key
        #Sift up works by comparing itself with its parents, if the current node is exceeded their parent, then swap. 
        #Keep the action until it maintains the heap conditions
    def sift_down(self, index, heap_size=None):
        if heap_size is None:
            heap_size = len(self.heap)
        temp = index
        key = self.heap[index]
        while True:
            left = self.left_child(temp)
            right = self.right_child(temp)
            largest = temp
            
            # Compare with left child
            if left < heap_size and self.heap[left] > self.heap[largest]:
                largest = left
            
            # Compare with right child
            if right < heap_size and self.heap[right] > self.heap[largest]:
                largest = right
            
            # If the element is already in the correct position, stop
            if largest == temp:
                break
            
            # Move the larger child up
            self.heap[temp] = self.heap[largest]
            temp = largest
        
        # Place the key in its final position
        self.heap[temp] = key
    #Sift down works after removing a node. At that point, the tree is complete but not a heap
    #So, we swap the root node with the larger of its two children, keep it continueing until getting a heap.
    def insert(self, key):
        self.heap.append(key)
        self.sift_up(len(self.heap) - 1)
        return True
    def remove(self):
        if len(self.heap) == 0:
            raise Exception("Heap underflow")
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.sift_down(0)
        return root
    def __str__(self):
        return str(self.heap)
"""
_______________________________________________________________________
"""
"""
Part 2: Build a Heap with Heapify
"""

def heapify(arr):
    heap = MaxHeap(arr)
    # Start from the last parent node and work backwards to the root
    # Last parent is at index (len(arr) - 2) // 2
    for i in range((len(arr) - 2) // 2, -1, -1):
        heap.sift_down(i, len(arr))
    return heap
# heapify (building a heap from an unsorted array) is O(n) — but not because each sift-down is O(1).
# Sift-down is not O(1); it can take up to O(log n) time.
# However, most elements sift down only a little, and only a few elements sift down a lot.
# This distribution is what makes the total cost O(n).
arr = [12, 3, 17, 8, 29, 1, 15, 4]
print(heapify(arr))

"""
 Part 3 — Implement Heapsort (20 points)
"""
def heapsort(arr):
    # First, build a max-heap from the array
    heap = MaxHeap(arr)
    n = len(arr)
    # Heapify: start from the last parent and work backwards
    for i in range((n - 2) // 2, -1, -1):
        heap.sift_down(i, n)
    
    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root (max) to end
        arr[0], arr[i] = arr[i], arr[0]
        # Sift down the root, but only consider elements 0 to i-1
        heap.sift_down(0, i)
    
    return arr

print(heapsort(arr))
"""
Part 4 — Application Problem (15 points)
"""

def priority_scheduler():
    # Ask user for 10 integer priorities
    user_input = input("Enter 10 task priorities: > ")
    
    # Parse the input into a list of integers
    priorities = list(map(int, user_input.split()))
    
    # Validate that we have exactly 10 priorities
    if len(priorities) != 10:
        print(f"Error: Expected 10 priorities, but got {len(priorities)}")
        return
    
    # Create a MaxHeap and insert all priorities
    heap = MaxHeap()
    for priority in priorities:
        heap.insert(priority)
    
    # Remove and print tasks in descending order of priority
    print("Tasks in priority order:", end=" ")
    result = []
    while len(heap.heap) > 0:
        result.append(str(heap.remove()))
    
    print(" ".join(result))

# Run the priority scheduler
if __name__ == "__main__":
    priority_scheduler()
