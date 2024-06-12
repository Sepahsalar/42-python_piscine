import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def transpose_image(image_path: str):
    """
    Load the image, cut a square part, transpose it manually,
    and display the resulting image.

    Parameters:
    image_path (str): The path to the image file.

    Returns:
    None
    """
    image = ft_load(image_path)
    if image is None:
        return

    try:
        cropped_image = image.crop((450, 100, 850, 500))
        img_array = np.array(cropped_image)
        print("The shape of image is:", img_array.shape)
        all_data = []
        for data in cropped_image.getdata():
            temp = []
            temp.append(data)
            all_data.append(temp)
        array = np.array(all_data)
        print(array)
        transposed_data = []
        width, height = cropped_image.size
        for x in range(height):
            row = []
            for y in range(width):
                pixel = cropped_image.getpixel((x, y))
                row.append(pixel)
            transposed_data.append(row)
        transposed_array = np.array(transposed_data)
        print("New shape after Transpose:", transposed_array.shape)
        print(transposed_array)
        plt.imshow(transposed_array, cmap='gray')
        plt.show()
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    transpose_image("../animal.jpeg")
