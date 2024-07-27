# Optimal Tour Extraction, Parse the Best Solution, and Compute Costs
def parse_tour(chromosome):
    robots = []
    tour = []
    start = 0  # Depot city index is assumed based on the problem
    for node in chromosome:
        if node == -1:
            if tour:
                tour.append(start)  # return to start depot for that tour
                robots.append(tour)
                tour = [start]  # new tour starting from depot
        else:
            tour.append(node)
    if tour:
        tour.append(start)  # close last tour
        robots.append(tour)
    
    return robots

def calculate_tour_cost(tour):
    cost = 0
    for j in range(len(tour) - 1):
        cost += distance(cities[tour[j]], cities[tour[j + 1]])
    return cost

# Extract best_solution tours for each robot and compute costs
best_robot_tours = parse_tour(best_solution)
tour_costs = []
overall_total_travel_cost = 0

for i, robot_tour in enumerate(best_robot_tours):
    tour_cost = calculate_tour_cost(robot_tour)
    tour_costs.append(tour_cost)
    overall_total_travel_cost += tour_cost
    print(f"Robot {i} Tour: {robot_tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_travel_cost:.2f}")