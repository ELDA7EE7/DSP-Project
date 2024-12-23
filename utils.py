import statistics
import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt
import pywt
import pandas as pd
import scipy.stats as stats
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
import matplotlib.pyplot as plt
FS=360
LOW_CUT=0.5
HIGH_CUT=40
WAVELET_FAMILY='db2'
LEVEL = 3

def plot(numbers:list,title):
    # Generate x-coordinates (index of each number)
    x = list(range(len(numbers)))

    # Draw a line through the points
    plt.plot(x, numbers, color='blue', linestyle='-', linewidth=2)

    # Add labels and a legend
    plt.xlabel('Index')
    plt.ylabel('ECG')
    plt.title(title)
    plt.legend()

    # Display the plot
    plt.grid(True)
    plt.show()
    
def getDataEntries(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split('|')
            data.append(parts)
    data = [i[:len(i)-1] for i in data]
    new_data = []
    for inner_list in data:
        new_inner_list = [float(element) for element in inner_list]
        new_data.append(new_inner_list)
    return new_data

def remove_mean(signal:list):
    mean= statistics.mean(signal)
    new_signal=[i-mean for i in signal]
    return new_signal

def remove_mean_for_all(signals:list):
    new_signals=[]
    for i in range(len(signals)):
        new_signals.append(remove_mean(signals[i]))
    return new_signals

def create_bandpass_filter(lowcut, highcut, fs, order=4):
    """
    Create Butterworth bandpass filter.
    """
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

def apply_bandpass_filter_batch(signals, fs, lowcut=0.5, highcut=40, order=4):
    """
    Apply Butterworth bandpass filter to multiple signals.
    
    Parameters:
    signals (numpy.ndarray): 2D array where each row is a signal
    """
    b, a = create_bandpass_filter(lowcut, highcut, fs, order)
    return list(np.apply_along_axis(lambda x: filtfilt(b, a, x), 1, signals))

def apply_bandpass_filer_for_signal(signal,fs=360,lowcut=0.5,highcut=40,order=4):
    b, a = create_bandpass_filter(lowcut, highcut, fs, order)
    return filtfilt(b, a, signal)
    


def calculate_statistics(signal):
    mean = np.mean(signal)
    std_deviation = np.std(signal)
    skewness = stats.skew(signal)
    kurtosis = stats.kurtosis(signal)
    return mean, std_deviation, skewness, kurtosis

def normalize_signal(signal, new_min=0, new_max=1):
    """
    Normalize a signal to a specified range [new_min, new_max].

    Parameters:
        signal (array-like): Input signal to be normalized.
        new_min (float): Minimum value of the normalized signal.
        new_max (float): Maximum value of the normalized signal.

    Returns:
        numpy.ndarray: Normalized signal.
    """
    signal = np.array(signal)
    old_min = np.min(signal)
    old_max = np.max(signal)
    
    if old_min == old_max:
        raise ValueError("Signal has no variation (all values are the same).")
    
    normalized_signal = (signal - old_min) / (old_max - old_min)  # Scale to [0, 1]
    normalized_signal = normalized_signal * (new_max - new_min) + new_min  # Scale to [new_min, new_max]
    
    return normalized_signal

def normalize_for_all(signals:list):
    new_signals=[]
    for i in range(len(signals)):
        new_signals.append(normalize_signal(signals[i],-1,1))
    return new_signals    


def plot_signal(window, signal_data, canvas=None, ax=None):
    if not signal_data:
        messagebox.showwarning("Warning", "No signal data to plot. Please upload a file first.")
        return

    # If canvas and ax are provided, clear the previous plot
    if canvas:
        canvas.get_tk_widget().destroy()  # Destroy the previous canvas widget

    # Create a new Matplotlib figure and axes if they don't exist
    if not ax:
        fig, ax = plt.subplots(figsize=(5, 3))
    else:
        fig = ax.figure

    # Plot the new signal data
    ax.clear()  # Clear previous plot
    ax.plot(signal_data, label="Signal", color="blue")
    ax.set_title("Signal Plot")
    ax.set_xlabel("Sample")
    ax.set_ylabel("Amplitude")
    ax.legend()

    # Embed the new plot into the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    return canvas, ax
    
def preprocess_signal(signal):
   signal = remove_mean(signal)
   signal = apply_bandpass_filer_for_signal(signal)
   signal = normalize_signal(signal,-1,1)
   return signal

def extract_features(signal):
    approximates=[]

    coeff=pywt.wavedec(signal,wavelet=WAVELET_FAMILY,level=LEVEL)
    approximates = coeff[0]
    
    statistics_row = calculate_statistics(approximates)
    # Convert to a DataFrame with correct column names
    statistics_row = pd.DataFrame(
        [statistics_row],  # Wrap in a list to create a single-row DataFrame
        columns=['Mean', 'Standard Deviation', 'Skewness', 'Kurtosis']
    )
    return statistics_row
   