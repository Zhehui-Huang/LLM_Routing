import numpy as np

# Coordinates of each city including depots
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Function to calculate Euclidean distance
def distance(c1, c2):
    x1, y1 = coordinates[c1]
    x2, y2 = coordinates[c2]
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Initialize tours for each robot staring from their depots
tours = [[0], [1]]  # Starting from respective depots 0 and 1

def generate_solution():
    cities_to_visit = list(range(2, len(coordinates)))  # Cities except depots
    np.random.shuffle(cities_to_visit)  # Shuffle to introduce randomness
    
    # split cities roughly equally
    half = len(cities_to_visit) // 2
    tours[0].extend(cities_to_visit[:half])
    tours[1].extend(cities_to_visit[half:])
    
    # Return to original depots
    tours[0].append(0)  
    tours[1].append(1)
    
    # Compute and print tours and costs
    total_cost = 0
    for i, tour in enumerate(tours):
        tour_cost = sum(distance(tour[j], tour[j+1]) for j in range(len(tour)-1))
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {tour_cost}")
        total_cost += tour_cost
        
    print(f"Overall Total Travel Cost: {total_cost}")

generate_solution()