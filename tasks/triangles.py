def triangles(graph):
    number = 0
    local_coefficients = {}
    triangles_for_vert = {}
    for current in graph.adj:
        triangles_for_vert[current] = 0

    for current in graph.adj:
        for adj_vert in graph.adj[current]:
            if adj_vert < current:
                continue
            for adj_to_adj in graph.adj[adj_vert]:
                if adj_to_adj in graph.adj[current] and adj_to_adj > adj_vert:
                    print(current, adj_vert, adj_to_adj)

                    triangles_for_vert[current] += 1
                    triangles_for_vert[adj_vert] += 1
                    triangles_for_vert[adj_to_adj] += 1

                    number += 1

    for current in graph.adj:
        current_vert_pow = len(graph.adj[current])
        local_coefficients[current] = 2 * triangles_for_vert[current] / current_vert_pow / (current_vert_pow - 1)
        print(f'vert:{current}, triangles:{triangles_for_vert[current]} coef:{local_coefficients[current]}\n')
    print(number)
