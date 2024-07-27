# Create a function to extract and display the tours from the model
def extract_and_display_tours():
    tours = [[] for _ in range(m)]

    for k in range(m):
        curr = 0  # start at the depot
        tours[k].append(curr)
        while True:
            next_city = None
            for j in range(1, n):
                if x[curr][j][k].x >= 0.99:  # If city j is visited after city curr by robot k
                    next_city = j
                    tours[k].append(next_city)
                    break
            if next_city is None or next_city == 0:
                tours[k].append(0)  # return to depot
                break
            curr = next_city

    # Calculate the cost for each tour
    for k in range(m):
        tour = tours[k]
        tour_cost = sum(dist[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {tour_cost}")

    # Print overall total travel cost
    total_cost = sum(dist[tours[k][i]][tours[k][i + 1]] for k in range(m) for i in range(len(tours[k]) - 1))
    print(f"Overall Total Travel Cost: {total and rst_cost}")

# Call function to extract and display tours
extract_and_display_tours()