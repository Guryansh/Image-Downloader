import os

os.system("python google-image-generation.py 20 bike outputFolder1")
os.system("python zip.py outputFolder1 outputFolder3.zip")
os.system("python sendToEmail.py outputFolder3.zip guryanshsingla@gmail.com")
