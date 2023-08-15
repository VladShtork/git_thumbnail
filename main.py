from PIL import Image


def main():
    im = Image.open("16. Город.jpg")
    print(im.format, im.size, im.mode)

    size = (128, 128)
    outfile = "16. Город_thumbnail.jpg"

    im.thumbnail(size)
    im.save(outfile, "PNG")

    newfile = Image.open(outfile)
    print(newfile.format, newfile.size, newfile.mode)


if __name__ == '__main__':
    main()main.py