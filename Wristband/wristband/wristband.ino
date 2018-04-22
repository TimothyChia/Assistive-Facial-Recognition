#include <Wire.h>
#include <Adafruit_SSD1306.h>
#include <Adafruit_GFX.h>

// OLED display TWI address
#define OLED_ADDR   0x3C

Adafruit_SSD1306 display(-1);

#if (SSD1306_LCDHEIGHT != 64)
#error("Height incorrect, please fix Adafruit_SSD1306.h!");
#endif

// using String objects. see Arduino reference.
// you DO need the newline, since char by char appends the newline to the fromPhone object.
String MATCH_FOUND = "Match Found\n";
String NO_MATCH = "No Match\n";
String RECOGNIZE_REQUEST = "Recognize Request\n";
      

String fromPhone = "";         // a String to hold incoming data
boolean stringComplete = false;  // whether the string is complete
const int motorPin = 9;
const int buttonPin = 13; // temporary choice for testing


// BUTTON VARIABLES:
int buttonState;             // the current reading from the input pin
int lastButtonState = LOW;   // the previous reading from the input pin
// the following variables are unsigned longs because the time, measured in
// milliseconds, will quickly become a bigger number than can be stored in an int.
unsigned long lastDebounceTime = 0;  // the last time the output pin was toggled
unsigned long debounceDelay = 50;    // the debounce time; increase if the output flickers

void setup() {
  // initialize and clear display
  display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDR);
  display.clearDisplay();
  display.display();

  print_d("Display Initialized!");


  Serial.begin(9600);
//  Serial.begin(1382400); // make sure to setup the HC 05 for this baud rate.
//  Serial.begin(460800);
//Serial.begin(115200);

//  Serial.begin(921600);
//  Serial.println("Serial initialized at 1382400");
  // reserve 200 bytes for the inputString:
  fromPhone.reserve(200);

  pinMode(motorPin,OUTPUT);
  pinMode(buttonPin,INPUT);
}

/*
 * A print function that prints the parameter text to the display.
 */
void print_d(String text){
  // display a line of text

  display.clearDisplay(); // for now, just get rid of what was there before.

  
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(1,20);
  display.print(text);

  // update display with all of the above graphics
  display.display();  
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
      if (buttonState == HIGH)
         Serial.println(RECOGNIZE_REQUEST);
    }
  }  
  lastButtonState = reading;



  // Do something when a newline arrives:
  if (stringComplete) {
    Serial.println(fromPhone);

    
    if(fromPhone.equals(MATCH_FOUND)){
      Serial.print("vibrating");
      vibrate();
    }
    if(fromPhone.equals(NO_MATCH)){
      vibrate();
      delay(1000);
      vibrate();
    }
    // for now, assumes the only other possibility is a name to be displayed.
    else{
          print_d(fromPhone);
    }    
    // clear the string:
    fromPhone = "";
    stringComplete = false;
  }
  

}

// pulses the motor for 1000 seconds
void vibrate(){
  digitalWrite(motorPin, HIGH);
  delay(1000);
  digitalWrite(motorPin,LOW);
}


/*
  SerialEvent occurs whenever a new data comes in the hardware serial RX. This
  routine is run between each time loop() runs, so using delay inside loop can
  delay response. Multiple bytes of data may be available.
*/
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    fromPhone += inChar;
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}
