# Newton Fractal Project

This project generates Newton Fractals using Newton's method to find the roots of a complex polynomial. It is inspired by the entrancing visualizations seen in videos like 3Blue1Brown's exploration of Newton’s method.

## Features
- Generates fractals for any function (by default \( P(z) = 2*z**5 - z**4 + 3*z**3 + 4*z**2 - 7 \)).
- Adjustable parameters including grid resolution, maximum iterations (num_steps), and convergence tolerance.
- When `max_iter` is set to 1, the output essentially becomes a Voronoi diagram—each region corresponds to the root that is nearest. (Many mesh-generation algorithms use Voronoi diagrams and their dual Delaunay triangulations to determine meaningful edge structures.)
- Modular project structure for clarity and extensibility.

## Usage

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt


## Example Output

Here's an example fractal plot generated using `max_iter=15` for the complex quintic polynomial:

![Newton Fractal](assets/1.png)
