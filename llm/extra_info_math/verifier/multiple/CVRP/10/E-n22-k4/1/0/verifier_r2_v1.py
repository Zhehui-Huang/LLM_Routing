def verify_solution(tours, demands, coordinates, capacity):
    visited_cities = set()

    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            print("Tours must start and end at the depot.")
            return "FAIL"
        
        demand_in_tour = 0
        tour_cost = 0.0
        
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            
            if city_to != 0:  # No need to consider depot to depot
                distance = calculate_distance(coordinates[city_from], coordinates[city_to])
                tour_cost += distance
                demand_in_tour += demands[city_to]
                visited_cities.add(city_to)
        
        if demand_in_tour > capacity:
            print(f"Demand in tour exceeds capacity: {demand_in_tour} > {capacity}")
            return "FAIL"

    if len(visited_cities) != len(demands) - 1:
        print("Not all cities were visited exactly once.")
        return "FAIL"

    return "CORRECT"