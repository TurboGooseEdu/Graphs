import matplotlib.pyplot as plt


def plot_probability_function(array):
    plt.style.use('seaborn-whitegrid')

    figure = plt.figure()

    default_axes = figure.add_subplot(2, 1, 1)
    loglog_axes = figure.add_subplot(2, 1, 2)

    default_axes.set_title('Probability of degree for node')
    default_axes.set_xlim(0, 100)
    default_axes.set_xlabel('Degree')
    default_axes.set_ylabel('Probability')
    default_axes.plot(array)
    plt.loglog()
    loglog_axes.plot(array)
    loglog_axes.set_title('Probability of degree for node (log-log)')
    loglog_axes.set_xlabel('Degree')
    loglog_axes.set_ylabel('Probability')
    plt.show()


def plot_deleting_nodes(array, name="Untitled graph"):
    plt.style.use('seaborn-whitegrid')

    figure = plt.figure()

    axes = []
    axes_names = [
        name + ": random",
        name + ": largest degree",
    ]

    for i in range(len(array)):
        axes.append(figure.add_subplot(2, 1, i + 1))
        axes[i].set_title(axes_names[i])

        axes[i].set_xlabel('Percentage of deleted vertices')
        axes[i].set_ylabel('The proportion of vertices')

        axes[i].set_xlim(0, 100)
        axes[i].plot(array[i])

    plt.show()
