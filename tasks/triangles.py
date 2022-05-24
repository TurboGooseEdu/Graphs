# returns a number of triangles for every vertex
def triangles(graph):
    vert_triangles = {}
    for vertex in graph.adj:
        vert_triangles[vertex] = 0

    for vertex in graph.adj:
        for adj_vert in graph.adj[vertex]:
            if adj_vert < vertex:
                continue
            for adj_to_adj in graph.adj[adj_vert]:
                if adj_to_adj in graph.adj[vertex] and adj_to_adj > adj_vert:
                    vert_triangles[vertex] += 1
                    vert_triangles[adj_vert] += 1
                    vert_triangles[adj_to_adj] += 1
    return vert_triangles


# closed_triplets - 3 vertexes with 3 edges between them
# triplets - 3 vertexes with at least 2 edges between them

# local clustering coefficients
# =
# closed_triplets_for_vert / triplets_for_vert
# closed_triplets_for_vert = the number of triangles containing this vertex
def local_clustering(graph, vert_triangles=None):
    if vert_triangles is None:
        vert_triangles = triangles(graph)

    local_coefficients = {}

    for vertex in graph.adj:
        vert_pow = len(graph.adj[vertex])

        local_coefficients[vertex] = 0
        if vert_pow > 1:
            triplets_doubled_vert = vert_pow * (vert_pow - 1)
            local_coefficients[vertex] = 2 * vert_triangles[vertex] / triplets_doubled_vert

    return local_coefficients


# average clustering coefficient
# =
# sum_for_each_vert(local_clustering_coefficient) / the_number_of_vertexes
def average_clustering(graph, local_coefficients=None, vert_triangles=None):
    if local_coefficients is None:
        if vert_triangles is None:
            vert_triangles = triangles(graph)

        local_coefficients = local_clustering(graph, vert_triangles)

    return sum(local_coefficients.values()) / graph.v


# global clustering coefficient
# =
# closed_triplets_number / triplets_number
# =
# total_triangles_number * 3 / triplets_number
# =
# total_triangles_number * 3 / sum_for_each_vert(pow * (pow-1) / 2)
# =
# total_triangles_number * 6 / sum_for_each_vert(pow * (pow-1))
def global_clustering(graph, vert_triangles=None):
    if vert_triangles is None:
        vert_triangles = triangles(graph)

    closed_triplets = sum(vert_triangles.values())

    triplets_doubled_total = 0

    for vertex in graph.adj:
        vert_pow = len(graph.adj[vertex])

        # the doubled number of all triplets for current vertex
        triplets_doubled_vert = 0

        if vert_pow > 1:
            triplets_doubled_vert = vert_pow * (vert_pow - 1)
        triplets_doubled_total += triplets_doubled_vert
    triplets = triplets_doubled_total / 2
    return closed_triplets / triplets


def all_clustering(graph, vert_triangles=None):
    if vert_triangles is None:
        vert_triangles = triangles(graph)

    closed_triplets = sum(vert_triangles.values())

    local_coefficients = {}
    average_coefficient = 0
    triplets = 0

    for vertex in graph.adj:
        vert_pow = len(graph.adj[vertex])

        # the doubled number of opened triplets for current vertex
        triplets_vert = 0

        local_coefficients[vertex] = 0
        if vert_pow > 1:
            triplets_vert = vert_pow * (vert_pow - 1) / 2
            local_coefficients[vertex] = vert_triangles[vertex] / triplets_vert
        triplets += triplets_vert

        average_coefficient += local_coefficients[vertex]

    average_coefficient /= graph.v  # graph.v - the number of vertexes
    global_coefficient = closed_triplets / triplets

    print(f'triangles = {vert_triangles}')
    print(f'local_coefficients = {local_coefficients}')
    print(f'average_coefficient = {average_coefficient}')
    print(f'global_coefficient = {global_coefficient}')
