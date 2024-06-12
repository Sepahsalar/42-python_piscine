import pandas as pd


def load(path: str):
    """
    Loads a CSV file into a pandas DataFrame,
    prints the dimensions of the dataset, and returns the DataFrame.
    If an error occurs, it prints an error message and returns None.

    Parameters:
    path (str): The file path to the CSV file to be loaded.

    Returns:
    pd.DataFrame or None: The loaded DataFrame if successful, otherwise None.

    Exceptions:
    Exception: Catches all exceptions, prints an error message,
    and returns None.
    """
    try:
        df = pd.read_csv(path)
        dimensions = df.shape
        print(f"Loading dataset of dimensions {dimensions}")
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    """
    Tests the load function with a specified CSV file path.
    """
    df = load("../life_expectancy_years.csv")
    if df is not None:
        print(df)
    else:
        print("Failed to load the dataset.")


if __name__ == "__main__":
    main()
