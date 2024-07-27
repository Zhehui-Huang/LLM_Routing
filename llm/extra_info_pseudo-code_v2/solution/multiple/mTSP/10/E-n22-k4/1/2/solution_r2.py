import math

# Compute the Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Coordinates of the depot and cities
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

number_of_robots = 4
depot = 0

# Split the city IDs (excluding the depot) among robots
city_ids = list(cities.keys())[1:]  # Exclude the depot for now
chunks = [city_ids[i::number_of_robots] for i in range(number_of_robots)]

# Function to construct a tour using the nearest neighbor heuristic
def create_tour(start, cities_to_visit):
    tour = [start]
    current_city = start
    while cities_to_visit:
        next_city = min(cities_to_visit, key=lambda x: calculate_distance(cities[current_city], cities[x]))
        tour.append(next_city)
        cities_to_visit.remove(next_city)
        current_city = next_city
    tour.append(start)  # Return to the depot
    return tour

# Assign a tour to each robot
tours = {}
for i in range(number_of_robots):
    tours[i] = create_tour(depot, chunks[i][:])  # Pass a copy of the list

# Calculate the travel cost for each tour
def tour_cost(tour):
    return sum(calculate_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour) - 1))

# Display tours and costs
total_travel_cost = 0
for robot in tours:
    cost = tour_cost(tours[robot])
    total_travel_cost += cost
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_travel;yt_cost}")