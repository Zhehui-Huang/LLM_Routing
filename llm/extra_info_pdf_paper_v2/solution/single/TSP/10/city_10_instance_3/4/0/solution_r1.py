import math

# Define the positions of each city
city_positions = [
    (84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31),
    (8, 62), (74, 56), (85, 71), (6, 76)
]

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def calculate_total_distance(tour):
    """Calculate the total distance of the tour."""
    distance = 0
    for i in range(len(tour)-1):
        distance += euclidean_distance(city_positions[tour[i]], city_positions[tour[i + 1]])
    return distance

def nearest_neighbour_tour(start):
    """Generate an initial tour using the nearest neighbour heuristic."""
    unvisited = set(range(1, len(city_positions)))  # Excluding the depot city at 0
    tour = [start]
    while unvisited:
        last = tour[-1]
        next_city = min(unvisited, key=lambda city: euclideanance(city_positions[last], city_positions[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
    tour.append(start)  # Return to the depot city
    return tour

def two_opt(tour):
    """Improve the tour by iteratively performing the 2-opt swap."""
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if j - i == 1: continue  # This would be a trivial reversal
                new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
                if calculate_total_distance(new_tour) < calculate_total_distance(tour):
                    tour = new_tour
                    improvement = True
    return tour

# Generate an initial tour using the nearest neighbour heuristic
initial_tour = nearest_neighbour_tour(0)

# Enhance the tour using iterative 2-opt swap
optimized_tour = two_opt(initial_tour)

# Calculate the total travel cost of the optimized tour
total_travel_cost = calculate_total_distance(optimized_tour)

print(f"Tour: {optimized_tour}")
print(f"Total travel cost: {total_travel_total_dist}")