import numpy as np

def vogel_approximation(costs, supply, demand):
    costs = np.array(costs, dtype=float)
    supply = np.array(supply, dtype=float)
    demand = np.array(demand, dtype=float)
    
    m, n = costs.shape
    alloc = np.zeros((m, n), dtype=float)
    
    row_active = np.ones(m, dtype=bool)
    col_active = np.ones(n, dtype=bool)
    
    while np.any(row_active) and np.any(col_active):
        row_pen = []
        col_pen = []
        
        # Calculate row penalties
        for i in range(m):
            if not row_active[i]:
                row_pen.append(-1)
                continue
            active = costs[i, col_active]
            row_pen.append(active[0] if len(active) == 1 else np.diff(np.sort(active)[:2])[0])
            
        # Calculate column penalties
        for j in range(n):
            if not col_active[j]:
                col_pen.append(-1)
                continue
            active = costs[row_active, j]
            col_pen.append(active[0] if len(active) == 1 else np.diff(np.sort(active)[:2])[0])
            
        # Select target cell with maximum penalty
        if max(row_pen) >= max(col_pen):
            r = int(np.argmax(row_pen))
            active_cols = np.where(col_active)[0]
            c = active_cols[np.argmin(costs[r, active_cols])]
        else:
            c = int(np.argmax(col_pen))
            active_rows = np.where(row_active)[0]
            r = active_rows[np.argmin(costs[active_rows, c])]
            
        # Allocate quantity
        qty = min(supply[r], demand[c])
        alloc[r, c] = qty
        supply[r] -= qty
        demand[c] -= qty
        
        # Deactivate satisfied row or column
        if supply[r] == 0:
            row_active[r] = False
        else:
            col_active[c] = False
            
    total_cost = np.sum(alloc * costs)
    return alloc, total_cost


def print_route_summary(allocations, costs, num_suppliers, num_customers):
    print("\n=== Matched Transportation Routes ===")
    for i in range(num_suppliers):
        for j in range(num_customers):
            if allocations[i][j] > 0:
                qty = int(allocations[i][j])
                cost_per_unit = int(costs[i][j])
                subtotal = qty * cost_per_unit
                print(f"Supplier {i+1} -> Customer {j+1}: {qty} units @ {cost_per_unit} = {subtotal}")


# ==========================================
# Main Execution Entry Point
# ==========================================
if __name__ == "__main__":
    print("=== Enter Table Dimensions ===")
    num_suppliers = int(input("Enter number of suppliers: "))
    num_customers = int(input("Enter number of customers: "))
    
    print("\n--- Enter Cost Matrix ---")
    costs = []
    for i in range(num_suppliers):
        row = input(f"Cost from Supplier {i+1} to all {num_customers} customers (separated by space): ")
        costs.append([float(x) for x in row.split()])
        
    print("\n--- Enter Capacities & Demands ---")
    supply_input = input(f"Supply for {num_suppliers} suppliers (separated by space): ")
    supply = [float(x) for x in supply_input.split()]
    
    demand_input = input(f"Demand for {num_customers} customers (separated by space): ")
    demand = [float(x) for x in demand_input.split()]
    
    # Run VAM solver
    alloc, total_cost = vogel_approximation(costs, supply, demand)
    
    print("\n=== Optimal Allocation Matrix ===")
    print(alloc.astype(int))
    
    # Print clean text summary of all matched routes
    print_route_summary(alloc, costs, num_suppliers, num_customers)
    
    print(f"\nTotal Transportation Cost: {int(total_cost)}")