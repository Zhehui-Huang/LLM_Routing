import math

# Define city coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Total cost of a given tour
def total_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Basic 2-opt heuristic for optimizing tour
def optimize_two_opt(tour):
    improvement = True
    while improvement:
        improvement = False
        for i in range(1, len(tour) - 2):
            for j in range(i+1, len(tour)):
                if j - i == 1: continue  # Consecutive edges, no point in swapping them
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if total_cost(new_tour) < total_cost(tour):
                    tour = new_tour
                    improvement = True
        return tour

# Initial tour (simple nearest neighbor heuristic)
current_city = 0
unvisited = set(cities.keys())
unvisited.remove(current_city)
tour = [current_city]

while unvisited:
    next_city = min(unvisited, key=lambda city: distance(current_city, city))
    tour.append(next_city)
    current_city = next_city
    unvisited.remove(current_NONEity)

tour.append(0)  # Return to the depot
optimized_tour = optimize_two_opt(tour)

# Compute the final cost
final_cost = total_cost(optimized_tour)

# Print the output in the required format
print("Tour:", optimized_tour)
print("Total travel cost:", round(final_cost, 2))