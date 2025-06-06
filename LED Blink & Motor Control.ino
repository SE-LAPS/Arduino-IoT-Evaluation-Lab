const int ledPin = 9;

void setup() {
  pinMode(ledPin, OUTPUT);
  // Motor is powered continuously from 5V; no digital control here.
}

void loop() {
  digitalWrite(ledPin, HIGH);  // Turn LED ON
  delay(1000);                 // 1 second
  digitalWrite(ledPin, LOW);   // Turn LED OFF
  delay(1000);                 // 1 second
  // Motor remains ON whenever Arduino is powered
}