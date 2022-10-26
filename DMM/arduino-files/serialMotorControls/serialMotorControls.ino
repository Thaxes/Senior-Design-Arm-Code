#define stepPin 2
#define dirPin 3
int M = 5000;
int stepsPerRevolution = 200;
char state;

void UP()   // spin clockwise one revolution quickly
{
digitalWrite(dirPin, HIGH);
  for (int i = 0; i < stepsPerRevolution; i++) {
     digitalWrite(stepPin, HIGH);
  delayMicroseconds(M);
  digitalWrite(stepPin, LOW); // by alternating between high and low on the stepPin, the motor actuates or 'spins'
  delayMicroseconds(M);
  }
  }

void DOWN()   // spin counter-clockwise one revolution quickly
{
 digitalWrite(dirPin, LOW);
  for (int i = 0; i < stepsPerRevolution; i++) {
     digitalWrite(stepPin, HIGH);
  delayMicroseconds(M);
  digitalWrite(stepPin, LOW);
  delayMicroseconds(M);
}
}

void setup() {
  
  pinMode(stepPin, OUTPUT); // define the motor pins as output so they can be controlled by the arduino
  pinMode(dirPin, OUTPUT);  
  Serial.begin(9600);       // begins the serial connection at the SAME baudrate as the object sending data. 
}

void loop() {
  if (Serial.available() > 0) // returns true IF available data is size greater than zero
  {
      state = Serial.read();
      if (state == 'w' || state == 'u') // if data is w or u, trigger the UP function
      {
        Serial.println("Received: ");
        Serial.println(state);    // prints the received data vale
        UP();
      }
      else if (state == 's' || state == 'd') // if data is s or d, trigger the DOWN function
      {
        Serial.println("Received: ");
        Serial.println(state);    // prints the received data vale
        DOWN();
      }
      else
      {
        Serial.println("Received: "); // else do not call a function. 
        Serial.println(state);    // prints the received data vale
      }
  }
  else
  {
    Serial.println("Nothing Received");
  }
delay(100);   //this delay is 100 milliseconds, so this loop is executed very, very quickly
}
