#include <Wire.h>

#define SLAVE_ADDRESS 0x08
int incomingByte = 0;
volatile boolean xbox_sending = false;
int xbox_says;
String command;


void setup() {
  // initialize i2c as slave
  Wire.begin(SLAVE_ADDRESS);

  // define callbacks for i2c communication
  Wire.onReceive(receiveEvent);

  Serial.begin(115200);
  Serial.println("Ready!");

}

void loop() {
 
  if (xbox_sending == true) {
    
    if (xbox_says == 1)
    {
      Serial.println("Sex BC");
    }
      if (xbox_says == 3)
    {
      Serial.println("Maa chudi padi hai");
    }
    xbox_sending = false;
  }
  
}


void receiveEvent(int howMany) {

  for (int i = 0; i < howMany; i++) {
    xbox_says = Wire.read();
   // temp[i + 1] = '  '; //add null after ea. char
  }

  xbox_sending = true;
}
