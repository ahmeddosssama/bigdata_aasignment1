import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def main(df):


    # Extract titles from names
    titles = []

    for index, row in df.iterrows():
        if 'Name' not in row:
            print("Error: 'Name' column does not exist in the dataframe.")
            continue

        full_name = row['Name']
        if not isinstance(full_name, str):
            print(f"Error: 'Name' value at index {index} is not a string.")
            continue

        name_parts = full_name.split(', ')
        if len(name_parts) < 2:
            print(f"Error: Incorrect 'Name' format at index {index}.")
            continue

        first_name = name_parts[1].split(' ')[0].strip()
        titles.append(first_name)

    # Add the titles list as a new column to the dataframe
    df['title'] = titles

    # Heatmap for survival vs. title
    sb.heatmap(pd.crosstab(df['Survived'], df['title']), annot=True, fmt='d')
    plt.savefig('vis.png')
    plt.show()
    

if __name__ == "__main__":
    import sys
    # Load the processed DataFrame from dpre.py
    df = pd.read_csv(sys.argv[1])
    main(df)