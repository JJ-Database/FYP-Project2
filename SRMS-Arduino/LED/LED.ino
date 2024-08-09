// Define the LED pins
int ledPin = 7;
int ledPin2 = 6;

void setup() {
  // Set the LED pins as outputs
  pinMode(ledPin, OUTPUT);
  pinMode(ledPin2, OUTPUT);
}

void loop() {
  // Turn the first LED on
  digitalWrite(ledPin, HIGH);

  // Turn the second LED on
  digitalWrite(ledPin2, HIGH);
  delay(1000); // Wait for 1 second

  // Turn the first LED off
  digitalWrite(ledPin, LOW);

  // Turn the second LED off
  digitalWrite(ledPin2, LOW);
  delay(1000); // Wait for 1 second
}