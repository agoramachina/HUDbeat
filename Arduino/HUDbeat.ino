#include <Adafruit_DotStar.h>
#include <SPI.h>         // COMMENT OUT THIS LINE FOR GEMMA OR TRINKET
#ifdef __AVR__
  #include <avr/power.h>
#endif

Adafruit_DotStar dotstar = Adafruit_DotStar(1, INTERNAL_DS_DATA, INTERNAL_DS_CLK, DOTSTAR_BGR);

const int BUTTON_PIN = 0;
const int LED_PIN =  2;
const int SENSOR_PIN = A0;
const int PULSE_LED = INTERNAL_DS_DATA;

int buttonState = 0;    // variable for reading the pushbutton status

int Signal;  // holds the incoming raw data. Signal value can range from 0-1024
int Threshold = 550;  // Determine which Signal to "count as a beat", and which to ingore.

void setup() {
  // button and LED
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);

  // Pulse Sensor
  pinMode(PULSE_LED, OUTPUT);  // pin that will blink to your heartbeat
  Serial.begin(9600);  // set up Serial Communication at certain speed.
  analogReference(AR_DEFAULT);  // set to 3.3 v
  dotstar.begin();  // setup Dotstar

}

void loop() {

  // BUTTON AND LED //
  // read the state of the pushbutton value:
  buttonState = digitalRead(BUTTON_PIN);

  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (buttonState == LOW) {
    // turn LED on:
    digitalWrite(LED_PIN, HIGH);
  } else {
    // turn LED off:
    digitalWrite(LED_PIN, LOW);
  }

  // PULSE SENSOR //
  Signal = analogRead(SENSOR_PIN);
  // Send the Signal value to Serial Plotter.
  Serial.println(Signal);

  // If the signal is above "550", then "turn-on" Arduino's on-Board LED.
  if (Signal > Threshold) {
    //digitalWrite(PULSE_LED, HIGH);
  }
  // Else, the sigal must be below "550", so "turn-off" this LED.
  else {
    //digitalWrite(PULSE_LED, LOW);
  }
  delay(10);

  dotstar.setPixelColor(0, 0, 64, 0); dotstar.show(); 

}
