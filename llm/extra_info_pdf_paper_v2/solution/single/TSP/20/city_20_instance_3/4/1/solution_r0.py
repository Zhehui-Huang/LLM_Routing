import math

# City coordinates indexed by city number
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

def calc_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def total_distance(tour):
    return sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

def find_initial_tour():
    unvisited = set(range(1, len(coordinates)))  # Cities without the depot city 0
    tour = [0]  # Start at depot city
    current = 0
    while unvisited:
        next_city = min(unvisited, key=lambda city: calc_distance(current, city))
        tour.append(next_city)
        current = next_city
        unvisited.remove(next_city)
    tour.append(0)  # Return to depot
    return tour

def two_opt_swap(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour) - 1):
                if calc_distance(tour[i - 1], tour[i]) + calc_distance(tour[j], tour[j + 1]) > \
                   calc_distance(tour[i - 1], tour[j]) + calc_distance(tour[i], tour[j + 1]):
                    tour[i:j+1] = reversed(tour[i:j+1])
                    improved = True
                    break
            if improved:
                break
    return tour

# Finding the tour
initial_tour = find_initial_tour()
improved_tour = two_opt_swap(initial_tour)
tour_cost = total_distance(improved_tour)

print(f"Tour: {improved_tour}")
print(f"Total travel cost: {tour_cost:.2f}")