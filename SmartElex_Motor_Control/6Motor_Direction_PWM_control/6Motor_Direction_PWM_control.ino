int dir1 = 50; //Motor 1 Direction Pin
int dir2 = 48; //Motor 2 Direction Pin
int dir3 = 46; //Motor 3 Direction Pin
int dir4 = 44; //Motor 4 Direction Pin
int dir5 = 42; //Motor 5 Direction Pin
int dir6 = 40; //Motor 6 Direction Pin

int pwm1 = 2; //Motor 1 PWM Pin
int pwm2 = 3; //Motor 2 PWM Pin
int pwm3 = 4; //Motor 3 PWM Pin
int pwm4 = 5; //Motor 4 PWM Pin
int pwm5 = 6; //Motor 5 PWM Pin
int pwm6 = 7; //Motor 6 PWM Pin


void setup() {
pinMode(pwm1, OUTPUT);
pinMode(pwm2, OUTPUT);
pinMode(pwm3, OUTPUT);
pinMode(pwm4, OUTPUT);
pinMode(pwm5, OUTPUT);
pinMode(pwm6, OUTPUT);

pinMode(dir1, OUTPUT);
pinMode(dir2, OUTPUT);
pinMode(dir3, OUTPUT);
pinMode(dir4, OUTPUT);
pinMode(dir5, OUTPUT);
pinMode(dir6, OUTPUT);

Serial.begin(115200);
}

void loop() {
forward(255);
Serial.println("Forward");
delay(4000);
brake();
Serial.println("Brake");
delay(1000);
reverse(255);
Serial.println("Reverse");
delay(4000);
brake();
Serial.println("Brake");
delay(1000);
clock_wise(255);
Serial.println("Clockwise");
delay(4000);
brake();
Serial.println("Brake");
delay(1000);
anticlock_wise(255);
Serial.println("AntiClockwise");
delay(4000);
brake();
Serial.println("Brake");
delay(1000);

}

void forward(int pwm) {
  digitalWrite(dir1, HIGH);
  digitalWrite(dir2, HIGH);
  digitalWrite(dir3, HIGH);
  digitalWrite(dir4, LOW);
  digitalWrite(dir5, LOW);
  digitalWrite(dir6, LOW);
  
  analogWrite(pwm1, pwm);
  analogWrite(pwm2, pwm);
  analogWrite(pwm3, pwm);
  analogWrite(pwm4, pwm);
  analogWrite(pwm5, pwm);
  analogWrite(pwm6, pwm);
}

void reverse(int pwm) {
  digitalWrite(dir1, LOW);
  digitalWrite(dir2, LOW);
  digitalWrite(dir3, LOW);
  digitalWrite(dir4, HIGH);
  digitalWrite(dir5, HIGH);
  digitalWrite(dir6, HIGH);
  
  analogWrite(pwm1, pwm);
  analogWrite(pwm2, pwm);
  analogWrite(pwm3, pwm);
  analogWrite(pwm4, pwm);
  analogWrite(pwm5, pwm);
  analogWrite(pwm6, pwm);
}

void brake() {
  digitalWrite(dir1, LOW);
  digitalWrite(dir2, LOW);
  digitalWrite(dir3, LOW);
  digitalWrite(dir4, LOW);
  digitalWrite(dir5, LOW);
  digitalWrite(dir6, LOW);
  
  analogWrite(pwm1, 0);
  analogWrite(pwm2, 0);
  analogWrite(pwm3, 0);
  analogWrite(pwm4, 0);
  analogWrite(pwm5, 0);
  analogWrite(pwm6, 0);
}

void clock_wise(int pwm) {
  digitalWrite(dir1, HIGH);
  digitalWrite(dir2, HIGH);
  digitalWrite(dir3, HIGH);
  digitalWrite(dir4, HIGH);
  digitalWrite(dir5, HIGH);
  digitalWrite(dir6, HIGH);
  
  analogWrite(pwm1, pwm);
  analogWrite(pwm2, pwm);
  analogWrite(pwm3, pwm);
  analogWrite(pwm4, pwm);
  analogWrite(pwm5, pwm);
  analogWrite(pwm6, pwm);
}

void anticlock_wise(int pwm) {
  digitalWrite(dir1, LOW);
  digitalWrite(dir2, LOW);
  digitalWrite(dir3, LOW);
  digitalWrite(dir4, LOW);
  digitalWrite(dir5, LOW);
  digitalWrite(dir6, LOW);
  
  analogWrite(pwm1, pwm);
  analogWrite(pwm2, pwm);
  analogWrite(pwm3, pwm);
  analogWrite(pwm4, pwm);
  analogWrite(pwm5, pwm);
  analogWrite(pwm6, pwm);
}
