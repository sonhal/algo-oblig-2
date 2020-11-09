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

**Run the program**
```bash
python3 -m exercise_1 [-h] in_file out_file

Use A* to search for optimal path in puzzle

positional arguments:
  in_file     file with problem puzzle
  out_file    output file name

optional arguments:
  -h, --help  show this help message and exit
```

### Exercise 3 (Network Flow)
Given a graph of capacities, give a output with the value of the optimal flow, 
the flow over each edge, and a cut proving that the flow is optimal.

**Note:** 
- Steps in the implementation is defined as number of times the BFS is computed over the graph.
- Min cut uses Depth-First search.

```bash
usage: python -m exercise_3  [-h] in_file out_file

Use Ford-Fulkerson algorithm to find maximum flow and minimum cut in a digraph

positional arguments:
  in_file     File with problem edges
  out_file    output file name

optional arguments:
  -h, --help  show this help message and exit

```