import pyqrcode
import webbrowser
import cv2
import png
import os

try:
# create a QR code object with the URL
    qr = pyqrcode.create('https://www.mcubesolutions.com/')

# create the filename
    filename = "qrcode.png"
    i = 1
    while os.path.exists(filename):
        filename = f"qrcode({i}).png"
        i += 1
    
    # save the QR code as an image
    qr.png(filename, scale=6)
    print(f"QR code saved as {filename}")


# display the QR code
    qr.show()

# read the QR code using OpenCV
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        decoded_objs = pyqrcode.decode(frame)
        for obj in decoded_objs:
            print(f'Decoded QR code: {obj.data}')
            webbrowser.open(obj.data)
            break
        if cv2.waitKey(1) == ord('q'):
            break

# release the webcam
    cap.release()

except Exception as e:
    print(f'Error: {e}')