import numpy as np

# Constants
num_cities = 22
num_robots = 4
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), 
    (128, 252), (163, 247), (146, 246), (161, 242),
    (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), 
    (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Calculate Euclidean distance
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Nearest neighbor search for initial solution
def nearest_neighbor():
    remaining_cities = set(range(1, num_cities))  # Exclude depot 0
    tours = [[0] for _ in range(num_robots)]  # Start each robot at depot 0
    
    # Distribute cities to each robot's tour
    while remaining_cities:
        for tour in tours:
            if not remaining_cities:
                break
            last_city = tour[-1]
            next_city = min(remaining_cities, key=lambda city: distance(last_city, city))
            tour.append(next_city)
            remaining_cities.remove(next_city)
    
    return tours

# Calculate travel cost of a tour
def calculate_tour_cost(tour):
    return sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Initialize solution
tours = nearest_neighbor()
total_costs = [calculate_tour_cost(tour) for tour in tours]
overall_cost = sum(total_costs)

# Output results
for idx, tour in enumerate(tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {total_costs[idx]:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")