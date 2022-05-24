def triangles(graph):
    # counting a number of triangles for every vertex
    total_triangles = 0
    vert_triangles = {}
    for vertex in graph.adj:
        vert_triangles[vertex] = 0

    for vertex in graph.adj:
        for adj_vert in graph.adj[vertex]:
            if adj_vert < vertex:
                continue
            for adj_to_adj in graph.adj[adj_vert]:
                if adj_to_adj in graph.adj[vertex] and adj_to_adj > adj_vert:
                    print(vertex, adj_vert, adj_to_adj)

                    vert_triangles[vertex] += 1
                    vert_triangles[adj_vert] += 1
                    vert_triangles[adj_to_adj] += 1

                    total_triangles += 1
    print(f'total triangles number = {total_triangles}')

    # closed_triplets - 3 vertexes with 3 edges between them
    # triplets - 3 vertexes with at least 2 edges between them

    # local clustering coefficients
    # =
    # closed_triplets_for_vert / triplets_for_vert
    # closed_triplets_for_vert = the number of triangles containing this vertex

    # average clustering coefficient
    # =
    # sum_for_each_vert(local_clustering_coefficient) / the_number_of_vertexes

    # global clustering coefficient
    # = 
    # closed_triplets_number / triplets_number
    # =
    # total_triangles_number * 3 / triplets_number
    # =
    # total_triangles_number * 3 / sum_for_each_vert(pow * (pow-1) / 2)
    # =
    # total_triangles_number * 6 / sum_for_each_vert(pow * (pow-1))

    local_coefficients = {}
    average_coefficient = 0
    triplets_doubled_total = 0

    for vertex in graph.adj:
        vert_pow = len(graph.adj[vertex])

        # the doubled number of opened triplets for current vertex
        triplets_doubled_vert = 0

        local_coefficients[vertex] = 0
        if vert_pow > 1:
            triplets_doubled_vert = vert_pow * (vert_pow - 1)
            local_coefficients[vertex] = 2 * vert_triangles[vertex] / triplets_doubled_vert
        triplets_doubled_total += triplets_doubled_vert

        average_coefficient += local_coefficients[vertex]

        print(f'vert:{vertex} triangles:{vert_triangles[vertex]} local_coefficient:{local_coefficients[vertex]}')

    average_coefficient /= graph.v  # graph.v - the number of vertexes
    global_coefficient = total_triangles * 6 / triplets_doubled_total

    print(f'average_coefficient = {average_coefficient}')
    print(f'global_coefficient = {global_coefficient}')
