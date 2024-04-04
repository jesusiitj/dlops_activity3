import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

roll_number = 203  # m22aie203

def load_data(file_path):
    """Load data from a CSV file."""
    try:
        data = pd.read_excel(file_path)
        return data
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def analyze_data(data):
    """Perform basic data analysis."""
    if data is not None:
        # Handling missing values
        missing_values = data.isnull().sum()
        if not missing_values.empty:
            print("Missing Values:")
            print(missing_values)
        else:
            print("No missing values.")

        # Summary statistics
        print("Summary Statistics:")
        print(data.describe())

        # Visualization: Box plots for numerical columns
        numerical_cols = data.select_dtypes(include=['int', 'float']).columns
        for col in numerical_cols:
            plt.figure(figsize=(8, 6))
            sns.boxplot(x=data[col])
            plt.title(f"Box Plot of {col}")
            plt.show()

        # Visualization: Count plot for categorical columns
        categorical_cols = data.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            plt.figure(figsize=(8, 6))
            sns.countplot(x=data[col])
            plt.title(f"Count Plot of {col}")
            plt.xticks(rotation=45)
            plt.show()

def main():
    file_path = input("Enter the path to the CSV file: ")
    file_path = file_path or './DryBeanDataset/Dry_Bean_Dataset.xlsx'
    data = load_data(file_path)
    if data is not None:
        analyze_data(data)

if __name__ == "__main__":
    main()
