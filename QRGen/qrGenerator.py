import qrcode

def generate_qr_code(data, file_name):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save(file_name)

    print(f"QR code saved as {file_name}")

if __name__ == "__main__":
    data = input("Enter the data to encode in the QR code: ")
    file_name = input("Enter the file name to save the QR code (with extension): ")
    generate_qr_code(data, file_name)
