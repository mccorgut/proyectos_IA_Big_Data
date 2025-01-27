import numpy as np
import cv2


def anonymize_face(buffer, response):
    # Read image from buffer
    nparr = np.fromstring(buffer, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    height, width, _ = img.shape

    for faceDetail in response['FaceDetails']:
        box = faceDetail['BoundingBox']
        x = int(width * box['Left'])
        y = int(height * box['Top'])
        w = int(width * box['Width'])
        h = int(height * box['Height'])

        # Get region of interest
        roi = img[y:y + h, x:x + w]

        # Applying a gaussian blur over this new rectangle area
        roi = cv2.GaussianBlur(roi, (83, 83), 30)

        # Impose this blurred image on original image to get final image
        img[y:y + roi.shape[0], x:x + roi.shape[1]] = roi

    print("Blurred face task has been successfully run")

    # Encode image and return image with blurred faces
    _, res_buffer = cv2.imencode('.jpg', img)
    return res_buffer
