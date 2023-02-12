import matplotlib.pyplot as plt
import numpy as np

def plot_letters_A_and_I(A_color, I_color):
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    # Plotting letter A
    ax[0].set_title("A", fontsize=30, color=A_color)
    ax[0].fill([0, 0.5, 1, 0.5, 0], [0, 0, 1, 2, 0], A_color, edgecolor="black")
    ax[0].axis("off")

    # Plotting letter I
    ax[1].set_title("I", fontsize=30, color=I_color)
    ax[1].fill([0.1, 0.9], [0, 2], I_color, edgecolor="black")
    ax[1].fill([0.45, 0.55], [0, 2], "white", edgecolor="black")
    ax[1].axis("off")

    plt.show()

plot_letters_A_and_I("#0072C6", "#FC4C02")
