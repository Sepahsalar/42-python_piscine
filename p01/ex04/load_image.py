from PIL import Image


def ft_load(path: str):
    """
    Load an image from the specified path, print its format,
    shape, and pixel content in RGB format.

    Parameters:
    path (str): The path to the image file.

    Returns:
    np.ndarray: A NumPy array representing the image.

    Raises:
    FileNotFoundError: If the specified file is not found.
    Exception: If any other error occurs during image processing.
    """
    try:
        img = Image.open(path)
        img = img.convert("L")
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None
    return img
