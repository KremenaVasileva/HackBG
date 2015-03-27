def reduce_file_path(path):
    path = path.replace('//', '/')
    while path.find('/..') != -1:
        index = path.find('/..')
        start = index
        while path[start - 1] != '/':
            start -= 1
        path = path[:start] + path[index + 3:]
    path = path.replace('/.', '')
    while path[-1] == '/' and len(path) > 1:
        path = path[:len(path) - 1]
    return path

print (reduce_file_path("//////"))
