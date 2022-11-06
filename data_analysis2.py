import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = np.linspace(0, 5, 100)
    inv_e_pow_x = np.exp(-x**2)

    plt.plot(x, inv_e_pow_x, 'g-', label='e^(-x)')
    plt.plot(x, np.log(inv_e_pow_x), 'r-', label="ln(e^(-x))")

    plt.legend(loc=9)
    plt.show()

