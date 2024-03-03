import cv2
from cvzone.HandTrackingModule import HandDetector
import mediapipe as mp 
from pynput.keyboard import Controller 
from time import sleep
import math 
# This was a failed intentent 

# This file does not work try file key2.py
cap = cv2.VideoCapture(0) 
mpHands = mp.solutions.hands 
Hands=mpHands.Hands()
mpdraw = mp.solutions.drawing_utils

keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]

ClickedText = ""
keyboard = Controller()
def drawALL(img,buttonList):  # draws the virtaul keyboard (it gives it its shape)

    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
    return img
