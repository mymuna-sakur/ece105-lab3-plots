"""
========================================
Moving Average Filter for Noisy Signal
========================================

This example demonstrates a moving average filter applied to a noisy
sinusoidal waveform. It compares the raw signal and the smoothed output
so engineers can visualize how the filter reduces high-frequency noise.
"""

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2, 400)
rng = np.random.default_rng(seed=42)
signal = np.sin(2 * np.pi * 5 * t) + 0.6 * rng.normal(size=t.size)
window = 25
kernel = np.ones(window) / window
smoothed = np.convolve(signal, kernel, mode="same")

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(t, signal, color="steelblue", linewidth=1.1, label="Noisy signal")
ax.plot(t, smoothed, color="coral", linewidth=2, label="Moving average (window=25)")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Amplitude")
ax.set_title("Moving Average Smoothing of a Noisy Sinusoid")
ax.legend(loc="upper right")
ax.grid(alpha=0.3)

plt.tight_layout()
plt.show()

# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules
#    is shown in this example:
#
#    - `matplotlib.axes.Axes.plot` / `matplotlib.pyplot.plot`
#    - `matplotlib.pyplot.subplots`
#    - `matplotlib.pyplot.tight_layout`
#    - `matplotlib.pyplot.show`
#
# .. tags::
#
#    plot-type: line
#    level: beginner

