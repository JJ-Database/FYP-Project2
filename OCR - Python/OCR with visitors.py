import cv2
import pytesseract
from PIL import Image
import pyrebase
import re
import os
import time
from datetime import datetime

# Firebase configuration
config = {
    "apiKey": "AIzaSyDUrwSd3rJvJKe0gOG5E0U68ow-fPGOLPA",
    "authDomain": "loginhtml-b6a38.firebaseapp.com",
    "databaseURL": "https://loginhtml-b6a38-default-rtdb.firebaseio.com",
    "projectId": "loginhtml-b6a38",
    "storageBucket": "loginhtml-b6a38.appspot.com",
    "messagingSenderId": "888243437180",
    "appId": "1:888243437180:web:5faad9d368f11ee6b1d3f9",
    "measurementId": "G-VXJT8PMFPF"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
db = firebase.database()

# Define the path to save the captured image
local_image_dir = r"C:\Users\ASUS\Downloads\carPlate"
local_image_filename = "captured_image.jpg"
local_image_path = os.path.join(local_image_dir, local_image_filename)

def generate_car_id():
    """Generate a unique carID in the format C0001-C9999."""
    for i in range(1, 10000):
        car_id = f"C{i:04d}"
        if not db.child("cars").child(car_id).get().val():
            return car_id
    raise ValueError("All car IDs are taken.")

def generate_visitor_id():
    """Generate a unique visitorID in the format V0001-V9999."""
    for i in range(1, 10000):
        visitor_id = f"V{i:04d}"
        if not db.child("visitors").child(visitor_id).get().val():
            return visitor_id
    raise ValueError("All visitor IDs are taken.")

def is_authorized_vehicle(plate_number):
    """Check if the extracted plate number matches any carPlateNumber in Firebase."""
    cars = db.child("vehicles").get()
    for car in cars.each():
        if car.val().get("carPlateNumber") == plate_number:
            return True
    return False

def is_approved_visitor(plate_number):
    """Check if the extracted plate number matches any approved visitor for today."""
    today = datetime.now().strftime("%d/%m/%Y")
    visitors = db.child("visitors").get()
    for visitor in visitors.each():
        if (visitor.val().get("status") == "approved" and
                visitor.val().get("visitDate") == today and
                visitor.val().get("vehicleNumber") == plate_number):
            return True
    return False

def preprocess_image(image_path):
    """Preprocess the image for better OCR accuracy."""
    image = cv2.imread(image_path)
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur to remove noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # Apply thresholding to get a binary image
    _, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return binary

def filter_text(text):
    """Filter the text to include only uppercase alphanumeric characters."""
    # Convert text to uppercase
    text = text.upper()
    # Remove any non-alphanumeric characters
    text = re.sub(r'[^A-Z0-9]', '', text)
    return text

try:
    # Ensure the local directory exists before attempting to download
    if not os.path.exists(local_image_dir):
        os.makedirs(local_image_dir)

    # Capture an image using the webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open the camera.")
        exit()

    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame from the camera.")
        cap.release()
        exit()

    # Save the captured image to the specified path
    cv2.imwrite(local_image_path, frame)
    cap.release()

    # Indicate successful image capture
    print("Image captured successfully.")

    # Preprocess the image
    preprocessed_image = preprocess_image(local_image_path)
    preprocessed_image_path = os.path.join(local_image_dir, "preprocessed_image.jpg")
    cv2.imwrite(preprocessed_image_path, preprocessed_image)

    # Upload the captured image to Firebase Storage
    storage.child(local_image_filename).put(local_image_path)

    # Load the preprocessed image and perform OCR
    image = Image.open(preprocessed_image_path)
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(image, config=custom_config).strip()

    # Filter the extracted text
    text = filter_text(text)

    # Handle cases where text extraction is null or empty
    if not text:
        text = "No text extracted"

    # Check if the vehicle is authorized or if it's an approved visitor
    if is_authorized_vehicle(text):
        entity = "car"
        authorization_status = "authorized"
        entity_id = generate_car_id()
    elif is_approved_visitor(text):
        entity = "visitor"
        authorization_status = "approved"
        entity_id = generate_visitor_id()
    else:
        entity = "car"
        authorization_status = "unauthorized"
        entity_id = generate_car_id()

    # Store the extracted text and authorization status in Firebase Realtime Database
    data = {
        "ID": entity_id,
        "plateNumber": text,
        "status": authorization_status
    }
    db.child(entity + "s").child(entity_id).set(data)

    # Update the barrier value in Firebase
    barrier_value = 1 if authorization_status in ["authorized", "approved"] else 0
    db.child("barrier").child("value").set(barrier_value)

    if authorization_status in ["authorized", "approved"]:
        # Wait for 5 seconds
        time.sleep(5)
        # Set the barrier value back to 0
        db.child("barrier").child("value").set(0)

    # Print the entity ID, extracted data, and authorization status
    print(f"Data extracted and saved to Firebase ({entity}):")
    print("ID:", entity_id)
    print("plateNumber:", text)
    print("status:", authorization_status)

except Exception as e:
    print("An error occurred:", e)
