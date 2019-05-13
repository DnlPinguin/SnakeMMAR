import numpy as np
import matplotlib.pyplot as plt


def aufgabe1(scope1, scope2):
    x_axis = np.arange(scope1, scope2)
    tx = wetterdaten[scope1:scope2, 6]
    rr = wetterdaten[scope1:scope2, 12]

    fig, ax1 = plt.subplots()
    ax1.plot(x_axis, tx, 'r')
    ax1.set_ylabel('Temperatur', color='r')
    ax1.tick_params('y', colors='r')

    ax2 = ax1.twinx()
    ax2.plot(x_axis, rr, 'b.')
    ax2.set_ylabel('Niederschlag', color='b')

    fig.show()

def aufgabe2():


if __name__ == '__main__':
    wetterdaten = np.loadtxt("muenchen_flughafen.txt", skiprows=3)
    #aufgabe1(0, 500)
