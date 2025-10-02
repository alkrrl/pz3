import matplotlib.pyplot as plt
import pandas as pd


def plot_function(x, y, func_name):
    plt.plot(x, y, label=f"{func_name}(x)")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(f"График функции {func_name}(x)")
    plt.legend()
    plt.grid(True)
    plt.show()


def print_table(x, y):
    df = pd.DataFrame({"X": x, "Y": y})
    print(df.to_string(index=False))
