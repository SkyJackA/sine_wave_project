import numpy as np
import matplotlib.pyplot as plt

def plot_sine_wave(frequency=1, duration=2, sample_rate=1000):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    # initializes a 1 Hz sine wave graphed over a two-second timeframe.
    y = np.sin(2 * np.pi * frequency * t)
    # sine wave equation (y = sin(2pi*t))
    plt.figure(figsize=(8, 4))
    plt.plot(t, y, label=f"{frequency} Hz")
    plt.title("Sine Wave")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot_sine_wave()