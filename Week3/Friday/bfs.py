def bfs(graph, start, end):
    visited = set()
    queue = []
    path_to = {}  # path_to[x] = y
    # if we go to x through y

    visited.add(start)
    queue.append(start)
    path_to[start] = None
    found = False
    path_length = 0

    while len(queue) != 0:
        current_node = queue.pop(0)
        if current_node == end:
            found = True
            break

        for neighbour in graph[current_node]:
            if neighbour not in visited:
                # in order to go to neighbour, we've gone through current_node
                path_to[neighbour] = current_node
                visited.add(neighbour)
                queue.append(neighbour)

    if found:
        # path_to[end] becomes "None" when we reach the start
        while path_to[end] is not None:
            path_length += 1
            end = path_to[end]

    return path_length


graph = {
    "1": ["2", "3", "5"],
    "2": ["4", "1"],
    "3": ["1", "6"],
    "4": ["2", "5", "6"],
    "5": ["4", "1"],
    "6": ["3", "4", "7"],
    "7": ["6", "8"],
    "8": ["7", "9"],
    "9": ["8", "10"],
    "10": ["9"],
    "11": ["12"],
    "12": ["11"]
}

print(bfs(graph, "1", "6"))
