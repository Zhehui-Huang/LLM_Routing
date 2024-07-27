def verify_solution(tours):
    # Let's define the number of cities including the depot (city 0)
    total_cities = 16  # from city 0 to city 15
    depot = 0
    
    # Check if each city is visited exactly once by any salesman
    visits = [0] * total_cities
    for tour in tours:
        for city in tour:
            if city != depot:
                visits[city] += 1
    
    # All cities except the depot should be visited exactly once
    if any(v != 1 for i, v in enumerate(visits) if i != depot):
        return "FAIL"
    
    # Flow conservation and each salesman leaving depot exactly once
    for tour in tours:
        # Check if tour starts and ends at depot
        if tour[0] != depot or tour[-1] != depot:
            return "FAIL"
        
        # Check if any city occurs more than once in the tour
        unique_cities = set(tour[1:-1])  # ignore depot at start and end
        if len(unique_cities) + 1 != len(tour[1:-1]):
            return "FAIL"
    
    # Binary and continuous variable checks are implicit in integer & correct indexing and consecutive visits in the tour lists

    return "CORRECT"

tours = [
    [0, 14, 9, 13, 8, 3, 12, 15, 11, 0],
    [0, 4, 0],
    [0, 10, 0],
    [0, 1, 0],
    [0, 6, 0],
    [0, 7, 0],
    [0, 2, 0],
    [0, 5, 0]
]

result = verify_solution(tours)
print(result)