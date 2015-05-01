import matplotlib.pyplot as plt

if __name__ == '__main__':
    # histogram = {'lighttpd': 3, 'nginx': 80, 'Apache': 599, 'IIS': 61}
    histogram = {'lighttpd': 3, 'Apache': 715, 'IIS': 71, 'nginx': 83}

    labels = []
    sizes = []
    for item in histogram:
        labels.append(item)
        sizes.append(histogram[item])

    colors = ['slateblue', 'peachpuff', 'darkseagreen', 'lightpink']
    explode = (0.1, 0, 0, 0)

    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

    plt.axis('equal')
    plt.show()
