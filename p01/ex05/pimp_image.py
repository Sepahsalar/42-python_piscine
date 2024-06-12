import numpy as np
import matplotlib.pyplot as plt


def show_image(array, mode):
    """
    Displays the image.

    Parameters:
    array (numpy.ndarray): Input image array.
    """
    plt.imshow(array)
    plt.axis('off')
    plt.title(mode)
    plt.show()


def ft_invert(array):
    """
    Inverts the colors of the image received and displays it.

    Parameters:
    array (numpy.ndarray): Input image array.

    Returns:
    numpy.ndarray: Inverted image array.
    """
    show_image(array, 'Original')
    inverted_array = 255 - array
    show_image(inverted_array, 'Invert')
    return inverted_array


def ft_red(array):
    """
    Removes green and blue components, leaving only red,
    and displays the image.

    Parameters:
    array (numpy.ndarray): Input image array.

    Returns:
    numpy.ndarray: Image array with only red component.
    """
    red_only = np.zeros_like(array)
    red_only[:, :, 0] = array[:, :, 0]
    show_image(red_only, 'Red')
    return red_only


def ft_green(array):
    """
    Removes red and blue components, leaving only green,
    and displays the image.

    Parameters:
    array (numpy.ndarray): Input image array.

    Returns:
    numpy.ndarray: Image array with only green component.
    """
    green_only = np.zeros_like(array)
    green_only[:, :, 1] = array[:, :, 1]
    show_image(green_only, 'Green')
    return green_only


def ft_blue(array):
    """
    Removes red and green components, leaving only blue,
    and displays the image.

    Parameters:
    array (numpy.ndarray): Input image array.

    Returns:
    numpy.ndarray: Image array with only blue component.
    """
    blue_only = np.zeros_like(array)
    blue_only[:, :, 2] = array[:, :, 2]
    show_image(blue_only, 'Blue')
    return blue_only


def ft_grey(array):
    """
    Converts the image to grayscale and displays it.

    Parameters:
    array (numpy.ndarray): Input image array.

    Returns:
    numpy.ndarray: Grayscale image array.
    """
    grey_array = np.mean(array, axis=2).astype(np.uint8)
    plt.imshow(grey_array, cmap='gray')
    plt.axis('off')
    plt.title('Grey')
    plt.show()
    return grey_array
