import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
signal_data = []  # Initialize signal data as an empty list

def upload_file():
    global signal_data
    signal_path=upload_file_path()
    signal_data= process_file(signal_path)
    #preprocess the file here
    
def upload_file_path():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        return file_path

def process_file(file_path):
    try:
        with open(file_path, "r") as file:
            line = file.readline().strip()  # Read the single line and strip whitespace
            numbers = [float(num) for num in line.split("|") if num]  # Split by '|' and convert to float
        return numbers
    except Exception as e:
        tk.messagebox.showerror("Error", f"Failed to read file: {e}")

    
def plot_signal(window):
    global signal_data
    if not signal_data:
        tk.messagebox.showwarning("Warning", "No signal data to plot. Please upload a file first.")
        return

    # Create a Matplotlib figure
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot(signal_data, label="Signal", color="blue")
    ax.set_title("Signal Plot")
    ax.set_xlabel("Sample")
    ax.set_ylabel("Amplitude")
    ax.legend()

    # Embed the plot into the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

def classify_signal():
    print("Empty function called.")

def main_window():
    # Initialize the Tkinter window
    window = tk.Tk()
    window.title("Signal Plotter")
    window.geometry("600x400")


    # Add buttons to the window
    upload_button = tk.Button(window, text="Upload Signal File", command=upload_file)
    upload_button.pack(pady=10)

    plot_button = tk.Button(window, text="Plot Signal", command=lambda:plot_signal(window))
    plot_button.pack(pady=10)

    empty_button = tk.Button(window, text="is the signal normal or LBBB?", command=classify_signal)
    empty_button.pack(pady=10)

    # Start the Tkinter event loop
    window.mainloop()
    

if __name__ == "__main__":
    main_window()
