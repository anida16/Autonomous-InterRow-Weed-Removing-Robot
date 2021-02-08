int dir1 = 23;
int pwm1 = 2;



void setup() {
pinMode(pwm1, OUTPUT);
pinMode(dir1, OUTPUT);
Serial.begin(115200);
}

void loop() {
digitalWrite(dir1, HIGH); 
analogWrite(pwm1,50);
Serial.println("Direction 1");
delay(5000);
digitalWrite(dir1, LOW);
analogWrite(pwm1,0);
Serial.println("Stop");
delay(5000);
digitalWrite(dir1, LOW);
analogWrite(pwm1,50);
Serial.println("Direction 2");
delay(5000);

}
