import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def plot_life_expectancy_vs_gdp(life_csv, gdp_csv):
    """
    Load life expectancy and GDP data from CSV files and
    plot the data for the year 1900.

    Parameters:
    life_expectancy_csv (str): The path to the CSV file containing
    life expectancy data.
    gdp_csv (str): The path to the CSV file containing GDP data.

    Returns:
    None

    This function loads the CSV files using the load function,
    extracts the data for the year 1900, and creates a scatter plot
    showing the life expectancy in relation to the gross national product.
    """
    life_df = load(life_csv)
    gdp_df = load(gdp_csv)
    year = '1900'
    life_1900 = life_df[['country', year]]
    gdp_1900 = gdp_df[['country', year]]
    add = life_1900.merge(gdp_1900, on='country', suffixes=('_life', '_gdp'))
    add = add.dropna()
    add[year + '_life'] = pd.to_numeric(add[year + '_life'])
    add[year + '_gdp'] = pd.to_numeric(add[year + '_gdp'])
    plt.figure(figsize=(10, 6))
    plt.scatter(add[year + '_gdp'], add[year + '_life'])
    plt.title('1900')
    plt.xlabel('Gross Domestic Product')
    plt.ylabel('Life Expectancy')
    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
    plt.show()


if __name__ == "__main__":
    life_csv = '../life_expectancy_years.csv'
    gdp_csv = '../income_per_person_gdppercapita_ppp_inflation_adjusted.csv'
    plot_life_expectancy_vs_gdp(life_csv, gdp_csv)
