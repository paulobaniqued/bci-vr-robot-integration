/*************************************************** 
Left and Right Control of 2-servo Hand Exoskeleton
by: Paul Baniqued
Using Keyestudio 16-channel Servo Motor Drive Shield For Arduino
 ****************************************************/

#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

int fingerAngle = 150; // this is the 'minimum' pulse length count (out of 4096)
int thumbAngle = 250;

void setup() 
{
  Serial.begin(9600);
  pwm.begin();
  
  pwm.setPWMFreq(60);  // Analog servos run at ~60 Hz updates

  pwm.setPWM(1, 0, fingerAngle);
  pwm.setPWM(2, 0, thumbAngle);
  pwm.setPWM(3, 0, thumbAngle);
  pwm.setPWM(4, 0, fingerAngle);

}

void leftClose() // Servo L1, PIN 1 + Servo L2, PIN 2
{
  for (int pos = 0; pos < 100; pos++) 
  {
    pwm.setPWM(1, 0, fingerAngle);
    fingerAngle++;

    pwm.setPWM(2, 0, thumbAngle);
    thumbAngle--;
  }
  delay(500);
  for (int pos = 100; pos > 0; pos--) 
  {
    pwm.setPWM(1, 0, fingerAngle);
    fingerAngle--;

    pwm.setPWM(2, 0, thumbAngle);
    thumbAngle++;
  }
  delay(500);
}

void rightClose() // Servo R1, PIN 4 + Servo R2, PIN 3
{
  for (int pos = 0; pos < 100; pos++) 
  {
    pwm.setPWM(4, 0, fingerAngle);
    fingerAngle--;

    pwm.setPWM(3, 0, thumbAngle);
    thumbAngle++;
  }
  delay(500);
  for (int pos = 100; pos > 0; pos--) 
  {
    pwm.setPWM(4, 0, fingerAngle);
    fingerAngle++;

    pwm.setPWM(3, 0, thumbAngle);
    thumbAngle--;
  }
  delay(500);
}
void loop() 
{
  leftClose();
  delay(1000);
  rightClose();
  delay(500);
}
