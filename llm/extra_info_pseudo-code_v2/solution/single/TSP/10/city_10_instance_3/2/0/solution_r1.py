import math

# --- Distance calculation function ---
def euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

# --- Cities coordinates ---
coordinates = [
    (84, 67),  # Depot City 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

# --- Initial tour ---
# A very naive initial tour just picks cities in numerical order
initial_tour = list(range(len(coordinates)))

# --- Calculate tour cost ---
def calculate_tour_cost(tour, coordinates):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
    # Add return to depot cost
    total_cost += euclidean_distance(coordinates[tour[-1]], coordinates[0])
    return total_cost

# --- Improve Tour via swaps (2-opt technique) ---
def improve_tour(tour, coordinates):
    best_cost = calculate_tour_cost(tour, coordinates)
    best_tour = tour[:]
    improved = True
    
    while improved:
        improved = False
        for i in range(1, len(tour)-1):
            for j in range(i+1, len(tour)):
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                new_cost = calculate_tour_cost(new_tour, coordinates)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_tour = new_tour[:]
                    improved = True
    return best_tour, best_cost

best_tour, best_cost = improve_tour(initial_tour, coordinates)
best_tour.append(0)  # to complete the circuit back to depot

# --- Outputting the result ---
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")