from PIL import Image
import numpy as np

def ft_load(path: str) -> np.ndarray:
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
        print("Image format:", img.format)
        img = img.convert("RGB")
        img_array = np.array(img)
        print("The shape of image is:", img_array.shape)
        print(img_array)     
        # return img_array
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None
    return img_array
