# yolo_image_detector
A simple project using Fast API and yolov8 for detecting the objects in a image and creating bounding box for them..


Run the application using : uvicorn main:app —reload
OPEN : http://127.0.0.1:8000/

STEPS TO RUN:

ON UI it displays a simple tags for uploading the image
Click on Upload
IT will redirect to /upload-image
IT runs the image_dectector → loads the image received via yolo
Yolo medium model - for detecting the object present in the image
Once after detection we will return the JSON with coordinates and image with bounding box
Detection results (objects, type, coordinates, probability)
Processed image
Parallel im saving the both of them as output.jpg and Detected_object.json in the current dir

Why YOLO

These are various detection models which are available

As im on CPU , im on CPU im using the medium model which is best for me 
As I'm focusing on both Accuracy and latency I'm working with the Medium Detection Model here.
