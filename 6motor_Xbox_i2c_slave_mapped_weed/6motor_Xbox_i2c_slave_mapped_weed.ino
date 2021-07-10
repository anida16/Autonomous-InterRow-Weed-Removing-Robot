
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

int jetson_cooling = 9;

int weeding_up = 10;
int weeding_down = 11;
int solenoid = 12;
int pwm;
volatile boolean xbox_sending = false;
int xbox_says;
int heading_angle;
double pwm_map;
int Final_pwm_360;
double pwm_map_360;
double pwm_map_temp_360;
int Final_pwm_90;
double pwm_map_90;
double pwm_map_temp_90;
int Final_pwm_270;
double pwm_map_270;
double pwm_map_temp_270;
int Final_pwm_180;
double pwm_map_180;
double pwm_map_temp_180;
#include <Wire.h>

void setup() {

  Wire.begin(0x8);
  Wire.onReceive(receiveEvent);

  pinMode(weeding_up, OUTPUT);
  pinMode(weeding_down, OUTPUT);
pinMode(solenoid, OUTPUT);
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

  //pinMode(jetson_cooling, OUTPUT);

  Serial.begin(115200);
  digitalWrite(weeding_up, HIGH);
  digitalWrite(weeding_down, HIGH);
  digitalWrite(solenoid, HIGH);
}

void loop() {


  if (xbox_sending == true) {

    ///////////////////////////////////////////////////////////////
    ///////////////////////Xbox Buttons Section/////////////////////
    //digitalWrite(solenoid, HIGH);
    
    if (xbox_says == 1) //Button A
    {
      Serial.println("Button A");
      digitalWrite(weeding_up, HIGH);
      digitalWrite(weeding_down, LOW);
    }

    if (xbox_says == 2) //Button B
    {
      Serial.println("Button B");
      digitalWrite(weeding_up, LOW);
      digitalWrite(weeding_down, HIGH);
    }

    if (xbox_says == 3) //Button X
    {
      Serial.println("Button X");
      //digitalWrite(solenoid, LOW);
    }

    if (xbox_says == 4) //Button Y
    {
      Serial.println("Button Y");
    }

    if (xbox_says == 5) //Dpad Up
    {
      forward();
      Serial.println("Dpad Up");
    }

    if (xbox_says == 6) //Dpad Down
    {
      Serial.println("Dpad Down");
      reverse();
    }

    if (xbox_says == 7) //Dpad Left
    {
      Serial.println("Dpad Left");
      clock_wise(150);
    }

    if (xbox_says == 8) //Dpad Right
    {
      anticlock_wise(150);
      Serial.println("Dpad Right");
    }

    if (xbox_says == 9 )
    {
      clock_wise(255);
      Serial.println("Left Button");
      //xbox_says = 0;
    }

    if (xbox_says == 10)
    {
      anticlock_wise(255);
      Serial.println("Right Button");
      //xbox_says = 0;
    }
    /////////////////////Xbox Buttons Section/////////////////////
    //////////////////////////////////////////////////////////////

    //////////////////////////////////////////////////////////////
    /////////////////////Solenoid Section/////////////////////////

    if (xbox_says == 183) //Button X
    {
      Serial.println("Left_Trigger");
      digitalWrite(solenoid, LOW);
    }


    /////////////////////Solenoid Section/////////////////////////
    //////////////////////////////////////////////////////////////


    //////////////////////////////////////////////////////////////
    ///////////////////////PWM Section////////////////////////////
    if (xbox_says == 11) //Right Trigger pwm
    {
      pwm = 5;
    }
    if (xbox_says == 12) //Right Trigger pwm
    {
      pwm = 10;
    }
    if (xbox_says == 13) //Right Trigger pwm
    {
      pwm = 15;
    }
    if (xbox_says == 14) //Right Trigger pwm
    {
      pwm = 20;
    }
    if (xbox_says == 15) //Right Trigger pwm
    {
      pwm = 25;
    }
    if (xbox_says == 16) //Right Trigger pwm
    {
      pwm = 30;
    }
    if (xbox_says == 17) //Right Trigger pwm
    {
      pwm = 35;
    }
    if (xbox_says == 18) //Right Trigger pwm
    {
      pwm = 40;
    }
    if (xbox_says == 19) //Right Trigger pwm
    {
      pwm = 45;
    }
    if (xbox_says == 20) //Right Trigger pwm
    {
      pwm = 51;
    }
    if (xbox_says == 21) //Right Trigger pwm
    {
      pwm = 56;
    }
    if (xbox_says == 22) //Right Trigger pwm
    {
      pwm = 61;
    }
    if (xbox_says == 23) //Right Trigger pwm
    {
      pwm = 66;
    }
    if (xbox_says == 24) //Right Trigger pwm
    {
      pwm = 71;
    }
    if (xbox_says == 25) //Right Trigger pwm
    {
      pwm = 76;
    }
    if (xbox_says == 26) //Right Trigger pwm
    {
      pwm = 81;
    }
    if (xbox_says == 27) //Right Trigger pwm
    {
      pwm = 86;
    }
    if (xbox_says == 28) //Right Trigger pwm
    {
      pwm = 91;
    }
    if (xbox_says == 29) //Right Trigger pwm
    {
      pwm = 96;
    }
    if (xbox_says == 30) //Right Trigger pwm
    {
      pwm = 102;
    }
    if (xbox_says == 31) //Right Trigger pwm
    {
      pwm = 107;
    }
    if (xbox_says == 32) //Right Trigger pwm
    {
      pwm = 112;
    }
    if (xbox_says == 33) //Right Trigger pwm
    {
      pwm = 117;
    }
    if (xbox_says == 34) //Right Trigger pwm
    {
      pwm = 122;
    }
    if (xbox_says == 35) //Right Trigger pwm
    {
      pwm = 127;
    }
    if (xbox_says == 36) //Right Trigger pwm
    {
      pwm = 132;
    }
    if (xbox_says == 37) //Right Trigger pwm
    {
      pwm = 137;
    }
    if (xbox_says == 38) //Right Trigger pwm
    {
      pwm = 142;
    }
    if (xbox_says == 39) //Right Trigger pwm
    {
      pwm = 147;
    }
    if (xbox_says == 40) //Right Trigger pwm
    {
      pwm = 153;
    }
    if (xbox_says == 41) //Right Trigger pwm
    {
      pwm = 158;
    }
    if (xbox_says == 42) //Right Trigger pwm
    {
      pwm = 163;
    }
    if (xbox_says == 43) //Right Trigger pwm
    {
      pwm = 168;
    }
    if (xbox_says == 44) //Right Trigger pwm
    {
      pwm = 173;
    }
    if (xbox_says == 45) //Right Trigger pwm
    {
      pwm = 178;
    }
    if (xbox_says == 46) //Right Trigger pwm
    {
      pwm = 183;
    }
    if (xbox_says == 47) //Right Trigger pwm
    {
      pwm = 188;
    }
    if (xbox_says == 48) //Right Trigger pwm
    {
      pwm = 193;
    }
    if (xbox_says == 49) //Right Trigger pwm
    {
      pwm = 198;
    }
    if (xbox_says == 50) //Right Trigger pwm
    {
      pwm = 204;
    }
    if (xbox_says == 51) //Right Trigger pwm
    {
      pwm = 209;
    }
    if (xbox_says == 52) //Right Trigger pwm
    {
      pwm = 214;
    }
    if (xbox_says == 53) //Right Trigger pwm
    {
      pwm = 219;
    }
    if (xbox_says == 54) //Right Trigger pwm
    {
      pwm = 224;
    }
    if (xbox_says == 55) //Right Trigger pwm
    {
      pwm = 229;
    }
    if (xbox_says == 56) //Right Trigger pwm
    {
      pwm = 234;
    }
    if (xbox_says == 57) //Right Trigger pwm
    {
      pwm = 239;
    }
    if (xbox_says == 58) //Right Trigger pwm
    {
      pwm = 244;
    }
    if (xbox_says == 59) //Right Trigger pwm
    {
      pwm = 249;
    }
    if (xbox_says == 60) //Right Trigger pwm
    {
      pwm = 255;
    }
    ///////////////////////PWM Section////////////////////////////
    //////////////////////////////////////////////////////////////

    //////////////////////////////////////////////////////////////
    //////////////////////Heading Angle///////////////////////////

    //61 is for no command
    if (xbox_says == 61) //Left Stick angle
    {
      Serial.println("Stick Angle is 360");
      heading_angle = 360;
    }
    if (xbox_says == 62) //Left Stick angle
    {
      Serial.println("Stick Angle is 3");
      heading_angle = 3;
    }
    if (xbox_says == 63) //Left Stick angle
    {
      Serial.println("Stick Angle is 6");
      heading_angle = 6;
    }
    if (xbox_says == 64) //Left Stick angle
    {
      Serial.println("Stick Angle is 9");
      heading_angle = 9;
    }
    if (xbox_says == 65) //Left Stick angle
    {
      Serial.println("Stick Angle is 12");
      heading_angle = 12;
    }
    if (xbox_says == 66) //Left Stick angle
    {
      Serial.println("Stick Angle is 15");
      heading_angle = 15;
    }
    if (xbox_says == 67) //Left Stick angle
    {
      Serial.println("Stick Angle is 18");
      heading_angle = 18;
    }
    if (xbox_says == 68) //Left Stick angle
    {
      Serial.println("Stick Angle is 21");
      heading_angle = 21;
    }
    if (xbox_says == 69) //Left Stick angle
    {
      Serial.println("Stick Angle is 24");
      heading_angle = 24;
    }
    if (xbox_says == 70) //Left Stick angle
    {
      Serial.println("Stick Angle is 27");
      heading_angle = 27;
    }
    if (xbox_says == 71) //Left Stick angle
    {
      Serial.println("Stick Angle is 30");
      heading_angle = 30;
    }
    if (xbox_says == 72) //Left Stick angle
    {
      Serial.println("Stick Angle is 33");
      heading_angle = 33;
    }
    if (xbox_says == 73) //Left Stick angle
    {
      Serial.println("Stick Angle is 36");
      heading_angle = 36;
    }
    if (xbox_says == 74) //Left Stick angle
    {
      Serial.println("Stick Angle is 39");
      heading_angle = 39;
    }
    if (xbox_says == 75) //Left Stick angle
    {
      Serial.println("Stick Angle is 42");
      heading_angle = 42;
    }
    if (xbox_says == 76) //Left Stick angle
    {
      Serial.println("Stick Angle is 45");
      heading_angle = 45;
    }
    if (xbox_says == 77) //Left Stick angle
    {
      Serial.println("Stick Angle is 48");
      heading_angle = 48;
    }
    if (xbox_says == 78) //Left Stick angle
    {
      Serial.println("Stick Angle is 51");
      heading_angle = 51;
    }
    if (xbox_says == 79) //Left Stick angle
    {
      Serial.println("Stick Angle is 54");
      heading_angle = 54;
    }
    if (xbox_says == 80) //Left Stick angle
    {
      Serial.println("Stick Angle is 57");
      heading_angle = 57;
    }
    if (xbox_says == 81) //Left Stick angle
    {
      Serial.println("Stick Angle is 60");
      heading_angle = 60;
    }
    if (xbox_says == 82) //Left Stick angle
    {
      Serial.println("Stick Angle is 63");
      heading_angle = 63;
    }
    if (xbox_says == 83) //Left Stick angle
    {
      Serial.println("Stick Angle is 66");
      heading_angle = 66;
    }
    if (xbox_says == 84) //Left Stick angle
    {
      Serial.println("Stick Angle is 69");
      heading_angle = 69;
    }
    if (xbox_says == 85) //Left Stick angle
    {
      Serial.println("Stick Angle is 72");
      heading_angle = 72;
    }
    if (xbox_says == 86) //Left Stick angle
    {
      Serial.println("Stick Angle is 75");
      heading_angle = 75;
    }
    if (xbox_says == 87) //Left Stick angle
    {
      Serial.println("Stick Angle is 78");
      heading_angle = 78;
    }
    if (xbox_says == 88) //Left Stick angle
    {
      Serial.println("Stick Angle is 81");
      heading_angle = 81;
    }
    if (xbox_says == 89) //Left Stick angle
    {
      Serial.println("Stick Angle is 84");
      heading_angle = 84;
    }
    if (xbox_says == 90) //Left Stick angle
    {
      Serial.println("Stick Angle is 87");
      heading_angle = 87;
    }
    if (xbox_says == 91) //Left Stick angle
    {
      Serial.println("Stick Angle is 90");
      heading_angle = 90;
    }
    if (xbox_says == 92) //Left Stick angle
    {
      Serial.println("Stick Angle is 93");
      heading_angle = 93;
    }
    if (xbox_says == 93) //Left Stick angle
    {
      Serial.println("Stick Angle is 96");
      heading_angle = 96;
    }
    if (xbox_says == 94) //Left Stick angle
    {
      Serial.println("Stick Angle is 99");
      heading_angle = 99;
    }
    if (xbox_says == 95) //Left Stick angle
    {
      Serial.println("Stick Angle is 102");
      heading_angle = 102;
    }
    if (xbox_says == 96) //Left Stick angle
    {
      Serial.println("Stick Angle is 105");
      heading_angle = 105;
    }
    if (xbox_says == 97) //Left Stick angle
    {
      Serial.println("Stick Angle is 108");
      heading_angle = 108;
    }
    if (xbox_says == 98) //Left Stick angle
    {
      Serial.println("Stick Angle is 111");
      heading_angle = 111;
    }
    if (xbox_says == 99) //Left Stick angle
    {
      Serial.println("Stick Angle is 114");
      heading_angle = 114;
    }
    if (xbox_says == 100) //Left Stick angle
    {
      Serial.println("Stick Angle is 117");
      heading_angle = 117;
    }
    if (xbox_says == 101) //Left Stick angle
    {
      Serial.println("Stick Angle is 120");
      heading_angle = 120;
    }
    if (xbox_says == 102) //Left Stick angle
    {
      Serial.println("Stick Angle is 123");
      heading_angle = 123;
    }
    if (xbox_says == 103) //Left Stick angle
    {
      Serial.println("Stick Angle is 126");
      heading_angle = 126;
    }
    if (xbox_says == 104) //Left Stick angle
    {
      Serial.println("Stick Angle is 129");
      heading_angle = 129;
    }
    if (xbox_says == 105) //Left Stick angle
    {
      Serial.println("Stick Angle is 132");
      heading_angle = 132;
    }
    if (xbox_says == 106) //Left Stick angle
    {
      Serial.println("Stick Angle is 135");
      heading_angle = 135;
    }
    if (xbox_says == 107) //Left Stick angle
    {
      Serial.println("Stick Angle is 138");
      heading_angle = 138;
    }
    if (xbox_says == 108) //Left Stick angle
    {
      Serial.println("Stick Angle is 141");
      heading_angle = 141;
    }
    if (xbox_says == 109) //Left Stick angle
    {
      Serial.println("Stick Angle is 144");
      heading_angle = 144;
    }
    if (xbox_says == 110) //Left Stick angle
    {
      Serial.println("Stick Angle is 147");
      heading_angle = 147;
    }
    if (xbox_says == 111) //Left Stick angle
    {
      Serial.println("Stick Angle is 150");
      heading_angle = 150;
    }
    if (xbox_says == 112) //Left Stick angle
    {
      Serial.println("Stick Angle is 153");
      heading_angle = 153;
    }
    if (xbox_says == 113) //Left Stick angle
    {
      Serial.println("Stick Angle is 156");
      heading_angle = 156;
    }
    if (xbox_says == 114) //Left Stick angle
    {
      Serial.println("Stick Angle is 159");
      heading_angle = 159;
    }
    if (xbox_says == 115) //Left Stick angle
    {
      Serial.println("Stick Angle is 162");
      heading_angle = 162;
    }
    if (xbox_says == 116) //Left Stick angle
    {
      Serial.println("Stick Angle is 165");
      heading_angle = 165;
    }
    if (xbox_says == 117) //Left Stick angle
    {
      Serial.println("Stick Angle is 168");
      heading_angle = 168;
    }
    if (xbox_says == 118) //Left Stick angle
    {
      Serial.println("Stick Angle is 171");
      heading_angle = 171;
    }
    if (xbox_says == 119) //Left Stick angle
    {
      Serial.println("Stick Angle is 174");
      heading_angle = 174;
    }
    if (xbox_says == 120) //Left Stick angle
    {
      Serial.println("Stick Angle is 177");
      heading_angle = 177;
    }
    if (xbox_says == 121) //Left Stick angle
    {
      Serial.println("Stick Angle is 180");
      heading_angle = 180;
    }
    if (xbox_says == 122) //Left Stick angle
    {
      Serial.println("Stick Angle is 183");
      heading_angle = 183;
    }
    if (xbox_says == 123) //Left Stick angle
    {
      Serial.println("Stick Angle is 186");
      heading_angle = 186;
    }
    if (xbox_says == 124) //Left Stick angle
    {
      Serial.println("Stick Angle is 189");
      heading_angle = 189;
    }
    if (xbox_says == 125) //Left Stick angle
    {
      Serial.println("Stick Angle is 192");
      heading_angle = 192;
    }
    if (xbox_says == 126) //Left Stick angle
    {
      Serial.println("Stick Angle is 195");
      heading_angle = 195;
    }
    if (xbox_says == 127) //Left Stick angle
    {
      Serial.println("Stick Angle is 198");
      heading_angle = 198;
    }
    if (xbox_says == 128) //Left Stick angle
    {
      Serial.println("Stick Angle is 201");
      heading_angle = 201;
    }
    if (xbox_says == 129) //Left Stick angle
    {
      Serial.println("Stick Angle is 204");
      heading_angle = 204;
    }
    if (xbox_says == 130) //Left Stick angle
    {
      Serial.println("Stick Angle is 207");
      heading_angle = 207;
    }
    if (xbox_says == 131) //Left Stick angle
    {
      Serial.println("Stick Angle is 210");
      heading_angle = 210;
    }
    if (xbox_says == 132) //Left Stick angle
    {
      Serial.println("Stick Angle is 213");
      heading_angle = 213;
    }
    if (xbox_says == 133) //Left Stick angle
    {
      Serial.println("Stick Angle is 216");
      heading_angle = 216;
    }
    if (xbox_says == 134) //Left Stick angle
    {
      Serial.println("Stick Angle is 219");
      heading_angle = 219;
    }
    if (xbox_says == 135) //Left Stick angle
    {
      Serial.println("Stick Angle is 222");
      heading_angle = 222;
    }
    if (xbox_says == 136) //Left Stick angle
    {
      Serial.println("Stick Angle is 225");
      heading_angle = 225;
    }
    if (xbox_says == 137) //Left Stick angle
    {
      Serial.println("Stick Angle is 228");
      heading_angle = 228;
    }
    if (xbox_says == 138) //Left Stick angle
    {
      Serial.println("Stick Angle is 231");
      heading_angle = 231;
    }
    if (xbox_says == 139) //Left Stick angle
    {
      Serial.println("Stick Angle is 234");
      heading_angle = 234;
    }
    if (xbox_says == 140) //Left Stick angle
    {
      Serial.println("Stick Angle is 237");
      heading_angle = 237;
    }
    if (xbox_says == 141) //Left Stick angle
    {
      Serial.println("Stick Angle is 240");
      heading_angle = 240;
    }
    if (xbox_says == 142) //Left Stick angle
    {
      Serial.println("Stick Angle is 243");
      heading_angle = 243;
    }
    if (xbox_says == 143) //Left Stick angle
    {
      Serial.println("Stick Angle is 246");
      heading_angle = 246;
    }
    if (xbox_says == 144) //Left Stick angle
    {
      Serial.println("Stick Angle is 249");
      heading_angle = 249;
    }
    if (xbox_says == 145) //Left Stick angle
    {
      Serial.println("Stick Angle is 252");
      heading_angle = 252;
    }
    if (xbox_says == 146) //Left Stick angle
    {
      Serial.println("Stick Angle is 255");
      heading_angle = 255;
    }
    if (xbox_says == 147) //Left Stick angle
    {
      Serial.println("Stick Angle is 258");
      heading_angle = 258;
    }
    if (xbox_says == 148) //Left Stick angle
    {
      Serial.println("Stick Angle is 261");
      heading_angle = 261;
    }
    if (xbox_says == 149) //Left Stick angle
    {
      Serial.println("Stick Angle is 264");
      heading_angle = 264;
    }
    if (xbox_says == 150) //Left Stick angle
    {
      Serial.println("Stick Angle is 267");
      heading_angle = 267;
    }
    if (xbox_says == 151) //Left Stick angle
    {
      Serial.println("Stick Angle is 270");
      heading_angle = 270;
    }
    if (xbox_says == 152) //Left Stick angle
    {
      Serial.println("Stick Angle is 273");
      heading_angle = 273;
    }
    if (xbox_says == 153) //Left Stick angle
    {
      Serial.println("Stick Angle is 276");
      heading_angle = 276;
    }
    if (xbox_says == 154) //Left Stick angle
    {
      Serial.println("NStick Angle is 279");
      heading_angle = 279;
    }
    if (xbox_says == 155) //Left Stick angle
    {
      Serial.println("Stick Angle is 282");
      heading_angle = 282;
    }
    if (xbox_says == 156) //Left Stick angle
    {
      Serial.println("Stick Angle is 285");
      heading_angle = 285;
    }
    if (xbox_says == 157) //Left Stick angle
    {
      Serial.println("Stick Angle is 288");
      heading_angle = 288;
    }
    if (xbox_says == 158) //Left Stick angle
    {
      Serial.println("Stick Angle is 291");
      heading_angle = 291;
    }
    if (xbox_says == 159) //Left Stick angle
    {
      Serial.println("Stick Angle is 294");
      heading_angle = 294;
    }
    if (xbox_says == 160) //Left Stick angle
    {
      Serial.println("Stick Angle is 297");
      heading_angle = 297;
    }
    if (xbox_says == 161) //Left Stick angle
    {
      Serial.println("Stick Angle is 00");
      heading_angle = 300;
    }
    if (xbox_says == 162) //Left Stick angle
    {
      Serial.println("Stick Angle is 303");
      heading_angle = 303;
    }
    if (xbox_says == 163) //Left Stick angle
    {
      Serial.println("Stick Angle is 306");
      heading_angle = 306;
    }
    if (xbox_says == 164) //Left Stick angle
    {
      Serial.println("Stick Angle is 309");
      heading_angle = 309;
    }
    if (xbox_says == 165) //Left Stick angle
    {
      Serial.println("Stick Angle is 312");
      heading_angle = 312;
    }
    if (xbox_says == 166) //Left Stick angle
    {
      Serial.println("Stick Angle is 315");
      heading_angle = 315;
    }
    if (xbox_says == 167) //Left Stick angle
    {
      Serial.println("Stick Angle is 318");
      heading_angle = 318;
    }
    if (xbox_says == 168) //Left Stick angle
    {
      Serial.println("Stick Angle is 321");
      heading_angle = 321;
    }
    if (xbox_says == 169) //Left Stick angle
    {
      Serial.println("Stick Angle is 324");
      heading_angle = 324;
    }
    if (xbox_says == 170) //Left Stick angle
    {
      Serial.println("Stick Angle is 327");
      heading_angle = 327;
    }
    if (xbox_says == 171) //Left Stick angle
    {
      Serial.println("Stick Angle is 330");
      heading_angle = 330;
    }
    if (xbox_says == 172) //Left Stick angle
    {
      Serial.println("Stick Angle is 333");
      heading_angle = 333;
    }
    if (xbox_says == 173) //Left Stick angle
    {
      Serial.println("Stick Angle is 336");
      heading_angle = 336;
    }
    if (xbox_says == 174) //Left Stick angle
    {
      Serial.println("Stick Angle is 339");
      heading_angle = 339;
    }
    if (xbox_says == 175) //Left Stick angle
    {
      Serial.println("Stick Angle is 342");
      heading_angle = 342;
    }
    if (xbox_says == 176) //Left Stick angle
    {
      Serial.println("Stick Angle is 345");
      heading_angle = 345;
    }
    if (xbox_says == 177) //Left Stick angle
    {
      Serial.println("Stick Angle is 348");
      heading_angle = 348;
    }
    if (xbox_says == 178) //Left Stick angle
    {
      Serial.println("Stick Angle is 351");
      heading_angle = 351;
    }
    if (xbox_says == 179) //Left Stick angle
    {
      //Serial.println("Stick Angle is 354");
      heading_angle = 354;
    }
    if (xbox_says == 180) //Left Stick angle
    {
      //Serial.println("Stick Angle is 357");
      heading_angle = 357;
    }
    if (xbox_says == 181) //Left Stick angle
    {
      Serial.println("Stick Angle is 360");
      heading_angle = 360;
    }
    /////////////////////////////////////////////////////
    //////////////////////////////////////////////////////////////
    //////////////////////////Else Loop///////////////////////////


    //Serial.println(xbox_says);
    if (xbox_says == 182)
    {
      brake();
      pwm = 0;
      heading_angle = -256;
      Final_pwm_90 = 256;
      Final_pwm_180 = 256;
      Final_pwm_270 = 256;
      Final_pwm_360 = 256;
      Serial.println("//////////////////////////////////Stop");
      digitalWrite(solenoid, HIGH);
      digitalWrite(weeding_up, HIGH);
      digitalWrite(weeding_down, HIGH);
    }

    //////////////////////////////////////////////////////////////
    //////////////////////////Else Loop///////////////////////////


    //Serial.println(pwm);

    if (heading_angle > 0 && heading_angle <= 90)
    {
      pwm_map_90 = map(heading_angle, 0, 90, -1000, 1000);
      pwm_map_temp_90 = pwm_map_90 / 1000;
      Final_pwm_90 = pwm_map_temp_90 * pwm;
      //Serial.println(Final_pwm_90);
    }
    if (heading_angle > 90 && heading_angle <= 180)
    {
      pwm_map_180 = map(heading_angle, 90, 180, -1000, 1000);
      pwm_map_temp_180 = pwm_map_180 / 1000;
      Final_pwm_180 = pwm_map_temp_180 * pwm;
      //Serial.println(Final_pwm_180);
    }
    if (heading_angle > 180 && heading_angle <= 270)
    {
      pwm_map_270 = map(heading_angle, 180, 270, -1000, 1000);
      pwm_map_temp_270 = pwm_map_270 / 1000;
      Final_pwm_270 = pwm_map_temp_270 * pwm;
      //Serial.println(Final_pwm_270);
    }
    if (heading_angle > 270 && heading_angle <= 360)
    {
      pwm_map_360 = map(heading_angle, 270, 360, -1000, 1000);
      pwm_map_temp_360 = pwm_map_360 / 1000;
      Final_pwm_360 = pwm_map_temp_360 * pwm;
      //Serial.println(Final_pwm_360);
    }
    // Serial.println(pwm_map_temp);
    //Serial.println(Final_pwm_90);
    //Serial.println(Final_pwm_180);
    //Serial.println(Final_pwm_270);
    //Serial.println(Final_pwm_360);

    if (Final_pwm_90 > 0 && Final_pwm_90 <= 255) //angle 45 to 90 degree
    {

      forward_left(pwm);
      forward_right (abs(Final_pwm_90));
      Serial.println("loop 1");
      Final_pwm_90 = 256;
    }
    if (Final_pwm_90 < 0 && Final_pwm_90 > -255) // angle 0 to 45 degree
    {
      forward_left(pwm);
      reverse_right(abs(Final_pwm_90));
      Serial.println("loop 2");
      Final_pwm_90 = 256;
    }
    if (Final_pwm_180 > 0 && Final_pwm_180 <= 255) // angle 125 to 180 degree
    {
      reverse_left(abs(Final_pwm_180));
      forward_right (pwm);
      Serial.println("loop 3");
      Final_pwm_180 = 256;
    }

    if (Final_pwm_180 < 0 && Final_pwm_180 > -255)  // angle 90 to 125 degree
    {
      forward_left(abs(Final_pwm_180));
      forward_right(pwm);
      Serial.println("loop 4");
      Final_pwm_180 = 256;
    }

    if (Final_pwm_270 > 0 && Final_pwm_270 <= 255) //angle 225 to 270 degree
    {
      reverse_left(pwm);
      reverse_right (abs(Final_pwm_270));
      Serial.println("loop 5");
      Final_pwm_270 = 256;
    }
    if (Final_pwm_270 < 0 && Final_pwm_270 > -255) // angle 180 to 225 degree
    {
      reverse_left(pwm);
      forward_right(abs(Final_pwm_270));
      Serial.println("loop 6");
      Final_pwm_270 = 256;
    }
    if (Final_pwm_360 > 0 && Final_pwm_360 <= 255) // angle 315 to 360 degree
    {
      forward_left(abs(Final_pwm_360));
      reverse_right (pwm);
      Serial.println("loop 7");
      Final_pwm_360 = 256;
    }

    if (Final_pwm_360 < 0 && Final_pwm_360 > -255)  // angle 270 to 315 degree
    {
      reverse_left(abs(Final_pwm_360));
      reverse_right(pwm);
      Serial.println("loop 8");
      Final_pwm_360 = 256;
    }




    xbox_sending = false;
  }

  //brake();


  //erial.println("boi");
  //forward(255);
  //Serial.println("Forward");
  //delay(4000);
  //brake();
  //Serial.println("Brake");
  //delay(1000);
  //reverse(255);
  //Serial.println("Reverse");
  //delay(4000);
  //brake();
  //Serial.println("Brake");
  //delay(1000);
  //clock_wise(255);
  //Serial.println("Clockwise");
  //delay(4000);
  //brake();
  //Serial.println("Brake");
  //delay(1000);
  //anticlock_wise(255);
  //Serial.println("AntiClockwise");
  //delay(4000);
  //brake();
  //Serial.println("Brake");
  //delay(1000);


}

void receiveEvent(int howMany) {

  for (int i = 0; i < howMany; i++) {
    xbox_says = Wire.read();
    // temp[i + 1] = '  '; //add null after ea. char
  }

  xbox_sending = true;
}

void forward() {
  Serial.print("Forward Slow");
  Serial.println(pwm_map);
  digitalWrite(dir1, HIGH);
  digitalWrite(dir2, HIGH);
  digitalWrite(dir3, HIGH);
  digitalWrite(dir4, LOW);
  digitalWrite(dir5, LOW);
  digitalWrite(dir6, LOW);

  analogWrite(pwm1, 150);
  analogWrite(pwm2, 150);
  analogWrite(pwm3, 150);
  analogWrite(pwm4, 150);
  analogWrite(pwm5, 150);
  analogWrite(pwm6, 150);
}

void reverse() {
  Serial.print("Forward Slow");
  Serial.println(pwm_map);
  digitalWrite(dir1, LOW);
  digitalWrite(dir2, LOW);
  digitalWrite(dir3, LOW);
  digitalWrite(dir4, HIGH);
  digitalWrite(dir5, HIGH);
  digitalWrite(dir6, HIGH);

  analogWrite(pwm1, 150);
  analogWrite(pwm2, 150);
  analogWrite(pwm3, 150);
  analogWrite(pwm4, 150);
  analogWrite(pwm5, 150);
  analogWrite(pwm6, 150);
}


void forward_left(int pwm_map) {
  Serial.print("Forward Left");
  Serial.println(pwm_map);
  digitalWrite(dir1, HIGH);
  digitalWrite(dir2, HIGH);
  digitalWrite(dir3, HIGH);

  analogWrite(pwm1, pwm_map);
  analogWrite(pwm2, pwm_map);
  analogWrite(pwm3, pwm_map);
}

void forward_right(int pwm_map) {
  Serial.print("Forward Right");
  Serial.println(pwm_map);
  digitalWrite(dir4, LOW);
  digitalWrite(dir5, LOW);
  digitalWrite(dir6, LOW);

  analogWrite(pwm4, pwm_map);
  analogWrite(pwm5, pwm_map);
  analogWrite(pwm6, pwm_map);
}

void reverse_left(int pwm_map) {
  Serial.print("Reverse Left");
  Serial.println(pwm_map);
  digitalWrite(dir1, LOW);
  digitalWrite(dir2, LOW);
  digitalWrite(dir3, LOW);

  analogWrite(pwm1, pwm_map);
  analogWrite(pwm2, pwm_map);
  analogWrite(pwm3, pwm_map);
}


void reverse_right(int pwm_map) {
  Serial.print("Reverse Right");
  Serial.println(pwm_map);
  digitalWrite(dir4, HIGH);
  digitalWrite(dir5, HIGH);
  digitalWrite(dir6, HIGH);

  analogWrite(pwm4, pwm_map);
  analogWrite(pwm5, pwm_map);
  analogWrite(pwm6, pwm_map);
}

void brake() {
  //Serial.println("Brake");
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

void clock_wise(int pwm_x) {

  Serial.println("Clockwise");
  digitalWrite(dir1, LOW);
  digitalWrite(dir2, LOW);
  digitalWrite(dir3, LOW);
  digitalWrite(dir4, LOW);
  digitalWrite(dir5, LOW);
  digitalWrite(dir6, LOW);

  analogWrite(pwm1, pwm_x);
  analogWrite(pwm2, pwm_x);
  analogWrite(pwm3, pwm_x);
  analogWrite(pwm4, pwm_x);
  analogWrite(pwm5, pwm_x);
  analogWrite(pwm6, pwm_x);
}

void anticlock_wise(int pwm_x) {

  Serial.println("Anti Clockwise");
  digitalWrite(dir1, HIGH);
  digitalWrite(dir2, HIGH);
  digitalWrite(dir3, HIGH);
  digitalWrite(dir4, HIGH);
  digitalWrite(dir5, HIGH);
  digitalWrite(dir6, HIGH);

  analogWrite(pwm1, pwm_x);
  analogWrite(pwm2, pwm_x);
  analogWrite(pwm3, pwm_x);
  analogWrite(pwm4, pwm_x);
  analogWrite(pwm5, pwm_x);
  analogWrite(pwm6, pwm_x);
}
