class Fancy:
    def __init__(self):
        self.MOD = 10**9 + 7
        self.sequence = []  # Stores the values at their original state
        self.add = [0]  # Tracks the cumulative add operations
        self.mul = [1]  # Tracks the cumulative multiply operations
        self.current_add = 0
        self.current_mul = 1
    
    def append(self, val: int) -> None:
        # When appending, we need to "undo" the current operations
        # so that when we apply all operations, we get the correct value
        # new_val = (val - current_add) * inverse(current_mul) % MOD
        val = (val - self.current_add) % self.MOD
        val = (val * pow(self.current_mul, self.MOD - 2, self.MOD)) % self.MOD
        self.sequence.append(val)
        self.add.append(self.current_add)
        self.mul.append(self.current_mul)
    
    def addAll(self, inc: int) -> None:
        self.current_add = (self.current_add + inc) % self.MOD
    
    def multAll(self, m: int) -> None:
        self.current_add = (self.current_add * m) % self.MOD
        self.current_mul = (self.current_mul * m) % self.MOD
    
    def getIndex(self, idx: int) -> int:
        if idx >= len(self.sequence):
            return -1
        
        # To get the current value, we need to:
        # val = sequence[idx] * current_mul + current_add
        # But we need to adjust for operations that happened before this element was added
        val = self.sequence[idx]
        
        # Apply the global operations
        val = (val * self.current_mul) % self.MOD
        val = (val + self.current_add) % self.MOD
        
        return val