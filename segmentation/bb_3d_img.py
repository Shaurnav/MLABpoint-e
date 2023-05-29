import mediapipe as mp
import cv2
import numpy as np
import matplotlib.pyplot as plt
import PIL
import urllib

def url_to_array(url):
    req = urllib.request.urlopen(url)
    arr = np.array(bytearray(req.read()), dtype=np.int8)
    arr = cv2.imdecode(arr, -1)
    arr = cv2.cvtColor(arr, cv2.COLOR_BGR2RGB)
    return arr

mug = 'https://goodstock.photos/wp-content/uploads/2018/01/Laptop-Coffee-Mug-on-Table.jpg'
mug = url_to_array(mug)

mp_objectron = mp.solutions.objectron
mp_drawing = mp.solutions.drawing_utils

# Instantiation
objectron = mp_objectron.Objectron(
    static_image_mode=True,
    max_num_objects=5,
    min_detection_confidence=0.2,
    model_name='Cup')

# Inference
results = objectron.process(mug)

if not results.detected_objects:
    print(f'No box landmarks detected.')

# Copy image so as not to draw on the original one
annotated_image = mug.copy()
for detected_object in results.detected_objects:
    # Draw landmarks
    mp_drawing.draw_landmarks(annotated_image, 
                              detected_object.landmarks_2d, 
                              mp_objectron.BOX_CONNECTIONS)

    # Draw axis based on rotation and translation
    mp_drawing.draw_axis(annotated_image, 
                         detected_object.rotation, 
                         detected_object.translation)
  
# Plot result
fig, ax = plt.subplots(figsize=(10, 10))
ax.imshow(annotated_image)
ax.axis('off')
plt.show()