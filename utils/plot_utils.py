import matplotlib.pyplot as plt

def plot_fractal(data, xlim, ylim, filename="newton_fractal.png",
                 title="Newton Fractal", cmap="viridis"):
    """
    Plot and save the fractal image.

    Parameters:
        data: 2D array representing the fractal (e.g., root indices).
        xlim: Tuple for x-axis limits.
        ylim: Tuple for y-axis limits.
        filename: File name for saving the image.
        title: Title of the plot.
        cmap: Matplotlib colormap.
    """
    plt.figure(figsize=(8, 8))
    plt.imshow(data, extent=(xlim[0], xlim[1], ylim[0], ylim[1]),
               origin='lower', cmap=cmap)
    plt.colorbar(label='Root Index')
    plt.title(title)
    plt.xlabel("Real Axis")
    plt.ylabel("Imaginary Axis")
    plt.savefig(filename, dpi=300)
    plt.show()
