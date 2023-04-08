# Recognition-of-Road-Sign-Using-CNN

Recognition of Road Signs Using Convolutional Neural Network

This research suggested utilizing a convolutional approach to implement 
road sign recognition and it focused on dealing with uploading an image and
quickly identifying which kind of road sign is present in which class of an input image.
Generally, this study aimed to develop a web application that uses a Convolutional Neural Network(CNN) algorithm to recognize road sign images.

// you can download the road signs model and dataset from the link below:
https://drive.google.com/drive/folders/1A9cVQzbHdvUzhgn1rBKKTekBtzEAFlrL?usp=share_link

STEPS TO RUN:
/ Install all the dependencies.
- First, install all the libraries and modules that are needed in the system 
install it using/in CMD. (use "pip install" while installing) 
### load modules for the system
	 - import numpy as np
	 - import os
	 - import PIL
	 - import tensorflow as tf
	 - import pathlib

### Flask app
	 - from flask import Flask
	 - from flask import request
	 - from flask import render_template
	 - import base64
	 - from PIL import Image
	 - import pandas as pd
	 - import cv2
	(install also JUPYTER NOTEBOOK in CMD)
 
- Second, after installing all needed in the system you can now run Road Sign Model in CMD and open CNN.ipnyb.
 

HOW TO RUN ROAD SIGN MODEL IN CMD
•	Open the Road Sign Model 1 or 2
•	Copy the URL address after opening it, or just type CMD there in the URL address and press Enter.
•	Or Run it on CMD 
•	After that type JUPYTER NOTEBOOK (wait for few minutes)
•	Then open CNN.ipnyb (you can now edit/retrain/debug the model)

HOW TO RUN FLASK APP IN CMD (Recognition of Road Sign Prototype)
•	Open the Road Sign Model 1 or 2
•	After opening click the web folder
•	Copy the URL address after opening it, or just type CMD there in the URL address and press Enter.
•	When the CMD is open just type python app.py (wait for few minutes while running the file)
•	After it finish running look for the link 127.0.0.1:5000 below.
•	127.0.0.1:5000 copy this link and paste in on the Microsoft edge and click enter.
•	It will automatically open the RECOGNITION OF ROAD SIGN 
WEB APPLICATION PROTOTYPE. (you can now upload road sign images in the flask app.)

*** System/Prototype should be restarted when there are changes in source code.
