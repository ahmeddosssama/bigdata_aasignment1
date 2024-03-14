import pandas as pd

def exploratory_data_analysis(df):
    insights = []
    
    # 1. Summary Statistics
    summary_stats = df.describe()
    insights.append("Summary Statistics:\n" + str(summary_stats))
    
    # 2. Missing Values
    missing_values = df.isnull().sum()
    insights.append("Missing Values Summary:\n" + str(missing_values))
       
    # Exclude non-numeric columns before computing correlation matrix
    numeric_df = df.select_dtypes(include=['number'])
    
    # 3. Correlation Analysis
    correlation_matrix = numeric_df.corr()
    insights.append("Correlation Matrix:\n" + str(correlation_matrix))
    
    # Return insights
    return insights

def main(processed_df):
    # Perform EDA
    insights = exploratory_data_analysis(processed_df)
    
    # Save insights as text files
    for i, insight in enumerate(insights, start=1):
        with open(f"eda-in-{i}.txt", "w") as file:
            file.write(insight)

if __name__ == "__main__":
    import sys
    # Load the processed DataFrame from dpre.py
    processed_df = pd.read_csv(sys.argv[1])
    main(processed_df)