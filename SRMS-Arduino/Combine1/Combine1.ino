#include <Servo.h>

// Define the servo pin
int servoPin = 8;

// Define the LED pins
int ledOnPin = 7;
int ledOffPin = 6;

// Create a Servo object
Servo myServo;

// Define the status
String status = ""; // Initialize as an empty string

// Variable to track if the sequence has been executed
bool hasMoved = false;

void setup() {
  // Start the Serial communication
  Serial.begin(9600);

  // Attach the servo to the pin
  myServo.attach(servoPin);

  // Set LED pins as outputs
  pinMode(ledOnPin, OUTPUT);
  pinMode(ledOffPin, OUTPUT);

  // Ensure LEDs are off initially
  digitalWrite(ledOnPin, LOW);
  digitalWrite(ledOffPin, LOW);
}

void loop() {
  // Check if data is available on the Serial input
  if (Serial.available() > 0) {
    // Read the incoming string
    status = Serial.readStringUntil('\n');
    status.trim(); // Remove any extra whitespace or newline characters

    // Reset the hasMoved flag if status changes
    hasMoved = false;
  }

  // Check the status and if the sequence has not been executed
  if (status == "ON" && !hasMoved) {
    // Light up the LED on pin 7
    digitalWrite(ledOnPin, HIGH);
    digitalWrite(ledOffPin, LOW);

    // Perform the servo movement sequence
    myServo.write(90);          // Move the servo to 90 degrees
    delay(1000);               // Wait for 1 second

    myServo.write(0);         // Move the servo to 0 degrees
    delay(1000);               // Wait for 1 second

    delay(5000);               // Wait for 5 seconds

    myServo.write(0);          // Move the servo back to 0 degrees
    delay(1000);               // Wait for 1 second

    myServo.write(90);         // Move the servo to 90 degrees
    delay(1000);               // Wait for 1 second

    // Set the flag to indicate the sequence has been executed
    hasMoved = true;

    // Ensure LEDs are turned off after the sequence is done
    digitalWrite(ledOnPin, LOW);
  } else if (status != "ON") {
    // If status is not "ON", light up the LED on pin 6
    digitalWrite(ledOnPin, LOW);
    digitalWrite(ledOffPin, HIGH);
  }

  // You can add other code here if needed
}
