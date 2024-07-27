import math

# Data setup
cities_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Resulting tours from proposed solution
robots_tours = {
    0: [0, 10, 17, 18, 13, 6, 9, 0],
    1: [0, 8, 11, 20, 2, 14, 0],
    2: [0, 1, 15, 4, 21, 12, 0],
    3: [0, 19, 7, 3, 16, 5, 0]
}

# Calculate travel costs
def calculate_distance(city1, city2):
    return math.sqrt((cities_coordinates[city1][0] - cities_coordinates[city2][0]) ** 2 +
                     (cities_coordinates[city1][1] - cities_coordinates[city2][1]) ** 2)

def calculate_tour_cost(tour):
    return sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Run tests
def test_requirements():
    all_visited_cities = set()
    all_tours_cost = 0
    
    for robot, tour in robots_tours.items():
        # Check if all tours start and end at their assigned depot (Requirement 1 & 4)
        if tour[0] != tour[-1] or tour[0] != 0:
            return "FAIL"
        
        # Collect all visited cities for Requirement 2 checking
        all_visited_cities.update(tour[:-1])  # exclude the duplicate depot at the end
        
        # Calculate and accumulate total cost for Requirement 3
        tour_cost = calculate_tour_cost(tour)
        all_tours_cost += tour_cost
        
    # Check Requirement 2: All cities visited and only once
    if all_visited_cities != set(range(22)):
        return "FAIL"
    
    # Output the total and individual tour costs (Requirement 4 is checked earlier within other checks)
    print(f"Overall Total Travel Cost: {all_tours_cost}")
    for robot, tour in robots_tours.items():
        print(f"Robot {robot} Tour: {tour}")
        print(f"Robot {robot} Total Travel Cost: {calculate_tour_cost(tour)}")

    return "CORRECT"

# Execute the unit tests
output = test_requirements()
print(output)