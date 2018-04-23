/* Section added by Tim 4/20/2018 */
// using String objects. see Arduino reference.
// you DO need the newline, since char by char appends the newline to the fromPhone object.
String TAKE_PHOTO = "Take Photo\n";
// String NO_MATCH = "No Match\n";
// String RECOGNIZE_REQUEST = "Recognize Request\n";
      

String fromPhone = "";         // a String to hold incoming data
boolean stringComplete = false;  // whether the string is complete

/* End of Tim's additions. */

void setup(){
// Open serial connection.
//Serial.begin(1000000);
 Serial.begin(115200);
}
 
void loop(){
//Serial.print("Hello world");
//delay(10); // ms


  while (Serial.available()) {
//      Serial.println("available");

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
  
  if (stringComplete) {
    Serial.println(fromPhone);

    
    if(fromPhone.equals(TAKE_PHOTO)){
      Serial.print("taking photo");
    }
    // if(fromPhone.equals(NO_MATCH)){
    //   vibrate();
    //   delay(1000);
    //   vibrate();
    // }
    // for now, assumes the only other possibility is a name to be displayed.
    // else{
          // print_d(fromPhone);
    // }    
    // clear the string:
    fromPhone = "";
    stringComplete = false;
  }
}
