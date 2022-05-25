import matplotlib.pyplot as plt


def node_degrees(graph):
    return dict(map(lambda item: (item[0], len(item[1])), graph.adj.items()))


def degrees_probabilities(graph):
    result = [0] * graph.v
    for vertex in graph.adj.items():
        cur_degree = len(vertex[1])
        result[cur_degree] += 1
    for i in range(graph.v):
        result[i] /= graph.v
    return result


def average_node_degree_from_graph(graph):
    degrees = node_degrees(graph)

    return average_node_degree(degrees)


def average_node_degree(degrees):
    result = 0
    for current_degree in degrees.values():
        result += current_degree

    return result / len(degrees)


def probability_function_plot(array):
    plt.style.use('seaborn-whitegrid')

    figure = plt.figure()

    default_axes = figure.add_subplot(2, 1, 1)
    loglog_axes = figure.add_subplot(2, 1, 2)

    default_axes.set_title('Default axes')
    default_axes.set_xlim(0, 1000)
    default_axes.plot(array)
    plt.loglog()
    loglog_axes.plot(array)
    loglog_axes.set_title('log-log axes')
    plt.show()
