# ITS Graph Theory class Group 5 Assignment 10

Group 5 Members:

- Maulana Anugra Putra/5025251159 (kukii83)

- I Gusti Agung Candra Nugraha/5025251169 (candranugraha576)

- Hussein Mohammad Mahsun/5025251170 (TheDelightOFice)

---

In this project, we will be basing our programs based on two materials:

- Coloring 
- Matching

# Sudoku Solver using Graph Coloring

A Sudoku solver that models the puzzle as a **graph coloring problem** and solves it with **backtracking** and the **MRV (DSATUR-style) heuristic**.

## 1. Graph Model

| Sudoku concept | Graph concept |
|---|---|
| Cell (81 total) | Vertex |
| Two cells sharing a row, column, or 3×3 box | Edge |
| Digit 1-9 | Color |
| Given clue | Pre-colored vertex |
| Valid solution | Proper coloring (no edge connects two same-colored vertices) |

Each vertex has degree 20 (8 in its row + 8 in its column + 4 more in its box). The goal is to color all 81 vertices with 9 colors so that no two adjacent vertices share a color.

## 2. Algorithm

### Step 1: Build the graph
For every pair of cells, add an edge if they share a row, column, or box. This is done once.

### Step 2: Validate the pre-coloring
Check all clue vertices. If two adjacent clues have the same digit, the puzzle is invalid and the solver stops immediately.

### Step 3: Choose the next vertex (MRV / DSATUR idea)
For each uncolored vertex, compute its available colors:

    available(v) = {1..9} - {color(u) : u is a neighbor of v}

Pick the vertex with the **fewest** available colors. This is the most constrained vertex (highest saturation in DSATUR terms). If a vertex has 0 options we hit a dead end right away, and if it has 1 option the move is forced.

### Step 4: Try colors and recurse
Assign each available color in turn and recurse on the next vertex.

### Step 5: Backtrack
If a vertex has no available colors, or every color tried led to a dead end, reset the vertex to uncolored and return to the previous vertex to try its next color.

### Step 6: Terminate
- **Success:** no uncolored vertex is left.
- **Failure:** every option at the first choice has been exhausted, so no valid coloring exists.

## 3. Pseudocode

    solve(color):
        v, options = uncolored vertex with fewest available colors
        if v is None:
            return True                  # all vertices colored
        for d in options:
            color[v] = d
            if solve(color):
                return True
            color[v] = 0                 # undo (backtrack)
        return False                     # dead end

## 4. Complexity

- Graph construction: O(81²), a constant for a fixed 9×9 board.
- Worst case search: exponential, since Sudoku (generalized to n×n) is NP-complete.
- In practice the MRV heuristic prunes the search heavily. Typical 9×9 puzzles are solved in milliseconds.

## 5. Sample Cases

| Case | Expected | Notes |
|---|---|---|
| Puzzle from lecture slide | Success | ~1661 tries. The clues allow more than one solution, so the output may differ from the slide. |
| Classic easy puzzle | Success | 51 tries |
| Empty grid | Success | Finds one of many valid solutions |
| Two 5s in the same row | Fail | Invalid clues, detected before searching |
| Row 1 has 1-8, column 9 has a 9 | Fail | Clues are consistent, but cell (r1,c9) has no available color, so no solution exists |

The last two cases show two kinds of failure: invalid input versus a search with no solution.

## 6. How to Run

    python3 sudoku_coloring.py

The program prints each puzzle, then either the solved grid or the reason it failed.

---

# Transportation Problem Solver using Vogel's Approximation Method (VAM)

An interactive Python implementation designed to solve arbitrary $m \times n$ balanced **Transportation Problems** using **Vogel's Approximation Method (VAM)**. This program calculates the optimal Initial Basic Feasible Solution (IBFS), determines allocated commodity quantities across supplier-customer routes, and computes the total minimum transportation cost.

---

## 1. Project Overview

In operations research and graph theory (specifically bipartite matching and network flow), the **Transportation Problem (TP)** deals with distributing a single commodity from several sources/suppliers to several destinations/demands in such a way that:

- Each supplier's capacity constraint is strictly satisfied.
- Each customer's demand requirement is fully met.
- The total global transportation cost across all active edges is minimized.

This application provides a simple command-line interface that accepts dynamic matrix sizes ($3 \times 4$, $4 \times 4$, $5 \times 5$, $7 \times 7$, etc.) without hardcoded limits, outputs the resulting allocation matrix, and details every active route.

---

## 2. Algorithm 

While classic methods such as the **Northwest Corner Method (NCM)** and the **Least Cost Method (LCM)** find basic feasible solutions quickly, **Vogel's Approximation Method (VAM)** is an advanced heuristic that yields solutions very close to (and often identical to) the global optimal solution.

### How VAM Works: Penalty-Based Allocation

VAM operates on the principle of **opportunity cost** or **penalty cost**:

1. **Calculate Penalties:**
   - For every active row, find the difference between the **two lowest costs**.
   - For every active column, find the difference between the **two lowest costs**.
   - *Intuition:* A higher penalty means failing to allocate to the cheapest cell in that row/column will incur a high cost penalty by forcing an allocation to a more expensive route.

2. **Select Maximum Penalty:**
   - Identify the row or column with the largest penalty value across the entire matrix.

3. **Greedy Allocation:**
   - In that selected row or column, identify the cell with the absolute lowest unit transportation cost.
   - Allocate as much commodity as possible to this cell:
     $$\text{Allocated Units} = \min(\text{Remaining Supply}, \text{Remaining Demand})$$

4. **Update & Eliminate:**
   - Subtract the allocated quantity from both the corresponding supply and demand.
   - Deactivate (cross out) the row if its supply reaches 0, or the column if its demand reaches 0.

5. **Iterate:**
   - Repeat Steps 1 through 4 on remaining active cells until all supplies and demands are fully exhausted.

6. **Compute Total Cost:**
   
   $$\text{Total Cost} = \sum_{i=1}^{m} \sum_{j=1}^{n} (\text{Allocated Units}_{ij} \times \text{Unit Cost}_{ij})$$

---

## 3. Prerequisites & Installation

### Requirements
- **Python 3.8+**
- **NumPy**

### Installation
Open your terminal or command prompt and install NumPy:
```bash
pip install numpy
```

---

## 4. How to Run the Code

1. Download the code/ copy and paste the code to your own compiler
2. Run the code
3. Enter the dimensions (number of suppliers and customers).
4. Enter the cost values row by row (space-separated).
5. Enter the supply list and demand list (space-separated).

---

## 5. Sample Inputs & Test Cases

### Sample Input 1: 

- **Number of suppliers:** `3`
- **Number of customers:** `4`

**Cost Matrix (Row by Row):**
```bash
19 30 50 10
70 30 40 60
40 8 70 20
```

**Supply Values:**
```bash
70 90 140
```

**Demand Values:**
```bash
50 80 70 100
```

**Sample output 1:**

<img width="343" height="238" alt="image" src="https://github.com/user-attachments/assets/24ee58a4-381c-4366-ab1a-7c2ae3466766" />

---

### Sample Input 2: 

- **Number of suppliers:** `4`
- **Number of customers:** `4`

**Cost Matrix (Row by Row):**
```bash
90 75 75 80
35 85 55 65
125 95 90 105
45 110 95 115
```

**Supply Values:**
```bash
15 25 10 20
```

**Demand Values:**
```bash
20 10 15 25
```

**Sample Output 2:**

<img width="343" height="225" alt="image" src="https://github.com/user-attachments/assets/f60b7f17-9f3d-4242-8ebf-3ceafb02fd50" />


---

### Sample Input 3: 
- **Number of suppliers:** `5`
- **Number of customers:** `5`

**Cost Matrix (Row by Row):**
```bash
12 13 4 6 10
8 11 15 9 5
6 7 8 14 12
10 9 6 11 8
14 5 10 7 11
```

**Supply Values:**
```bash
100 150 120 80 50
```

**Demand Values:**
```bash
90 110 130 70 100
```

**Sample Output 3:**

<img width="337" height="322" alt="image" src="https://github.com/user-attachments/assets/440cf483-de52-47b4-9e04-218e7c889952" />


---

AI Usage disclosure:
https://claude.ai/share/63f4fe88-00c8-4c94-a4ab-b04c36938809
https://share.gemini.google/Dp4gbkIV948U
