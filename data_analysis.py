import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

if __name__ == "__main__":
    x = np.linspace(1, 100, 10000)
    x.sort()
    x_pdf = norm.pdf(x, x.mean(), x.std())

    p_s = np.linspace(0.025, 0.975, 100)  # inside confidence interval boundaries
    x_inverse_pdf = norm.ppf(p_s, x.mean(), x.std())

    fig, ax = plt.subplots(2, 1)
    ax[0].plot(x, x_pdf)
    ax[0].axvline(x.mean(), ls="--", c="green")
    ax[0].set_title("Normal PDF")

    ax[1].plot(p_s, x_inverse_pdf)
    ax[1].set_title("Inverse normal PDF")
    ax[1].set_xticks(np.linspace(0, 1, 11))

    plt.show()


