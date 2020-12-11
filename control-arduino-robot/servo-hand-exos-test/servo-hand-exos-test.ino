/*************************************************** 
Left and Right Control of 2-servo Hand Exoskeleton
by: Paul Baniqued
Using Keyestudio 16-channel Servo Motor Drive Shield For Arduino
 ****************************************************/

#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

int LeftFingerAngle = 150; // this is the 'minimum' pulse length count (out of 4096)
int LeftThumbAngle = 250;
int RightFingerAngle = 350;
int RightThumbAngle = 250;

int slowly = 10; //slow down servo

void setup() 
{
  Serial.begin(9600);
  pwm.begin();
  
  pwm.setPWMFreq(60);  // Analog servos run at ~60 Hz updates

  pwm.setPWM(0, 0, LeftFingerAngle);
  pwm.setPWM(2, 0, RightFingerAngle);
  
  pwm.setPWM(4, 0, LeftThumbAngle);
  pwm.setPWM(6, 0, RightThumbAngle);
}

void leftClose() // Servo L1, PIN 1 + Servo L2, PIN 2
{
  for (int pos = 0; pos < 100; pos++) 
  {
    pwm.setPWM(0, 0, LeftFingerAngle);
    LeftFingerAngle+=2;

    pwm.setPWM(4, 0, LeftThumbAngle);
    LeftThumbAngle--;
    delay(slowly);
  }
  delay(1000);
  for (int pos = 100; pos > 0; pos--) 
  {
    pwm.setPWM(0, 0, LeftFingerAngle);
    LeftFingerAngle-=2;

    pwm.setPWM(4, 0, LeftThumbAngle);
    LeftThumbAngle++;
    delay(slowly);
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
    delay(slowly);
  }
  delay(1000);
  for (int pos = 100; pos > 0; pos--) 
  {
    pwm.setPWM(2, 0, RightFingerAngle);
    RightFingerAngle+=2;

    pwm.setPWM(6, 0, RightThumbAngle);
    RightThumbAngle--;
    delay(slowly);
  }
  delay(500);
}
void loop() 
{
  leftClose();
  delay(1000);
  rightClose();
  delay(1000);
}
