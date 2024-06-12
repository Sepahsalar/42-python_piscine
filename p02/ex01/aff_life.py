import matplotlib.pyplot as plt
from load_csv import load


def plot_life_expectancy(csv_file, country):
    """
    Load life expectancy data from a CSV file and
    plot the data for a specified country.

    Parameters:
    csv_file (str): The path to the CSV file containing life expectancy data.
    country (str): The country for which to plot the life expectancy data.

    Returns:
    None

    This function loads the CSV file using the load_csv function,
    filters the data for the specified country,
    and creates a line plot showing the life expectancy projections
    over the years.
    """
    df = load(csv_file)
    country_data = df[df['country'] == country]
    if country_data.empty:
        print(f"No data available for {country}.")
        return
    years = country_data.columns[1:].values
    life_expectancy = country_data.values[0][1:].astype(float)
    years = years.astype(int)
    year_range = years.max() - years.min()
    tick_interval = max(1, year_range // 10)
    plt.figure(figsize=(10, 6))
    plt.plot(years, life_expectancy, label=country)
    plt.title(f'{country} Life Expectancy Projections')
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.xticks(ticks=range(years.min(), years.max() + 1, tick_interval))
    plt.legend()
    plt.show()


if __name__ == "__main__":
    csv_file = "../life_expectancy_years.csv"
    country = "Finland"
    plot_life_expectancy(csv_file, country)
