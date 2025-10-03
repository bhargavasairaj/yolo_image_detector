from ultralytics import YOLO
import json
import cv2
from ultralytics.utils.plotting import Annotator  # ultralytics.yolo.utils.plotting is deprecated
import numpy as np
model = YOLO("yolov8m.pt")

def image_detector(image):
    output={}
    results =model.predict(image)
    #single image
    result = results[0]
    for i, r in enumerate(results):
        im_bgr = r.plot()   # image with boxes drawn
        output_path="output.jpg"
        cv2.imwrite(output_path, im_bgr)
    # img_array = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    if result:
        for box in result.boxes:
            cords = box.xyxy[0].tolist()
            class_id = box.cls[0].item()
            conf = box.conf[0].item()
            output[result.names[class_id]] = {"OBJECT TYPE": class_id,"Coordinates" : cords,"PROABABLITY":conf}
            print(output)
            print("Object type:", box.cls)
            print("Coordinates:", box.xyxy)
            print("Probability:", box.conf)
        with open("Detected_Object.json","w") as f:
            json.dump(output,f)
    return output,output_path