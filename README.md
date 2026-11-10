# ITS Graph Theory class Group 5 Assignment 10

Group 5 Members:

- Maulana Anugra Putra/5025251159 (kukii83)

- I Gusti Agung Candra Nugraha/5025251169 (candranugraha576)

- Hussein Mohammad Mahsun/5025251170 (TheDelightOFice)

---

In this project, we will be basing our programs based on two materials:

- Coloring 
- Matching


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

## 2. Algorithm Used: Vogel's Approximation Method (VAM)

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
