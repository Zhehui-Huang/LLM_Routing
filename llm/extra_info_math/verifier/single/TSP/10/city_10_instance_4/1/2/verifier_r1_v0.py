import math

# Given cities and the optimal tour
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
tour = [3, 6, 2, 8, 9, 1, 5, 7, 4, 0, 3, 0]
reported_cost = 338.5984032397796

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Check if the tour starts and ends at the depot city (0)
def check_start_end_depot(tour):
    return tour[0] == 0 and tour[-1] == 0

# Check if each city except depot is visited exactly once
def check_visit_once(tour):
    city_visit = {k: 0 for k in cities.keys()}
    for city in tour:
        city_visit[city] += 1
    city_visit.pop(0, None)  # Remove depot city check for multiple visits
    return all(v == 1 for v in city_visit.values())

# Check the total travel cost
def check_total_travel_cost(tour, reported_cost):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += distance(tour[i], tour[i + 1])
    return math.isclose(total_cost, reported_cost, rel_tol=1e-9)

# Check for no subtours within the tour (not implemented in this strict checker)
# Implement subtour checking logic if necessary. Since TSP solution should form a single tour, we skip here.

# Run the unit tests to verify the solution
def verify_solution(tour, reported_cost):
    return (
        "CORRECT"
        if all([
            check_start_end_depot(tour),
            check_visit_once(tour),
            check_total_travel_cost(tour, reported_cost)
        ])
        else "FAIL"
    )

# Output the result of verifying the TSP solution
print(verify_solution(tour, reported_cost))