#include <math.h>
#define stepPin 54
#define dirPin 55
#define X_ENABLE_PIN 38
const unsigned long M = 100000; //microseconds
const int stepsPerRevolution = 400; //steps per revolution

unsigned long D2 = 200; //used as x in calculating acceleration delay f(x) = 1microsecond/x
char state;   //input from serialmonitor

void step(unsigned long delay2)//one step of the motor
{
  // These four lines result in 1 step:
  digitalWrite(stepPin, HIGH);
  delayMicroseconds(delay2);
  digitalWrite(stepPin, LOW);
  delayMicroseconds(delay2);
}

void COUNTER()  //Rotate motor counterclockwise
{
digitalWrite(dirPin, HIGH);
  // Spin the stepper motor 1 revolution slowly:
  for (int i = 0; i < stepsPerRevolution; i++) {
    step(M);
  }
  }

void CLOCK()  //Rotate motor clockwise
{
 digitalWrite(dirPin, LOW);
  // Spin the stepper motor 1 revolution slowly:
  for (int i = 0; i < stepsPerRevolution; i++) {
    // These four lines result in 1 step:
  step(M);
}
}

void AccelCOUNTER() //Rotate motor counterclockwise with acceleration
{
 digitalWrite(dirPin, HIGH);
  // Spin the stepper motor 1 revolution with acceleration:
  
  for (int i = 0; i < stepsPerRevolution / 25; i++) { //divide stepsPerRevolution by the number of steps taken in the nested loop.
    unsigned long delay2 = 1000000UL/D2;  //calculate a fraction
    if (D2 < 2000) //if x has not reached 2000, increment
    {
      D2 += 100;
    }
    else if (D2 < 2500) //if x has reached 500 but not 2500, increment but less
    {
      D2 += 50;
    }
    else if (D2 >= 2500)  //if x has reached 2500, do not increment any more.
    {
      D2 = 2500;
    }
      for (int j = 0; j <= 25; j++) //take 25 steps
    {
      step(delay2);
    }   
}
}

void AccelCLOCK() //Rotate motor clockwise with acceleration
{
 digitalWrite(dirPin, LOW);
  // Spin the stepper motor 1 revolution with acceleration:
  
  for (int i = 0; i < stepsPerRevolution / 25; i++) { //divide stepsPerRevolution by the number of steps taken in the nested loop.
    unsigned long delay2 = 1000000UL/D2;  //calculate a fraction
    if (D2 < 2000) //if x has not reached 2000, increment
    {
      D2 += 100;
    }
    else if (D2 < 2500) //if x has reached 500 but not 2500, increment but less
    {
      D2 += 50;
    }
    else if (D2 >= 2500)  //if x has reached 2500, do not increment any more.
    {
      D2 = 2500;
    }
      for (int j = 0; j <= 25; j++) //take 25 steps
    {
      step(delay2);
    }   
}
}

void setup() {
  
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);  
  pinMode(X_ENABLE_PIN, OUTPUT);
  digitalWrite(X_ENABLE_PIN, LOW);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) //if any input on serial port
  {
      state = Serial.read();  //if serial character is w, accelerate counterclockwise
      if (state == 'w') 
      {
        Serial.println("Received: ");
        Serial.println(state);
        AccelCOUNTER();
      }
      else if (state == 's') //if serial character is s, accelerate clockwise
      {
        Serial.println("Received: ");
        Serial.println(state);
        AccelCLOCK();
      }
      else  //else, print the serial character and do nothing
      {
        Serial.println("Received: ");
        Serial.println(state);
      }
  }
  else  //else, do nothing
  {
    Serial.println("Nothing Received");
  }
  delay(100);
}
