import math

# Define the positions of each city
city_positions = [
    (84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31),
    (8, 62), (74, 56), (85, 71), (6, 76)
]

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_distance(tour):
    """Calculate the total distance of the tour."""
    return sum(euclidean_distance(city_positions[tour[i]], city_positions[tour[i+1]]) for i in range(len(tour)-1))

def nearest_neighbour_tour(start=0):
    """Generate an initial tour using the nearest neighbour heuristic."""
    remaining = set(range(1, len(city_positions)))  # Cities excluding the depot
    tour = [start]
    while remaining:
        last = tour[-1]
        next_city = min(remaining, key=lambda city: euclidean_distance(city_positions[last], city_positions[city]))
        tour.append(next_city)
        remaining.remove(next_city)
    tour.append(start)  # To return to the depot in the end
    return tour

def two_opt(tour):
    """Attempt to improve the tour by consecutively applying 2-opt swaps."""
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour)-2):
            for j in range(i+1, len(tour)-1):
                if j-i == 1:
                    continue  # Ignore trivial swaps
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                if calculate_total_distance(new_tour) < calculate_total_distance(tour):
                    tour = new_tour
                    improved = True
        if not improved:
            break
    return tour

# Start the TSP solution
initial_tour = nearest_neighbour_tour()
optimized_tour = two_opt(initial_tour)
total_travel_cost = calculate_total_distance(optimized_tour)

print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {total_travel_cost}")