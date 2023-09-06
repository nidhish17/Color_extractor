# import cv2
from colorthief import ColorThief
# import matplotlib.pyplot as plt
# import numpy as np
# from PIL import Image
#
# from collections import Counter


def color_extractor(image_file, color_count=10):

    try:
        ct = ColorThief(image_file)

        ten_colors = ct.get_palette(color_count=color_count+1)
        # print(ten_colors)
        # plt.imshow([[ten_colors[i] for i in range(10)]])
        # plt.show()
        hex_code = []

        most_dominant_color = ct.get_palette(quality=2)[0]

        for color in ten_colors:
            hex_code.append(f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}")

        # print(hex_code)
        dominant_color_hex = f"#{most_dominant_color[0]:02x}{most_dominant_color[1]:02x}{most_dominant_color[2]:02x}"

        return [hex_code, dominant_color_hex]
    # return hex_code
    except Exception as e:
        print(e)
        return "error"

# print(color_distance( (255, 76, 0), (198, 0, 50) ))




#
# print(color_extractor("images/yiren.jpg"))


# print("-------------------vs------------------------------------")
#counting 10 most common colors
#
# colors_in_img = []
#
# for color in pixels:
#     colors_in_img.append(tuple(color))
#
# # print(Counter(colors_in_img).most_common(10))
#
# #turtle counter
#
# rgb_colors = {}
#
# for color in colors_in_img:
#     if color in rgb_colors:
#         rgb_colors[color] += 1
#     else:
#         rgb_colors[color] = 1
#
# sorted_dict = dict(sorted(rgb_colors.items(), key=lambda item: item[1], reverse=True))
#
# print(sorted_dict)
