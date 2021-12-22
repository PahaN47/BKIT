import matplotlib
import values
import numpy as np
from matplotlib import pyplot as plt
matplotlib.use('Agg')
from math import *

def str_to_func(str):
    try:
        return eval('lambda x: ' + str.lower())
    except SyntaxError:
        return lambda x: 0

def plot(str):
    fig, ax = plt.subplots()
    f = str_to_func(str)
    x = np.linspace(-10, 10, 10000)
    fx = np.array([])
    x_good = np.array([])
    for x0 in x:
        try:
            if abs(f(x0)) > 200:
                raise ValueError
            fx = np.append(fx, f(x0))
            x_good = np.append(x_good, x0)
        except ValueError:
            pass
        except OverflowError:
            pass
        except ZeroDivisionError:
            pass
    ax.plot(x_good, fx)
    plot_file = values.prog_path + '/' + values.fig_filename
    fig.savefig(plot_file)
    return plot_file

if __name__ == '__main__':
    plot('exp(1/x)')
    