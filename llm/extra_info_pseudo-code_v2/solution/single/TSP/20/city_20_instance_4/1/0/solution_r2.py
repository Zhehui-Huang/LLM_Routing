import math

# Define the cities coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Function to create an initial tour using the nearest neighbor approach
def create_initial_tour():
    unvisited = list(cities.keys())[1:]  # Excluding the depot city
    tour = [0]
    current_city = 0
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(current_city, x))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    tour.append(0)  # Return to the depot city
    return tour

# Function to calculate the total cost of a tour
def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Function to perform two-opt swaps
def two_opt_swap(tour, i, k):
    new_tour = tour[:i] + tour[i:k+1][::-1] + tour[k+1:]
    return new_tour

# Function to apply the two-opt improvement technique
def apply_two_opt(tour):
    improvement = True
    while improvement:
        improvement = False
        best_cost = calculate_tour_cost(tour)
        for i in range(1, len(tour) - 1):
            for k in range(i + 1, len(tour)):
                new_tour = two_opt_swap(tour, i, k)
                new_cost = calculate_tour_cost(new_tour)
                if new_cost < best_cost:
                    tour = new_tour
                    best_cost = new_cost
                    improvement = True
    return tour

# Generate initial tour and apply Two-Opt improvement
initial_tour = create_initial_tour()
improved_tour = apply_two_opt(initial_tour)
tour_cost = calculate_tour_cost(improved_tour)

# Print the optimal tour and the total travel cost
print("Tour:", improved_tour)
print("Total travel cost:", tour_cost)