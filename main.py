class Screen:
    def __init__(self):
        self.pixels = []
        while len(self.pixels) < 7:  # While less rows than screen
            self.pixels.append([])
            while len(self.pixels[-1]) < 17:
                self.pixels[-1].append([0, 0, 0])  # Add 0 0 0 rgb values for each pixel

    def display(self):
        return self.pixels

    def set_pixel(self, x, y, r, g, b):
        self.pixels[x][y] = [r, g, b]
        return x, y, r, g, b


def print_screen():
    screen = Screen()
    screen.set_pixel(1, 1, 10, 10, 255)
    # character = 9632
    character = 9608

    for row in screen.display():
        for pixel in row:
            code = "[38;2;" + str(pixel[0]) + ";" + str(pixel[1]) + ";" + str(pixel[2]) + "m"
            print(f"\u001b{code}{chr(character)}\u001b[0m", end="", flush=True)
        print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_screen()
