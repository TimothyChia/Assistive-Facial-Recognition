
const int buttonPin = 13; // temporary choice for testing


// BUTTON VARIABLES:
int buttonState;             // the current reading from the input pin
int lastButtonState = LOW;   // the previous reading from the input pin
// the following variables are unsigned longs because the time, measured in
// milliseconds, will quickly become a bigger number than can be stored in an int.
unsigned long lastDebounceTime = 0;  // the last time the output pin was toggled
unsigned long debounceDelay = 50;    // the debounce time; increase if the output flickers


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(buttonPin,INPUT);


}

void loop() {
  // put your main code here, to run repeatedly:


  // BUTTON CODE: Comments at https://www.arduino.cc/en/Tutorial/Debounce
  // if button pressed, tell the phone to get a photo and recognize
  int reading = digitalRead(buttonPin);
  if (reading != lastButtonState) 
    lastDebounceTime = millis();
  if ((millis() - lastDebounceTime) > debounceDelay) {
    if (reading != buttonState) {
      buttonState = reading;
      if (buttonState == HIGH){
        Serial.print("*RDY*\n");
//        Serial.print("*RDY*\n");
        for(int i = 0;i < 30000; i++)
          Serial.print("a");
        Serial.print("\n");
        Serial.print("b");
      }
         

         
    }
  }  
  lastButtonState = reading;

}
