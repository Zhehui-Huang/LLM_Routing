import numpy as  np

def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def total_distance(tour, coords):
    dist = 0
    for i in range(1, len(tour)):
        dist += euclidean_distance(coords[tour[i-1]], coords[tour[i]])
    dist += euclidean_distance(coords[tour[-1]], coords[tour[0]])
    return dist

def two_opt(tour, coords):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour)-1):
            for j in range(i+1, len(tour)):
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if total_distance(new_tour, coords) < total_distance(tour, coords):
                    tour = new_tour
                    improvement = True
    return tour

# Coordinates of the cities including the depot
coords = [
    (3, 26), (85, 72), (67, 0), (50, 100), (61, 89), (91, 56), (2, 65),
    (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49),
    (18, 49), (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Initial tour (sequential order)
initial_tour = list(range(len(coords)))

# Apply 2-opt algorithm
optimized_tour = two_opt(initial_tour, coords)
optimized_tour.append(optimized_tour[0]) # Closing the loop

# Calculate the total travel cost
cost = total_distance(optimized_tour, coords)

print("Tour:", optimized_tour)
print("Total travel cost:", cost)