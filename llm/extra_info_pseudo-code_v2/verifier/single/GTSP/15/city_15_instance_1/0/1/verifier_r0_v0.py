import math

def euclidean_distance(city1, city2):
    return round(math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2), 2)

def verify_solution(tour, total_cost):
    # City coordinates indexed by city indices
    cities = [
        (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
        (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
        (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
    ]
    
    # City groups each city belongs to
    groups = [
        [1, 2, 5, 6], [8, 9, 10, 13], [3, 4, 7], [11, 12, 14]
    ]
    
    def validate_city_count():
        return len(cities) == 15
    
    def validate_start_end_depot():
        return tour[0] == 0 and tour[-1] == 0
    
    def validate_one_city_per_group():
        selected = set(tour[1:-1])
        for group in groups:
            if len(selected.intersection(group)) != 1:
                return False
        return True
    
    def validate_travel_cost():
        computed_cost = 0
        for i in range(len(tour) - 1):
            computed_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        return round(computed_cost, 2) == total_cost
    
    if all([validate_city_count(), validate_start_end_depot(), 
            validate_one_city_per_group(), validate_travel_cost()]):
        return "CORRECT"
    else:
        return "FAIL"

# Solution provided
solution_tour = [0, 5, 10, 4, 11, 0]
solution_total_cost = 184.24

# Invoke the test
print(verify_solution(solution_tour, solution_total_cost))