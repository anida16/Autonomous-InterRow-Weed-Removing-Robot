#include <Wire.h>

//const int ledPin = 13;
void setup() {

Serial.begin(115200);
Wire.begin(0x08);
Wire.onReceive(receiveEvent);

pinMode(LED_BUILTIN, OUTPUT);
}


void receiveEvent(int howMany) {
  while(Wire.available()) {
    Serial.println("Inside LOOP");
    int c = Wire.read();
    Serial.println(c);
    
    if (c == 1){
      digitalWrite(LED_BUILTIN, HIGH);}
    else {
      digitalWrite(LED_BUILTIN, LOW);}
}
}

void loop() {
delay(100);

}
