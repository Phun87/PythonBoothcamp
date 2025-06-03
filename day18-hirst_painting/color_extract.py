import colorgram

colors_list = []
colors = colorgram.extract("image.jpg", 38)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    colors_list.append(new_color)
print(colors_list)