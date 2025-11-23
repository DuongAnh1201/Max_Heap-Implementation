
class MaxHeap:
    def __init__(self):
        self.heap = []
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
    def sift_down(self, index):
        temp = index
        key = self.heap[index]
        while True:
            left = self.left_child(temp)
            right = self.right_child(temp)
            largest = temp
            
            # Compare with left child
            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left
            
            # Compare with right child
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right
            
            # If the element is already in the correct position, stop
            if largest == temp:
                break
            
            # Move the larger child up
            self.heap[temp] = self.heap[largest]
            temp = largest
        
        # Place the key in its final position
        self.heap[temp] = key
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