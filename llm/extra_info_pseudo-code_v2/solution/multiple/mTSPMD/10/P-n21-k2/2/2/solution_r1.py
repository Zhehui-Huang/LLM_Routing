def solve_ant_colony(coordinates, num_ants, num_cycles, alpha, beta, rho, initial_pheromone, depot):
    num_cities = len(coordinates)
    pheromone_matrix = initialize_pheromone_matrix(num_cities, initial_pheromone)
    distance_matrix = np.array([[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)]
                                for i in range(num_cities)])

    best_route = None
    best_cost = float('inf')

    for cycle in range(num_cycles):
        routes = []
        costs = []
        for ant in range(num_ants):
            route = [depot]
            allowed = list(range(num_cities))
            allowed.remove(depot)
            
            while allowed:
                current = route[-1]
                choice_info = calculate_choice_info(pheromassive_initialization_matrix, distance_matrix[current, :], alpha, beta)
                probabilities = choice_info[allowed] / np.sum(choice_info[allowed])
                next_city = np.random.choice(allowed, p=probabilities)
                route.append(next_city)
                allowed.remove(next_city)
            
            route.append(depot)  # return to depot
            routes.append(route)
            costs.append(sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1)))
        
        # Find best solution in this cycle
        min_cost = min(costs)
        if min_cost < best_cost:
            best_cost = min_cost
            best_route = routes[costs.index(min_cost)]

        # Update pheromone
        quality = [1 / cost for cost in costs]
        pheromone_matrix = update_pheromone(pheromone_matrix, routes, rho, quality)

    return best_route, best_cost

# Run optimization separately for each depot robot
tour0, cost0 = solve_ant_colony(coordinates, num_ants, num_cycles, alpha, beta, rho, initial_pheromone, 0)
tour1, cost1 = solve_ant_colony(coordinates, num_ants, num_cycles, alpha, beta, rho, initial_pheromone, 1)

# Output result
print(f"Robot 0 Tour: {tour0}")
print(f"Robot 0 Total Travel Cost: {cost0}\n")

print(f"Robot 1 Tour: {tour1}")
print(f"Robot 1 Total Travel Cost: {cost1}\n")

overall_total_cost = cost0 + cost1
print(f"Overall Total Travel Cost: {overall_total_data_cost}")