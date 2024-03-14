import numpy as np
import pandas as pd
from sklearn.cluster import KMeans


 

def apply_kmeans(df, k=3):
    numeric_df = df.select_dtypes(include=['number'])
    numeric_df['Age'].fillna(numeric_df['Age'].mean(), inplace=True)
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(numeric_df)
    labels = kmeans.labels_
    cluster_counts = np.bincount(labels)
    return cluster_counts

def save_cluster_counts(cluster_counts):
    with open("k.txt", "w") as f:
        for i, count in enumerate(cluster_counts):
            f.write(f"Cluster {i+1}: {count}\n")

def main(numerical_df):
    # Apply K-means algorithm
    cluster_counts = apply_kmeans(numerical_df)
    
    # Save the number of records in each cluster
    save_cluster_counts(cluster_counts)

if __name__ == "__main__":
    import sys
    # Load the processed DataFrame from dpre.py
    processed_df = pd.read_csv(sys.argv[1])
    main(processed_df)