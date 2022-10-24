// The above headers are necessary for utilizing ROS
#define stepPin 1
#define dirPin 2
// define which pins the stepper controller is connected to

int stepsPerRevolution = 400;

void UP()
{
digitalWrite(dirPin, HIGH);

  // Spin the stepper motor 1 revolution slowly:
  for (int i = 0; i < stepsPerRevolution; i++) {
    // These four lines result in 1 step:
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(700);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(700);
}
}

void DOWN()
{
 digitalWrite(dirPin, LOW);
  // Spin the stepper motor 1 revolution slowly:
  for (int i = 0; i < stepsPerRevolution; i++) {
    // These four lines result in 1 step:
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(700);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(700);
}
}

void STOP()
{
  digitalWrite(stepPin, LOW);
}

void interpretCommand(char x)
{

if (x == 1)
{
  Serial.write("up");
  UP();
}
else if (x == 2)
{
  Serial.write("down");
  DOWN();
}
else if (x == 0)
{
  Serial.write("stop");
    STOP();
}
else  
{
  Serial.write("stop");
  STOP();
}
}

void setup()
{

pinMode(dirPin, OUTPUT);
pinMode(stepPin, OUTPUT);
Serial.begin(9600);
while (! Serial); // Wait untilSerial is ready - Leonardo
Serial.println("Enter 0 to turn off LED and 1 to turn on LED");
}

void loop()
{
if(Serial.available())
{
	char ch = Serial.read();
	interpretCommand(ch);
}
delay(200);
}
