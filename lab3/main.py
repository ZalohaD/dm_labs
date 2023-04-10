import itertools

def read_data(file_path):
    with open(file_path, 'r') as file:
        n = int(file.readline().strip())
        data = [[int(x) for x in line.strip().split()] for line in file]
    return n, data

def tsp(n, distances):
    cities = range(n)
    min_distance = float('inf')
    for path in itertools.permutations(cities):
        distance = sum(distances[path[i]][path[i+1]] for i in range(n-1))
        distance += distances[path[-1]][path[0]]
        if distance < min_distance:
            min_distance = distance
            best_path = path
    return min_distance, best_path

if __name__ == '__main__':
    n, distances = read_data('data.txt')
    min_distance, best_path = tsp(n, distances)
    print(f'Minimum distance: {min_distance}')
    print(f'Best path: {best_path}')