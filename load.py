import sys
import pandas as pd
import subprocess

def main(file_path):
    # Load the dataset from the specified file path
    df = pd.read_csv(file_path)

    # Save the loaded dataset to a new CSV file
    df.to_csv('titanic.csv', index=False)

    # Call another script or function to perform further data processing (e.g., dpre.py)
    subprocess.run(["python3", "dpre.py", "titanic.csv"])
    subprocess.run(["python3", "eda.py", "res_dpre.csv"])
    subprocess.run(["python3", "model.py","res_dpre.csv"])
    subprocess.run(["python3", "vis.py","titanic.csv"])
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 load.py <file_path>")
    else:
        file_path = sys.argv[1]
        main(file_path)