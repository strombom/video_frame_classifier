import cv2
import glob
import numpy as np
import contextlib
from PIL import Image
from fastai.data.all import *
from fastai.vision.all import *


def label_func(fname):
    if 'no' in str(fname):
        return 'no'
    else:
        return 'yes'
    
detector = load_learner('detector.pkl')

video_filenames = glob.glob('videos/*.mkv')

for video_filename in video_filenames:
    print("Open video", video_filename)
    date = video_filename[7:-4]
    vidcap = cv2.VideoCapture(video_filename)

    def getFrame(time):
        vidcap.set(cv2.CAP_PROP_POS_MSEC, int(time * 1000))
        has_frame, image = vidcap.read()
        return has_frame, image

    first_detected = False
    progress = 60
    end_time = 10 * 60
    time = 0
    success = True
    while success and time < end_time:
        success, image = getFrame(time)
        if success:
            if time > progress:
                print(progress, "s")
                progress += 60
            with contextlib.redirect_stdout(None):
                detected = detector.predict(image[70:470, 600:1150])[0]
            if detected == 'yes':
                if not first_detected:
                    first_detected = True
                    end_time = min(end_time, time + 2 * 60)
                cv2.imwrite(f"detected/{date}_{time:05}.jpg", image)

        time += 0.5
