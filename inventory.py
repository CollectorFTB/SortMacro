"""
The Inventory, StashTab, QuadTab classes let you iterate over stash positions on your screen easily
"""
from dataclasses import dataclass

# Voodoo 2560x1440 numbers
ITEM_WIDTH = 36 * 2
STASH_START = (56, 214)
INVENTORY_START = (1725, 820)

@dataclass
class Storage:   
    def __iter__(self):
        self.cur_col = 0
        self.cur_row = 0
        return self

    def __next__(self):
        if self.cur_row == self.height:
            raise StopIteration

        # Calculate next mouse location
        x,y = self.start
        next_position = x + int(self.cur_col * self.step), y + int(self.cur_row * self.step) 
    
        # Update current position
        self.cur_row = self.cur_row + 1 if self.cur_col == self.width - 1 else self.cur_row 
        self.cur_col = (self.cur_col + 1) % self.width

        return next_position

class StashTab(Storage):
    width: int = 12
    height: int = 12
    step: float = ITEM_WIDTH
    start: tuple = STASH_START


class QuadTab(StashTab):
    width: int = 24
    height: int = 24
    step: float = ITEM_WIDTH // 2
    start: tuple = STASH_START

class Inventory(Storage):
    width: int = 12
    height: int = 5
    step: float = ITEM_WIDTH
    start: tuple = INVENTORY_START