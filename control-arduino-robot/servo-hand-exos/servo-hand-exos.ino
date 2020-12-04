/*************************************************** 
Left and Right Control of 2-servo Hand Exoskeleton
by: Paul Baniqued
Using Keyestudio 16-channel Servo Motor Drive Shield For Arduino
 ****************************************************/

#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

#define FINGERMIN  150 // this is the 'minimum' pulse length count (out of 4096)
#define FINGERMAX  250 // this is the 'maximum' pulse length count (out of 4096)
#define THUMBMIN 200
#define THUMBMAX 250

void setup() 
{
  Serial.begin(9600);
  Serial.println("16 channel Servo test!");

  pwm.begin();
  pwm.setPWMFreq(60);  // Analog servos run at ~60 Hz updates

}

void leftFingerClose() // Servo L1, PIN 1
{
  for (int finger_pos = FINGERMIN; finger_pos < FINGERMAX; finger_pos++) 
  {
    pwm.setPWM(1, 0, finger_pos);
  }
  delay(500);
  for (int finger_pos = FINGERMAX; finger_pos > FINGERMIN; finger_pos--) 
  {
    pwm.setPWM(1, 0, finger_pos);
  }
  delay(500);
}

void leftThumbClose() // Servo L2, PIN 2
{
  for (int thumb_pos = THUMBMAX; thumb_pos > THUMBMIN; thumb_pos--) 
  {
    pwm.setPWM(2, 0, thumb_pos);
  }
  delay(500);
  for (int thumb_pos = THUMBMIN; thumb_pos < THUMBMAX; thumb_pos++) 
  {
    pwm.setPWM(2, 0, thumb_pos);
  }
  delay(500);
}

void rightThumbClose() // Servo R2, PIN 3
{
  for (int thumb_pos = THUMBMIN; thumb_pos < THUMBMAX; thumb_pos++) 
  {
    pwm.setPWM(3, 0, thumb_pos);
  }
  delay(500);
  for (int thumb_pos = THUMBMAX; thumb_pos > THUMBMIN; thumb_pos--) 
  {
    pwm.setPWM(3, 0, thumb_pos);
  }
  delay(500);
}

void rightFingerClose() // Servo R1, PIN 4 
{
  for (int finger_pos = FINGERMAX; finger_pos > FINGERMIN; finger_pos--) 
  {
    pwm.setPWM(4, 0, finger_pos);
  }
  delay(500);
  for (int finger_pos = FINGERMIN; finger_pos < FINGERMAX; finger_pos++) 
  {
    pwm.setPWM(4, 0, finger_pos);
  }
  delay(500);
}


void loop() 
{
  leftFingerClose();
  leftThumbClose();
  rightThumbClose();
  rightFingerClose();
  delay(1000);
}
