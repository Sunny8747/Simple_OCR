# import tensorflow as tf
import numpy as np
from PIL import Image, ImageFilter

png_file = Image.open("testing2.png")
print(png_file)
# np_array_img = Image.open("np_array.png")
# np_array_image_arr = np.array(np_array_img)
# print(np_array_image_arr[0][0])

result_image_arr = np.array(png_file)

np_white = np.array([255, 255, 255, 255])
np_black = np.array([0, 0, 0, 0])

color_set = []
white_set = []
for y in range(0, 419):
    for x in range(0, 447):
        temp_list = result_image_arr[y][x].tolist()
        if temp_list not in color_set:
            if temp_list[0] > 200 and temp_list[1] > 200 and temp_list[2] > 200:
                white_set.append(temp_list)
            color_set.append(temp_list)

for y in range(0, 419):
    for x in range(0, 447):
        temp_list = result_image_arr[y][x].tolist()
        if temp_list != [255, 255, 255, 255]:
            result_image_arr[y][x] = np_black
# print(list(color_set))
# print(white_set)
img = Image.fromarray(result_image_arr, "RGBA")
img.save("np_array.png")
# result_image.save("result.png")


# print(tf.version)
