"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""
from ast import main

import numpy as np
import matplotlib.pyplot as plt

# Create a function generate_data(seed) that returns sensor_a,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.

def generate_data(seed):
    """Generate synthetic temperature sensor readings.

    Parameters
    ----------
    seed : int
        Random number generator seed for reproducibility.

    Returns
    -------
    sensor_a : numpy.ndarray
        Temperature readings from sensor A in Celsius, shape (200,).
    sensor_b : numpy.ndarray
        Temperature readings from sensor B in Celsius, shape (200,).
    timestamps : numpy.ndarray
        Measurement timestamps in seconds, shape (200,).
    """
    rng = np.random.default_rng(seed=seed)
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=200)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=200)
    timestamps = rng.uniform(low=0.0, high=10.0, size=200)
    return sensor_a, sensor_b, timestamps

# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_scatter(ax, timestamps, sensor_a, sensor_b, *, s=20, alpha=0.7, label_a='Sensor A', label_b='Sensor B', color_a='blue', color_b='orange'):
    """Draw a scatter plot of two sensors on an existing Axes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        An existing Matplotlib Axes object to modify in place.
    timestamps : numpy.ndarray
        1-D array of timestamps (seconds), shape (N,).
    sensor_a : numpy.ndarray
        1-D array of temperature readings for sensor A, shape (N,).
    sensor_b : numpy.ndarray
        1-D array of temperature readings for sensor B, shape (N,).

    Returns
    -------
    None
        The function modifies ax in place and returns None.
    """
    ax.scatter(timestamps, sensor_a, s=s, alpha=alpha, label=label_a, color=color_a)
    ax.scatter(timestamps, sensor_b, s=s, alpha=alpha, label=label_b, color=color_b)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Sensor A and B Readings vs Time')
    ax.legend()

# Create plot_histogram(sensor_a, sensor_b, ax) that draws
# the overlaid histogram from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_histogram(ax, sensor_a, sensor_b, *, bins=30, alpha=0.5, label_a='Sensor A', label_b='Sensor B', color_a='blue', color_b='orange'):
    """Draw an overlaid histogram of two sensors on an existing Axes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        An existing Matplotlib Axes object to modify in place.
    sensor_a : numpy.ndarray
        1-D array of temperature readings for sensor A, shape (N,).
    sensor_b : numpy.ndarray
        1-D array of temperature readings for sensor B, shape (N,).
    bins : int, optional
        Number of bins for the histogram, default is 30.
    alpha : float, optional
        Transparency level for the histogram bars, default is 0.5.
    label_a : str, optional
        Label for sensor A in the legend, default is 'Sensor A'.
    label_b : str, optional
        Label for sensor B in the legend, default is 'Sensor B'.
    color_a : str, optional
        Color for sensor A's histogram bars, default is 'blue'.
    color_b : str, optional
        Color for sensor B's histogram bars, default is 'orange'.

    Returns
    -------
    None
        The function modifies ax in place and returns None.
    """
    ax.hist(sensor_a, bins=bins, alpha=alpha, label=label_a, color=color_a)
    ax.hist(sensor_b, bins=bins, alpha=alpha, label=label_b, color=color_b)
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Count')
    ax.set_title('Temperature Distribution: Sensor A vs Sensor B')
    ax.axvline(sensor_a.mean(), color='blue', linestyle='dashed', linewidth=1.5, label='Mean A')
    ax.axvline(sensor_b.mean(), color='orange', linestyle='dashed', linewidth=1.5, label='Mean B')
    ax.legend()

# Create plot_boxplot(sensor_a, sensor_b, ax) that draws
# the side-by-side box plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None. 
    
def plot_boxplot(ax, sensor_a, sensor_b):
    """Draw a side-by-side box plot of two sensors on an existing Axes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        An existing Matplotlib Axes object to modify in place.
    sensor_a : numpy.ndarray
        1-D array of temperature readings for sensor A, shape (N,).
    sensor_b : numpy.ndarray
        1-D array of temperature readings for sensor B, shape (N,).

    Returns
    -------
    None
    The function modifies ax in place and returns None.
    """
    ax.boxplot([sensor_a, sensor_b], tick_labels=['Sensor A', 'Sensor B'])
    overall_mean = np.mean(np.concatenate([sensor_a, sensor_b]))
    ax.axhline(overall_mean, color='red', linestyle='dashed', linewidth=1.5, label='Overall Mean')
    ax.set_xlabel('Sensor')
    ax.set_ylabel('Temperature (deg C)')
    ax.set_title('Sensor A vs Sensor B Temperature Distribution')
    ax.legend()

# Create main() that generates data, creates a 1x3 subplot figure,
# calls each plot function, adjusts layout, and saves as sensor_analysis.png
# at 150 DPI with tight bounding box.

def main():
    """Generate sensor data and save all three plots as a single PNG.

    Returns
    -------
    None
    """
    sensor_a, sensor_b, timestamps = generate_data(2223)
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    plot_scatter(plt.axes[0], timestamps, sensor_a, sensor_b)
    plot_histogram(plt.axes[1], sensor_a, sensor_b)
    plot_boxplot(plt.axes[2], sensor_a, sensor_b)
    plt.tight_layout()
    fig.savefig('sensor_analysis.png', dpi=150, bbox_inches='tight')
    print('Saved sensor_analysis.png')


if __name__ == '__main__':
    main()
