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

Input
    - from file
    - output file
    - input file
        - first line: number of nodes m.
        - following first line: m lines with m numbers each (matrix) defining the 
        capacities between each pair of nodes. number on (i, j) is the capacity from node i to j (edge i,j)
        - Nodes[0: m-1] where 0 is source and m-1 is sink
        - no edges goes to source (column 0 is all 0's) and no edges goes from sink (row m -1 is all 0's)
        
Output
    - Line with value of optimal flow
    - Line with nodes (by number, sorted) on the source side of a cut with capacity of optimal flow. Source node included
    - number of steps used to obtain the optimal flow (migth vary)
    - m x m lines with where cells are filled with flow number, same format as input
        
            

Graph
    - Directed graph
    - capacaty from v to w can be different from w to v
    - capacities: non-neg int
    - vertex = node
 

 
Flow graph
    Node
        - has capacity
        - flow (capasity used)
        - flow/capasity
        