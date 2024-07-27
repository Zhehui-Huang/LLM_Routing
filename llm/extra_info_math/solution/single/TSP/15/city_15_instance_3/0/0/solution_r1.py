import pulp
import math

def run_tsp_solver():
    # Define the cities and their coordinates
    cities = {
        0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
        5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
        10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
    }
    
    n = len(cities)
    
    # Euclidean distance calculation
    def distance(city1, city2):
        return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)
    
    # Create cost dictionary
    costs = {(i, j): distance(cities[i], cities[j]) for i in cities for j in cities if i != j}
    
    # Problem formulation
    prob = pulp.LpProblem("TSP", pulp.LpMinimize)
    
    # Variables
    x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')
    
    # Objective
    prob += pulp.lpSum(costs[i, j] * x[i, j] for i in cities for j in cities if i != j)
    
    # Constraints
    for i in cities:
        prob += pulp.lpSum(x[j, i] for j in cities if j != i) == 1  # entering a city
        prob += pulp.lpSum(x[i, j] for j in cities if i != j) == 1  # leaving a city
    
    # Solve TSP
    prob.solve()

    # Ensuring a feasible solution exists
    if pulp.LpStatus[prob.status] != 'Optimal':
        print("Failed to find an optimal solution.")
        return
    
    # Extract the tour from the variables
    tour = [0]
    current_city = 0
    while True:
        next_cities = [j for j in cities if j != current_city and pulp.value(x[current_city, j]) == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        tour.append(next_city)
        current_city = next_mapping
    
    # Ensure the tour ends at the starting city (depot)
    tour.append(0)
    
    # Calculate the tour cost
    total_cost = sum(costs[tour[i], tour[i+1]] for i in range(len(tour) - 1))
    
    # Results
    print("Tour:", tour)
    print("Total travel cost:", total_cost)

# Run the defined function to solve the TSP
run_tsp_solver()