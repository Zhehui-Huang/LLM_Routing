import math

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ: return
        if self.rank[rootP] > self.rank[rootQ]:
            self.parent[rootQ] = rootP
        elif self.rank[rootP] < self.rank[rootQ]:
            self.parent[rootP] = rootQ
        else:
            self.parent[rootQ] = rootP
            self.rank[rootP] += 1

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def algorithm_bb(coords):
    n = len(coords)
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            dist = euclidean_distance(coords[i], coords[j])
            edges.append((dist, i, j))
    edges.sort()

    uf = UnionFind(n)
    E_BB = []

    for dist, u, v in edges:
        if uf.find(u) != uf.find(v) or len(E_BB) + 1 < n:
            uf.union(u, v)
            E_BB.append((dist, u, v))

    E_BB.sort(reverse=True)  # to find the maximum as the tree is already connected
    while True:
        max_edge = E_BB[0]
        new_uf = UnionFind(n)
        new_edges = E_BB[1:]
        for _, u, v in new_edges:
            if new_uf.find(u) != new_uf.find(v):
                new_uf.union(u, v)
        if all(new_uf.find(i) == new_uf.find(0) for i in range(n)):
            E_BB = new_edges
        else:
            break

    tour = [0]
    visited = set(tour)

    def find_next_city(current):
        for _, u, v in sorted(E_BB, key=lambda x: x[0]):
            if u == current and v not in visited:
                return v
            elif v == current and u not in visited:
                return u
        return None

    for _ in range(n-1):
        next_city = find_next_city(tour[-1])
        if next_city is not None:
            tour.append(next_city)
            visited.add(next_city)

    tour.append(0)  # return to starting point

    # Calculating stats
    total_cost = sum(euclidean_distance(coords[tour[i]], coords[tour[i + 1]]) for i in range(len(tour) - 1))
    max_distance = max(euclidean_distance(coords[tour[i]], coords[tour[i + 1]]) for i in range(len(tour) - 1))

    return tour, total_cost, max_distance

# Cities coordinates
city_coords = [
    (84, 67), (74, 40), (71, 13), (74, 82), (97, 28),
    (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)
]

tour, total_cost, max_distance = algorithm_bb(city_coords)
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")