//#include <LiquidCrystal.h>
//LiquidCrystal lcd(0x27,16,2);

const int trig=10;
const int echo=9;

long duration;
long distance;
int distanceCm, distanceInch;

void setup() {
  // put your setup code here, to run once:
  //lcd.begin(16,2);
  //lcd.backlight();
  pinMode(trig,OUTPUT);
  pinMode(echo,INPUT);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(trig,LOW);
  delayMicroseconds(2);

  digitalWrite(trig,HIGH);
  delayMicroseconds(10);
  digitalWrite(trig,LOW);
  duration = pulseIn(echo,HIGH);
  distance = duration*0.034/2; //speed of sound=340 m/s =0.034 cm/microsecond.

  Serial.print("Distance : ");
  Serial.println(distance);

  /*
  long duration = pulseIn(echo,HIGH);
  long distance=duration*0.034/2; //speed of sound=340 m/s =0.034 cm/microsecond.
  lcd.setCursor(10,0);
  lcd.print("    ");
  
  lcd.setCursor(10,0);
  lcd.print(distance);
  Serial.print("Distance : ");
  Serial.println(distance);
  Serial.print(" cm");
  delay(3000);
  */
}                 

