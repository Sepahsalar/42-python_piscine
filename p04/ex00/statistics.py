def ft_statistics(*args, **kwargs):
    """
    Calculate and print statistical measures
    (`mean`, `median`, `quartiles`, `standard deviation`, `variance`)
    based on the arguments and keyword arguments provided.

    Parameters:
    `*args`: Variable length argument list containing numerical data.
    `**kwargs`: Keyword arguments specifying which statistical
    measures to calculate.
    """
    def mean(data):
        """
        Calculate the `mean` (average) of the given data.

        Parameters:
        `data` (list of `float`): List of numerical values.

        Returns:
        `float`: `Mean` of the data.
        """
        return sum(data) / len(data)

    def median(data):
        """
        Calculate the `median` of the given data.

        Parameters:
        `data` (list of `float`): List of numerical values.

        Returns:
        `float`: `Median` of the data.
        """
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def quartiles(data):
        """
        Calculate the first (25%) and third (75%) `quartiles` of
        the given data.

        Parameters:
        `data` (list of `float`): List of numerical values.

        Returns:
        list of `float`: [first `quartile`, third `quartile`]
        """
        sorted_data = sorted(data)
        n = len(sorted_data)
        q1 = sorted_data[n // 4]
        q3 = sorted_data[(3 * n) // 4]
        return [q1, q3]

    def variance(data):
        """
        Calculate the `variance` of the given data.

        Parameters:
        `data` (list of `float`): List of numerical values.

        Returns:
        `float`: `Variance` of the data.
        """
        m = mean(data)
        return sum((x - m) ** 2 for x in data) / len(data)

    def std_dev(data):
        """
        Calculate the `standard deviation` of the given data.

        Parameters:
        `data` (list of `float`): List of numerical values.

        Returns:
        `float`: `Standard deviation` of the data.
        """
        return variance(data) ** 0.5
    try:
        data = [float(arg) for arg in args]
        if not data:
            raise ValueError
    except (ValueError, TypeError):
        data = []
    results = {}
    for key, value in kwargs.items():
        try:
            if value == "mean":
                results[value] = mean(data)
            elif value == "median":
                results[value] = median(data)
            elif value == "quartile":
                results[value] = quartiles(data)
            elif value == "std":
                results[value] = std_dev(data)
            elif value == "var":
                results[value] = variance(data)
            else:
                continue
        except Exception:
            results[value] = "ERROR"
    if not results:
        return
    for key, result in results.items():
        if result == "ERROR":
            print(result)
        else:
            print(f"{key} : {result}")
