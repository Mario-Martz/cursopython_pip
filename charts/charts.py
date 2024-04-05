import matplotlib.pyplot as pylot

def generate_pie_chart():
    labels = ['A', 'B', 'C', 'D', 'E']
    values = [10, 20, 30, 40, 50]

    fig, ax = pylot.subplots()
    ax.pie(values, labels=labels)
    pylot.savefig('.pie.png')
    pylot.close()