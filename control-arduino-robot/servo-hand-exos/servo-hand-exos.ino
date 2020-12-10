/*************************************************** 
Left and Right Control of 2-servo Hand Exoskeleton
by: Paul Baniqued
Using Keyestudio 16-channel Servo Motor Drive Shield For Arduino
 ****************************************************/

// import Adafruit PWM servo driver
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

// set initial pulse length count (out of 4096)
int LeftFingerAngle = 150;
int LeftThumbAngle = 250;
int RightFingerAngle = 350;
int RightThumbAngle = 250;

int switchState = 0; // initial switch button state
const int ledPin = 13; // the pin the LED is attached to

int incomingByte; // a variable to read incoming serial data into

void setup() 
{
  Serial.begin(9600);
  pwm.begin();
  
  pwm.setPWMFreq(60);  // Analog servos run at ~60 Hz updates

  // pins set in even numbers to provide space in the servo shield
  pwm.setPWM(0, 0, LeftFingerAngle);
  pwm.setPWM(2, 0, RightFingerAngle);
  pwm.setPWM(4, 0, LeftThumbAngle);
  pwm.setPWM(6, 0, RightThumbAngle);

  // Red LED pin
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, HIGH);
}

void leftClose() // Servo L1, PIN 1 + Servo L2, PIN 2
{
  for (int pos = 0; pos < 100; pos++) 
  {
    pwm.setPWM(0, 0, LeftFingerAngle);
    LeftFingerAngle+=2;

    pwm.setPWM(4, 0, LeftThumbAngle);
    LeftThumbAngle--;
  }
  delay(2000);
  for (int pos = 100; pos > 0; pos--) 
  {
    pwm.setPWM(0, 0, LeftFingerAngle);
    LeftFingerAngle-=2;

    pwm.setPWM(4, 0, LeftThumbAngle);
    LeftThumbAngle++;
  }
  delay(500);
}

void rightClose() // Servo R1, PIN 4 + Servo R2, PIN 3
{
  for (int pos = 0; pos < 100; pos++) 
  {
    pwm.setPWM(2, 0, RightFingerAngle);
    RightFingerAngle-=2;

    pwm.setPWM(6, 0, RightThumbAngle);
    RightThumbAngle++;
  }
  delay(2000);
  for (int pos = 100; pos > 0; pos--) 
  {
    pwm.setPWM(2, 0, RightFingerAngle);
    RightFingerAngle+=2;

    pwm.setPWM(6, 0, RightThumbAngle);
    RightThumbAngle--;
  }
  delay(500);
}
void loop() 
{
  // check for incoming serial data

  if (Serial.available() > 0)
  {    
    // read the oldest byte in the serial buffer
    incomingByte = Serial.read();

    switch (incomingByte)
    {
      case 'L': // Close LEFT HAND
        digitalWrite(ledPin, LOW);
        leftClose();
        delay(1000);
        digitalWrite(ledPin, HIGH);
      break;

      case 'R': // Close RIGHT HAND
        digitalWrite(ledPin, LOW);
        rightClose();
        delay(1000);
        digitalWrite(ledPin, HIGH);
      break;
    }
  }
}
