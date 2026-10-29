# This class defines a number for matrix base 10 arithmetic
import copy

class Number:
    def __init__(self, size: int, value: list[list[int]]):
        sublist_lengths = [len(sublist) for sublist in value]
        if len(value) == size and all(x == size for x in sublist_lengths):
            self.size = size
            self.value = value

    def expandMatrix(self, size):       #Expands matrix into a desired size, adding 0s where expanded
        if self.size > size:
            raise Exception("Cannot contract a matrix")

        #Expand existing rows into desired size
        for list in self.value:
            while len(list) < size:
                list.append(0)

        #Expands existing matrix into detire size
        while len(self.value) < size:
            self.value.append([0] * size)


    def __add__(self, other):
        copy.deepcopy

    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.value)

test = Number(2, [[1,0],[0,1]])