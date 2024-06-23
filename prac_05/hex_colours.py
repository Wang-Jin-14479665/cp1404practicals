"""
CP1404 Practical
color code in a dictionary
Estimate: 30 minutes
Actual:   20 minutes
"""

COLOR_TO_HEX = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff"
}


longest_color_length = max(len(color) for color in COLOR_TO_HEX)

for color, hex_code in COLOR_TO_HEX.items():
    print(f"color {color:<{longest_color_length}} Hex code: {hex_code}")

color = input("Enter a color: ").lower()
while color != "":
    try:
        print(color, "Hex code: ", COLOR_TO_HEX[color])
    except KeyError:
        print("Invalid color")
    color = input("Enter a color: ").lower()
