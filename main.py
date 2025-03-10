import argparse
import numpy as np
from utils.plot_utils import plot_fractal
from newton_fractal import newton_fractal

def f(z):
    """Define the quintic polynomial P(z) = 2*z**5 - z**4 + 3*z**3 + 4*z**2 - 7."""
    return 2*z**5 - z**4 + 3*z**3 + 4*z**2 - 7

def df(z):
    """Derivative of P(z): P'(z) = 10*z**4 - 4*z**3 + 9*z**2 + 8*z."""
    return 10*z**4 - 4*z**3 + 9*z**2 + 8*z

def main():
    parser = argparse.ArgumentParser(
        description="Generate Newton Fractal for a Quintic Polynomial")
    parser.add_argument("--resolution", type=int, default=500,
                        help="Grid resolution for the fractal")
    parser.add_argument("--max_iter", type=int, default=30,
                        help="Maximum number of iterations (num_steps)")
    parser.add_argument("--tolerance", type=float, default=1e-6,
                        help="Convergence tolerance")
    parser.add_argument("--xlim", type=float, nargs=2, default=[-2, 2],
                        help="Real axis limits")
    parser.add_argument("--ylim", type=float, nargs=2, default=[-2, 2],
                        help="Imaginary axis limits")
    args = parser.parse_args()

    # Compute the roots of the quintic polynomial using numpy's roots function.
    coefficients = [2, -1, 3, 4, 0, -7]
    roots = np.roots(coefficients)
    print("Computed roots:", roots)

    # Compute the fractal. With max_iter=1, the output will resemble a Voronoi diagram.
    root_idx, iterations = newton_fractal(f, df, roots,
                                            xlim=tuple(args.xlim),
                                            ylim=tuple(args.ylim),
                                            resolution=args.resolution,
                                            max_iter=args.max_iter,
                                            tolerance=args.tolerance)

    # Plot the fractal using the helper function from plot_utils.
    title = f"Newton Fractal for Quintic Polynomial (max_iter = {args.max_iter})"
    plot_fractal(root_idx, tuple(args.xlim), tuple(args.ylim),
                 filename="newton_fractal_quintic.png", title=title, cmap="viridis")

if __name__ == "__main__":
    main()