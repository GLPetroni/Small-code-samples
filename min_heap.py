# Course: CS261 - Data Structures
# Assignment: 5
# Student:
# Description:


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def left_child(self, index):
        if index is None:
            return None, None
        return 2*index, self.heap[2*index]

    def right_child(self, index):
        if index is None:
            return None, None
        return (2*index)+1, self.heap[(2*index)+1]

    def parent(self, index):
        if index is None:
            return None, None
        return (index//2)-1, self.heap[(index//2)-1]

    def bubble_up(self, index):
        cur = self.heap[index]
        parent_num = (index-1) >> 1
        if index > 0:
            parent = self.heap[parent_num]
            if cur <= parent:
                self.heap[index], self.heap[parent_num] = parent, cur
                self.bubble_up(parent_num)



    def add(self, node: object) -> None:
        """
        TODO: Write this implementation
        """
        self.heap.append(node)
        self.bubble_up(self.heap.length()-1)

    def get_min(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise MinHeapException
        index = self.heap.length()-1
        cur = self.heap[index]
        while index != 0:
            tmp = self.heap[index-1]
            if tmp < cur:
                cur = tmp
                index = index-1
            else:
                index = index-1
        return cur

    def remove_min(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise MinHeapException
        index = self.heap.length()-1
        cur = self.heap[index]
        while index != 0:
            tmp = self.heap[index-1]
            if tmp < cur:
                cur = tmp
                index = index-1
            else:
                index = index-1
        tmp = self.heap[self.heap.length()-1]
        if self.heap.length() == 1:
            self.heap.pop()
            return cur
        self.heap[index], self.heap[self.heap.length()-1] = tmp, cur
        k = self.heap.pop()
        da = self.heap
        start = self.heap.length()//2-1
        for i in range(start, -1, -1):
            self._bubble_down(i)
        return k

    def _bubble_down(self, parent: int) -> None:
        """ Bubble down given node to correct heap position """
        swapped = True
        while swapped:
            swapped = False
            left = parent * 2 + 1
            right = parent * 2 + 2
            if right < self.heap.length() and self.heap.get_at_index(right) < self.heap.get_at_index(left):
                left = right
            if left < self.heap.length() and self.heap.get_at_index(parent) > self.heap.get_at_index(left):
                self.heap.swap(left,parent)
                parent = left
                swapped = True


    def build_heap(self, da: DynamicArray) -> None:
        """
        TODO: Write this implementation
        """
        tmp = DynamicArray()
        i = 0
        while i != self.heap.length():
            self.heap[i] = None
            i += 1
        j = 0
        while j < da.length():
            tmp.append(da[j])
            j+=1
        self.heap = tmp
        start = self.heap.length()//2 - 1
        for i in range(start, -1, -1):
            self._bubble_down(i)


# BASIC TESTING
if __name__ == '__main__':

    #print("\nPDF - add example 1")
    #print("-------------------")
    #h = MinHeap()
    #print(h, h.is_empty())
    #for value in range(300, 200, -15):
    #    h.add(value)
    #    print(h)

    #print("\nPDF - add example 2")
    #print("-------------------")
    #h = MinHeap(['fish', 'bird'])
    #print(h)
    #for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
    #    h.add(value)
    #    print(h)


    #print("\nPDF - get_min example 1")
    #print("-----------------------")
    #h = MinHeap(['fish', 'bird'])
    #print(h)
    #print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())


    #print("\nPDF - build_heap example 1")
    #print("--------------------------")
    #da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    #h = MinHeap(['zebra', 'apple'])
    #print(h)
    #h.build_heap(da)
    #print(h)
    #da.set_at_index(0, 500)
    #print(da)
    #print(h)
    #h = MinHeap([])
    #da = DynamicArray([-4,2,-3,1,1])
    #print('should be: [-4, 1, -3, 2, 1]')
    #h.build_heap(da)
    #print('end: ',h)
    #da = DynamicArray([1, 0, -2, -3])
    #print('should be: [-3, 0, -2, 1]')
    #h.build_heap(da)
    #print('end: ', h)

