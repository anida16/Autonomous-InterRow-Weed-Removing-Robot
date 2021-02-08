/*
  Arduino Slave for Raspberry Pi Master
  i2c_slave_ard.ino
  Connects to Raspberry Pi via I2C

  DroneBot Workshop 2019
  https://dronebotworkshop.com
*/

// Include the Wire library for I2C
#include <Wire.h>

// LED on pin 13
const int ledPin = 13;

void setup() {
  // Join I2C bus as slave with address 8
  Wire.begin(0x8);
  Serial.begin(115200);

  // Call receiveEvent when data received


  // Setup pin 13 as output and turn LED off
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
}

// Function that executes whenever data is received from master
void receiveEvent(int howMany) {
  while (Wire.available()) { // loop through all but the last
    int c = Wire.read(); // receive byte as a character
    //digitalWrite(ledPin, c);
    if (c == 1)
    { digitalWrite(ledPin, LOW);
      Serial.println("Dekh dekh dekh tu yhan whan na fek ..");
    }
    if (c == 2)
    { digitalWrite(ledPin, HIGH);
      Serial.println("Dekh faile gi bimaari hoga sabka bura haal ..");
    }
    if (c == 3)
    { //digitalWrite(ledPin, HIGH);
      digitalWrite(ledPin, HIGH);
      Serial.println("To ka kren bhaiya ?");
    }
    if (c == 4)
    { //digitalWrite(ledPin, HIGH);
      digitalWrite(ledPin, HIGH);
      Serial.println("Gadi wala aaya ghar se kachra nikal ..");
    }
    if (c == 5)
    { //digitalWrite(ledPin, HIGH);
      digitalWrite(ledPin, HIGH);
      Serial.println("Dekh dekh dekh tu yhan whan na fek ..");
    }
    if (c == 6)
    { digitalWrite(ledPin, HIGH);
      Serial.println("Dekh faile gi bimaari hoga sabka bura haal ..");
    }
    if (c == 7)
    { //digitalWrite(ledPin, HIGH);
      digitalWrite(ledPin, HIGH);
      Serial.println("To ka kren bhaiya ?");
    }
    if (c == 8)
    { //digitalWrite(ledPin, HIGH);
      digitalWrite(ledPin, HIGH);
      Serial.println("To ka kren bhaiya ?");
    }
    if (c == 11)
    { //digitlWrite(ledPin, HIGH);
      digitalWrite(ledPin, HIGH);
      Serial.println("raja raja raja raja");
    }
    if (c == 12)
    { //digitlWrite(ledPin, HIGH);
      digitalWrite(ledPin, HIGH);
      Serial.println("raja raja raja raja raja raja raja raja");
    }
    //Serial.println(c);
  }
}
void loop() {
  Wire.onReceive(receiveEvent);
  //delay(1000);
}
