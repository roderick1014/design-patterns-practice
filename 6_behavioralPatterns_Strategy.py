'''

    Design Pattern 6: Behavioral Patterns - Strategy.

'''

from abc import ABC, abstractmethod  # Abstract based classes

class FilterStrategy(ABC):

    @abstractmethod
    def removeValue(self, val):
        pass

class RemoveNegativeStrategy(FilterStrategy):

    def removeValue(self, val):
        # If the val < 0, return non-zero value.
        return val < 0
    
class RemoveOddStrategy(FilterStrategy):

    def removeValue(self, val):
        # Take the absolute value of an input and mod by 2. 
        # Output > 0 means it's an odd value, thereby return non-zero value.
        return abs(val) % 2
    
class Values:

    def __init__(self, vals):
        self.vals = vals
    
    def filter(self, strategy):
        res = []
        for n in self.vals:
            # Return zero ==> append the value, Non-zero ==> don't append the value to the list.
            if not strategy.removeValue(n):    
                res.append(n)
        return res
    
if __name__ == '__main__':
    values = Values([-7, -4, -1, 0, 2, 6, 9])
    print(values.filter(RemoveNegativeStrategy()))  # [0, 2, 6, 9]
    print(values.filter(RemoveOddStrategy()))       # [-4, 0, 2, 6]