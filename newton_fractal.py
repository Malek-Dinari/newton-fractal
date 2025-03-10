import numpy as np

def newton_fractal(func, dfunc, roots, xlim=(-1.5, 1.5), ylim=(-1.5, 1.5),
                   resolution=500, max_iter=30, tolerance=1e-6):
    """
    Compute the Newton fractal for a given function.

    Parameters:
        func: The function f(z) (should be vectorized for numpy arrays).
        dfunc: The derivative f'(z).
        roots: List or array of known roots (complex numbers).
        xlim: Tuple (xmin, xmax) for real axis limits.
        ylim: Tuple (ymin, ymax) for imaginary axis limits.
        resolution: Number of points along each axis.
        max_iter: Maximum number of iterations (num_steps).
        tolerance: Convergence tolerance.

    Returns:
        root_index: 2D array of indices indicating which root each point converged to (-1 if not converged).
        iterations: 2D array of iteration counts until convergence.
    """
    # Create grid of complex numbers
    real = np.linspace(xlim[0], xlim[1], resolution)
    imag = np.linspace(ylim[0], ylim[1], resolution)
    X, Y = np.meshgrid(real, imag)
    Z = X + 1j * Y

    # Arrays to store which root is converged to and at which iteration
    root_index = np.full(Z.shape, -1, dtype=int)
    iterations = np.zeros(Z.shape, dtype=int)

    # Newton iteration loop
    for i in range(max_iter):
        # Calculate derivative; avoid division by zero by replacing zeros with a small number.
        dz = dfunc(Z)
        dz[dz == 0] = 1e-10

        # Newton's method update: z = z - f(z)/f'(z)
        Z = Z - func(Z) / dz

        # Check convergence against each known root
        for k, r in enumerate(roots):
            # Identify points that have not converged yet and are close to a specific root
            mask = (root_index == -1) & (np.abs(Z - r) < tolerance)
            root_index[mask] = k
            iterations[mask] = i + 1  # Use 1-indexed iteration count

    return root_index, iterations
