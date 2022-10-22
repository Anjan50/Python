###  NEED pillow and img2pdf libraries to work ###

# check if the libraries are installed
try:
    import img2pdf
    from PIL import Image, UnidentifiedImageError
    import os

    img_path = input(
        "Enter the path of the image: ")  # get the path of the image

    # open image
    img = Image.open(img_path)
    split_path = img_path.split(
        "\\")  # split the path to get the name of the image
    pdf_path = os.path.join(f"{split_path[0]}\\", *split_path[1:-1],
                            split_path[-1].split(".")[0] +
                            ".pdf")  # create the path of the pdf

    # convert to pdf
    pdf = img2pdf.convert(img.filename)

    # save the pdf
    f = open(pdf_path, "wb")
    f.write(pdf)

    # close the files
    f.close()
    img.close()

except UnidentifiedImageError:
    print("Error: Image not found or cannot be opened")

except IOError as e:
    print("Error: Image not found")
    print(e)

except ImportError:
    print("Please install the libraries first!!!")
