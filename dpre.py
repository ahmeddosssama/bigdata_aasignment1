import sys
import pandas as pd
from subprocess import run, PIPE
from sklearn.feature_selection import SelectKBest, chi2

def data_preprocessing(input_file):
    # Load the DataFrame from the input CSV file
    df = pd.read_csv(input_file)
    print(df.head())
    print("DataFrame shape:", df.shape)
    print("DataFrame data types:")
    print(df.dtypes)
    
    ## DATA CLEANING:
    #dropping irrelevant features
    df = df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
    # Handling Missing values
    print("\nMissing Values Summary:")
    print(df.isna().sum())
    # Dividing data into numerical or categorical
    numerical_df = df.select_dtypes(include='number')
    categorical_df = df.select_dtypes(include='object')
    # Impute missing values in the "Age" column
    numerical_df['Age'].fillna(numerical_df['Age'].mean(), inplace=True)
    
    
    ## DATA TRANSFORMATION
    # Normalization/Standardization
    numerical_df['Age_Disc'] = numerical_df['Age']
    # Create new feature "FamilySize"
    numerical_df['FamilySize'] = numerical_df['SibSp'] + numerical_df['Parch'] + 1
    # OneHotEncoding
    categorical_df = pd.get_dummies(categorical_df)
    df_processed = pd.concat([numerical_df, categorical_df], axis=1)
    print("\nMissing Values Summary after handling:")
    print(df_processed.isna().sum())
    
    
    ## DATA REDUCTION
    # Use SelectKBest to select the top 4 features
    X = df_processed.drop('Survived', axis=1)
    y = df_processed['Survived']
    selector = SelectKBest(chi2, k=4)
    X_new = selector.fit_transform(X, y)
    X_new
    # Add a new column 'TopFeatures' to indicate the selected features
    top_features_indices = selector.get_support(indices=True)
    df_processed['TopFeatures'] = 0
    df_processed.loc[:, 'TopFeatures'].iloc[top_features_indices] = 1

    ##DATA DISCRETIZATION
    # Discretize "Age" into 4 age groups
    bins = [0, 18, 30, 50, 80]
    labels = ['Child', 'Young Adult', 'Adult', 'Elderly']
    df_processed['AgeGroup'] = pd.cut(df_processed['Age'], bins=bins, labels=labels)
    # Discretize "Fare" into 3 fare categories
    fare_bins = [0, 50, 100, float('inf')]
    fare_labels = ['Low', 'Medium', 'High']
    df_processed['FareCategory'] = pd.cut(df_processed['Fare'], bins=fare_bins, labels=fare_labels)

    print(df_processed.head())
    return df_processed




def main():
    # Get input file path from command line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 dpre.py input_file.csv")
        return
    input_file = sys.argv[1]
    
    df_processed = data_preprocessing(input_file)
    df_processed.to_csv('res_dpre.csv', index=False)  # Save the resulting DataFrame
    csv_data = df_processed.to_csv(index=False)
    process = run(["python3", "eda.py"], input=csv_data, stdout=PIPE, stderr=PIPE, text=True)
    print('process.stdout',process.stdout)
    print('process.stderr',process.stderr)

    

if __name__ == "__main__":
    main()