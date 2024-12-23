import tkinter as tk
from tkinter import filedialog
from utils import *
import joblib
signal_data = []  # Initialize signal data as an empty list
canvas = None
ax = None
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


def classify_signal(label):
    global signal_data
    signal_data_processed = preprocess_signal(signal_data)
    features = extract_features(signal_data_processed)
    prediction = knn_loaded.predict(features)
    if prediction == 0 :
        prediction = "NORMAL"
    else:
        prediction = "LBBB"
    
    label.config(text=f"Signal Classification: {prediction}")
    
def plot_button_handler(window,signal):
    global canvas , ax
    canvas , ax =plot_signal(window,signal,canvas,ax)

def main_window():
    # Initialize the Tkinter window
    global signal_data 
    window = tk.Tk()
    window.title("Signal Plotter")
    window.geometry("600x400")


    # Add buttons to the window
    upload_button = tk.Button(window, text="Upload Signal File", command=upload_file)
    upload_button.pack(pady=10)

    plot_button = tk.Button(window, text="Plot Signal", command=lambda:plot_button_handler(window,signal_data))
    plot_button.pack(pady=10)

    predict_button = tk.Button(window, text="is the signal normal or LBBB?", command=lambda:classify_signal(result_label))
    predict_button.pack(pady=10)

    result_label = tk.Label(window, text="", width=50)
    result_label.pack(pady=10)
    # Start the Tkinter event loop
    window.mainloop()
    

if __name__ == "__main__":
    #load the model
    knn_loaded = joblib.load('knn_model.joblib')
    
    main_window()
