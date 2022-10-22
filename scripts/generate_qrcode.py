###  NEED pyqrcoden and pypng libraries to work ###

# check if the libraries are installed

try:
    import pyqrcode
    import png
    content = input("Enter the content of the QR code: ") # get the value of the QR code
    
    # create the QR code
    qr = pyqrcode.create(content)
    
    # save the QR code
    qr.png("qrcode.png", scale=8)

except ImportError:
    print("Please install the libraries first!!!")
    print("pip install pyqrcode pypng")

