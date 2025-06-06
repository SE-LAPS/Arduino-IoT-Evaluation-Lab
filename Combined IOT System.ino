#include DHT.h

 Ultrasonic pins
const int trigPin = 7;
const int echoPin = 6;

 DHT22 pins
#define DHTPIN 2
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

 LED pin
const int ledPin = 9;

 Motor control (we'll simulate motor ONOFF by digital pin driving,
 but the motor is actually connected to 5V; for safety, we use a transistor pin or relay).
 For this example, we assume a transistordriver circuit on D3
const int motorControlPin = 3;

void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(ledPin, OUTPUT);
  pinMode(motorControlPin, OUTPUT);
  
   Initialize sensors
  dht.begin();
  
   Start with motor ON
  digitalWrite(motorControlPin, HIGH);
}

void loop() {
   --- Part 1 Distance measurement ---
  long duration, distanceCm;
  
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH);
  distanceCm = duration  0.034  2;
  
   Print distance
  Serial.print(Distance );
  Serial.print(distanceCm);
  Serial.print( cmt);
  
   Blink LED if object  10 cm
  if (distanceCm  10) {
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }
  
   --- Part 2 DHT22 reading ---
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();
  
  if (isnan(humidity)  isnan(temperature)) {
    Serial.println(DHT22 Error);
  } else {
    Serial.print(Temp );
    Serial.print(temperature);
    Serial.print( °C  Humidity );
    Serial.print(humidity);
    Serial.println( %);
  }
  
   --- Part 3 Motor control based on humidity ---
  if (humidity  80.0) {
     Turn motor OFF
    digitalWrite(motorControlPin, LOW);
    Serial.println(Motor OFF (High Humidity));
  } else {
     Turn motor ON
    digitalWrite(motorControlPin, HIGH);
    Serial.println(Motor ON);
  }
  
  delay(2000);  Wait 2 seconds between cycles
}