import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_tour(tour, cities):
    # Requirements
    starts_at_depot = tour[0] == 0 and tour[-1] == 0
    visits_each_city_once = len(set(tour)) == len(cities) and len(tour) == len(cities) + 1
    follows_tour_order = all(tour[i] in cities.keys() for i in range(len(tour)))
    
    return starts_at_depot and visits_each_city_once and follows_tour_order

def validate_costs(tour, cities, claimed_total_cost, claimed_max_distance):
    total_cost = 0
    max_distance = 0
    valid_costs = True
    
    for i in range(len(tour)-1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance

    total_cost = round(total_cost, 2)
    max_distance = round(max_distance, 2)

    return math.isclose(total_cost, claimed_total_cost, rel_tol=1e-5) and math.isclose(max_distance, claimed_max_distance, rel_tol=1e-5)

def main():
    cities = {
        0: (50, 42),
        1: (41, 1),
        2: (18, 46),
        3: (40, 98),
        4: (51, 69),
        5: (47, 39),
        6: (62, 26),
        7: (79, 31),
        8: (61, 90),
        9: (42, 49),
    }
    solution_tour = [0, 1, 5, 2, 4, 3, 8, 9, 6, 7, 0]
    total_travel_cost = 328.40
    max_distance = 45.19
    
    if not validate_tour(solution_tour, cities):
        print("FAIL")
        return

    if not validate_costs(solution_tour, cities, total_travel_cost, max_distance):
        print("FAIL")
        return

    print("CORRECT")

if __name__ == "__main__":
    main()