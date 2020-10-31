# Algorithm: Design and Efficiency 
## Oblig 2

### Exercise 1 (A*)
*Build a A\* program*
*Move the tiles in a way that ends up in the final state*

**Main Requirements**
- solve a 8-puzzle
- solve 15-puzzle
- Program should assume NxN boards
- Can assume N <= 10
- The solution must be optimal (no solution with fewer moves)

**Game Rules**
- let the empty square "switch place" with one of the (max 4)
neighbouring tiles. a move can be L, R, U, D (left, right, up, down).
-  

**Example: N=3**
Here 0 indicates the empty square.
1 2 3
0 4 5
7 8 6

**Example final state**
1 2 3
4 5 6
7 8 0