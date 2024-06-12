import matplotlib.pyplot as plt
from load_csv import load


def convert_to_number(population_str):
    """
    Convert population string with 'k' and 'M' suffixes to numeric values.

    Parameters:
    population_str (str): Population string with suffixes.

    Returns:
    float: Population value as a float.
    """
    if population_str.endswith('k'):
        return float(population_str[:-1]) * 1000
    elif population_str.endswith('M'):
        return float(population_str[:-1]) * 1000000
    else:
        return float(population_str)


def plot_population(csv_file, country1, country2):
    """
    Load population data from a CSV file and plot the data
    for two specified countries.

    Parameters:
    csv_file (str): The path to the CSV file containing population data.
    country1 (str): The first country to plot.
    country2 (str): The second country to plot.

    Returns:
    None

    This function loads the CSV file using the load_csv function,
    filters the data for the specified countries, and creates a line plot
    showing the population projections over the years.
    """
    df = load(csv_file)
    years = list(range(1800, 2051))
    country1_data = df[df['country'] == country1].iloc[:, 1:252]
    country2_data = df[df['country'] == country2].iloc[:, 1:252]
    if country1_data.empty:
        print(f"No data available for {country1}.")
        return
    if country2_data.empty:
        print(f"No data available for {country2}.")
        return
    country1_population = country1_data.values[0].astype(str)
    country2_population = country2_data.values[0].astype(str)
    country1_population = [convert_to_number(pop)
                           for pop in country1_population]
    country2_population = [convert_to_number(pop)
                           for pop in country2_population]
    year_range = 2050 - 1800
    tick_interval = max(1, year_range // 10)
    plt.figure(figsize=(10, 6))
    plt.plot(years, country1_population, label=country1)
    plt.plot(years, country2_population, label=country2)
    plt.title(f'Population Comparison: {country1} vs {country2}')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.xticks(ticks=range(1800, 2051, tick_interval))
    plt.legend()
    max_population = max(max(country1_population), max(country2_population))
    plt.ticklabel_format(axis='y', style='plain', useOffset=False)
    plt.gca().get_yaxis().set_major_formatter
    (plt.FuncFormatter(lambda x,
                       loc: f"{int(x/1000000):,.0f}M" if x > 0 else ''))
    plt.yticks(ticks=range(0, int(max_population) + 1, 1000000))
    plt.show()


if __name__ == "__main__":
    csv_file = '../population_total.csv'
    country1 = 'Finland'
    country2 = 'Norway'
    plot_population(csv_file, country1, country2)
