/*
  MPU-9250 Accel, Gryro and Mag Test Program

  This  program reads and prints to the Serial Monitor window
  the raw X/Y/Z values for the accelerometer, gyroscope, magnetometer
  and temperature.  It also calculates the pitch and roll values

  Connect VCC to 5V and GND to ground on the MCU
  Connect SCL to SCL and SDA to SDA on MCU

  Uses Bolder Flight MPU9250.h library
*/
#include "MPU9250.h"
// an MPU9250 object with the MPU-9250 sensor on I2C bus 0 with address 0x68
MPU9250 IMU(Wire, 0x68);
int status;
float AcX, AcY, AcZ;
float pitch, roll;
//===============================================================================
//  Initialization
//===============================================================================
void setup() {
  // serial to display data
  Serial.begin(115200);
  while (!Serial) {}

  // start communication with IMU
  status = IMU.begin();
  if (status < 0) {
    Serial.println("IMU initialization unsuccessful");
    Serial.println("Check IMU wiring or try cycling power");
    Serial.print("Status: ");
    Serial.println(status);
    while (1) {}
  }
}
//===============================================================================
//  Main
//===============================================================================
void loop() {
  // read the sensor
  IMU.readSensor();
  // display the data
  Serial.println("\tX\tY\tZ");
  Serial.print("Accel:\t");
  Serial.print(IMU.getAccelX_mss(), 3);
  Serial.print("\t");
  Serial.print(IMU.getAccelY_mss(), 3);
  Serial.print("\t");
  Serial.println(IMU.getAccelZ_mss(), 3);

  Serial.print("Gyro:\t");
  Serial.print(IMU.getGyroX_rads(), 3);
  Serial.print("\t");
  Serial.print(IMU.getGyroY_rads(), 3);
  Serial.print("\t");
  Serial.println(IMU.getGyroZ_rads(), 3);

  Serial.print("Mag:\t");
  Serial.print(IMU.getMagX_uT(), 3);
  Serial.print("\t");
  Serial.print(IMU.getMagY_uT(), 3);
  Serial.print("\t");
  Serial.println(IMU.getMagZ_uT(), 3);

  Serial.print("Temp:\t");
  Serial.println(IMU.getTemperature_C(), 3);

  AcX = IMU.getAccelX_mss();
  AcY = IMU.getAccelY_mss();
  AcZ = IMU.getAccelZ_mss();
  //get pitch/roll
  getAngle(AcX, AcY, AcZ);

  Serial.println("\tAngle in Degrees");
  Serial.print("Pitch:\t");
  Serial.println(pitch, 6);
  Serial.print("Roll:\t");
  Serial.println(roll, 6);
  Serial.println();
  delay(250);
}
//===============================================================================
//  GetAngle - Converts accleration data to pitch & roll
//===============================================================================
void getAngle(float Vx, float Vy, float Vz) {
  float x = Vx;
  float y = Vy;
  float z = Vz;
  pitch = atan(x / sqrt((y * y) + (z * z)));
  roll = atan(y / sqrt((x * x) + (z * z)));
  //convert radians into degrees
  pitch = pitch * (180.0 / 3.14);
  roll = roll * (180.0 / 3.14) ;
}
