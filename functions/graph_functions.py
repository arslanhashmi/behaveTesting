import matplotlib.pyplot as plt
from functions.global_variables import PATH_TO_SAVE_FIGURES, API_HITS


def make_box_plot(name, php_data, python_data, title='Bar plot ', x_label='1: Php, 2: Python', y_label = 'Seconds'):
    """

    :param name: name of the end point
    :param php_data: response times []
    :param python_data: response times []
    :param title: Title for plot
    :param x_label: label of x axis
    :param y_label: label of y axis
    """

    title = "{title}{name} end point for {hits} hits".format(
        title=title,
        hits=API_HITS,
        name=name
    )
    fig = plt.figure()
    data = [php_data, python_data]
    plt.title(title)
    plt.boxplot(data)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    fig.savefig("{folder}/{name}_boxplot.png".format(
            folder=PATH_TO_SAVE_FIGURES,
            name=name
        )
    )
    plt.close(fig)


def make_subplot(name, php_data, python_data, title='Plot for ', x_label='Hits', y_label='Seconds'):
    """

    :param name: name of end point
    :param php_data: response times []
    :param python_data: response times []
    :param title: Title for plot
    :param x_label: label of x axis
    :param y_label: label of y axis
    """
    #For php
    fig, ax = plt.subplots(nrows=1, ncols=1)

    plt.title(title+name + " end point (Php)")
    plt.title("{title}{name} end point (Php)".format(
            title=title,
            name=name
        )
    )
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    ax.plot(range(1, API_HITS + 1), php_data)
    fig.savefig("{folder}/{name}_timings_php.png".format(
            folder=PATH_TO_SAVE_FIGURES,
            name=name
        )
    )
    plt.close(fig)

    #For python
    fig, ax = plt.subplots(nrows=1, ncols=1)
    plt.title("{title}{name} end point (Python)".format(
            title=title,
            name=name
        )
    )
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    ax.plot(range(1, API_HITS + 1), python_data)
    fig.savefig("{folder}/{name}_timings_python.png".format(
            folder=PATH_TO_SAVE_FIGURES,
            name=name
        )
    )
    plt.close(fig)
