import pytesseract

tesseract_cmd = r'C:\Users\tiago\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts\pytesseract.exe"


print(pytesseract.image_to_string(Image.open('test.png')))