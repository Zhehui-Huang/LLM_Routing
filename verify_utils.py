import re


def extract_solution_with_separation(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Split the content by double newlines to find separated chunks
    # chunks = content.split('\n\n')
    chunks = re.split(r'\n\s*\n', content)
    # Assuming the solution chunk is well defined and separated as indicated
    solution_chunk = ""
    for chunk in chunks:
        if "Robot" in chunk and "Tour" in chunk:
            solution_chunk = chunk
            break

    # Extract tours from the solution chunk
    tours = {}
    costs = {}
    final_cost = -1
    for line in solution_chunk.split('\n'):
        if line.startswith('Robot') and 'Tour' in line:
            parts = line.split(':')
            robot = parts[0].strip()
            tour = eval(parts[1].strip())
            tours[robot] = tour

        if line.startswith('Robot') and 'Cost' in line:
            parts = line.split(':')
            robot = parts[0].strip()
            if parts[1].strip() == 'inf':
                cost = float(1e9)
            else:
                cost = eval(parts[1].strip())
            costs[robot] = cost

        if line.startswith('Final cost'):
            parts = line.split(':')
            final_cost = eval(parts[1].strip())

    return tours, costs, final_cost
