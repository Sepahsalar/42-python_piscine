import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom_image(image_path: str):
    # Load the image
    image = ft_load(image_path)
    if image is None:
        return

    try:
        zoomed_image = image.crop((450, 100, 850, 500))
        print("New shape after slicing:", zoomed_image.size)
        all_data = []
        for data in zoomed_image.getdata():
            temp = []
            temp.append(data)
            all_data.append(temp)
        array = np.array(all_data)
        print(array)
        plt.imshow(zoomed_image, cmap='gray')
        plt.show()

    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    zoom_image("../animal.jpeg")
