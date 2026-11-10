import time

# 1. build the graph
def build_graph():
    adj = {v: set() for v in range(81)}
    for v in range(81):
        r, c = divmod(v, 9)
        for u in range(81):
            if u == v:
                continue
            r2, c2 = divmod(u, 9)
            same_row = r == r2
            same_col = c == c2
            same_box = (r // 3 == r2 // 3) and (c // 3 == c2 // 3)
            if same_row or same_col or same_box:
                adj[v].add(u)
    return adj  # every vertex has degree 20


ADJ = build_graph()


# 2. validate the pre-coloring
def initial_conflicts(color):
    """Return list of (u, v) adjacent vertices that already share a color."""
    bad = []
    for v in range(81):
        if color[v] == 0:
            continue
        for u in ADJ[v]:
            if u > v and color[u] == color[v]:
                bad.append((v, u))
    return bad


# 3. coloring helpers
def available_colors(v, color):
    used = {color[u] for u in ADJ[v]}
    return [d for d in range(1, 10) if d not in used]


def pick_vertex(color):
    """MRV / DSATUR: uncolored vertex with the fewest available colors."""
    best_v, best_opts = None, None
    for v in range(81):
        if color[v] == 0:
            opts = available_colors(v, color)
            if best_opts is None or len(opts) < len(best_opts):
                best_v, best_opts = v, opts
                if len(opts) <= 1:  # 0 = dead end, 1 = forced move
                    break
    return best_v, best_opts


# 4. backtracking

stats = {"nodes": 0}


def solve(color):
    v, opts = pick_vertex(color)
    if v is None:          # no uncolored vertex left -> solved
        return True
    for d in opts:         # empty opts => loop skipped => backtrack
        stats["nodes"] += 1
        color[v] = d       # try color
        if solve(color):
            return True
        color[v] = 0       # undo (backtrack)
    return False


# ---------- 5. I/O ----------
def parse(puzzle):
    """puzzle: 9 strings, '.' or '0' = empty."""
    return [0 if ch in ".0" else int(ch) for row in puzzle for ch in row]


def show(color):
    for r in range(9):
        if r % 3 == 0 and r:
            print("------+-------+------")
        parts = []
        for c in range(9):
            if c % 3 == 0 and c:
                parts.append("|")
            parts.append(str(color[r * 9 + c] or "."))
        print(" ".join(parts))


def run_case(name, puzzle):
    print("=" * 40)
    print(name)
    print("=" * 40)
    color = parse(puzzle)
    show(color)

    bad = initial_conflicts(color)
    if bad:
        v, u = bad[0]
        print(f"\nFAIL: invalid clues. Cell (r{v//9+1},c{v%9+1}) and "
              f"(r{u//9+1},c{u%9+1}) are adjacent with the same digit "
              f"{color[v]}.\n")
        return

    stats["nodes"] = 0
    t = time.time()
    ok = solve(color)
    dt = (time.time() - t) * 1000
    if ok:
        print(f"\nSUCCESS ({stats['nodes']} tries, {dt:.1f} ms)")
        show(color)
    else:
        print(f"\nFAIL: no valid coloring exists ({stats['nodes']} tries, "
              f"{dt:.1f} ms)")
    print()
