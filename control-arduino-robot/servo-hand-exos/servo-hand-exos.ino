/*************************************************** 
Left and Right Control of 2-servo Hand Exoskeleton
by: Paul Baniqued
Using Keyestudio 16-channel Servo Motor Drive Shield For Arduino
 ****************************************************/

#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

// called this way, it uses the default address 0x40
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
// you can also call it with a different address you want
//Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x41);

// Depending on your servo make, the pulse width min and max may vary, you 
// want these to be as small/large as possible without hitting the hard stop
// for max range. You'll have to tweak them as necessary to match the servos you
// have!
#define SERVOMIN  150 // this is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  600 // this is the 'maximum' pulse length count (out of 4096)

// our servo # counter
//uint8_t servonum = 0;

void setup() {
  Serial.begin(9600);
  Serial.println("16 channel Servo test!");

  pwm.begin();
  
  pwm.setPWMFreq(60);  // Analog servos run at ~60 Hz updates
}

// you can use this function if you'd like to set the pulse length in seconds
// e.g. setServoPulse(0, 0.001) is a ~1 millisecond pulse width. its not precise!
void setServoPulse(uint8_t n, double pulse) {
  double pulselength;
  
  pulselength = 1000000;   // 1,000,000 us per second
  pulselength /= 60;   // 60 Hz
  Serial.print(pulselength); Serial.println(" us per period"); 
  pulselength /= 4096;  // 12 bits of resolution
  Serial.print(pulselength); Serial.println(" us per bit"); 
  pulse *= 1000;
  pulse /= pulselength;
  Serial.println(pulse);
  pwm.setPWM(n, 0, pulse);
}

void loop() {
  // Drive each servo one at a time
  //Serial.println(servonum);
  for (uint16_t pulselen = SERVOMIN; pulselen < SERVOMAX; pulselen++) {
    pwm.setPWM(0, 0, pulselen);
    pwm.setPWM(1, 0, pulselen);
    pwm.setPWM(2, 0, pulselen);
    pwm.setPWM(3, 0, pulselen);
    pwm.setPWM(4, 0, pulselen);
    pwm.setPWM(5, 0, pulselen);
    pwm.setPWM(6, 0, pulselen);
    pwm.setPWM(7, 0, pulselen);
    pwm.setPWM(8, 0, pulselen);
    pwm.setPWM(9, 0, pulselen);
    pwm.setPWM(10, 0, pulselen);
    pwm.setPWM(11, 0, pulselen);
    pwm.setPWM(12, 0, pulselen);
    pwm.setPWM(13, 0, pulselen);
    pwm.setPWM(14, 0, pulselen);
  }
  delay(500);
  for (uint16_t pulselen = SERVOMAX; pulselen > SERVOMIN; pulselen--) {
    pwm.setPWM(0, 0, pulselen);
    pwm.setPWM(0, 0, pulselen);
    pwm.setPWM(1, 0, pulselen);
    pwm.setPWM(2, 0, pulselen);
    pwm.setPWM(3, 0, pulselen);
    pwm.setPWM(4, 0, pulselen);
    pwm.setPWM(5, 0, pulselen);
    pwm.setPWM(6, 0, pulselen);
    pwm.setPWM(7, 0, pulselen);
    pwm.setPWM(8, 0, pulselen);
    pwm.setPWM(9, 0, pulselen);
    pwm.setPWM(10, 0, pulselen);
    pwm.setPWM(11, 0, pulselen);
    pwm.setPWM(12, 0, pulselen);
    pwm.setPWM(13, 0, pulselen);
    pwm.setPWM(14, 0, pulselen);
  }
  delay(500);

}
