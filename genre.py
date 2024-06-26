from enum import Enum

# ---------------------------------------
# --- class Genre 
# ---------------------------------------
class Genre(Enum):
    M= 1
    F= 2
    O= 3

    def __str__(self): return self.name
    def __repr__(self): return self.name
    
if __name__ == "__main__":
    g = Genre.F
    print(g)