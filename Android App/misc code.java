StringBuffer fromWristbandBuffer;
String fromWristband;

BufferedReader in
  = new BufferedReader(new InputStreamReader(mmInStream));

  while(true){
// use blocking read calls to read one char at a time until a newline is found
fromWristbandBuffer = new StringBuffer(1024); //use an empty buffer
    while(true){
        char inChar = (char) in.read();
        fromWristbandBuffer.append(inChar) ;
        if(inChar == '\n'){
            fromWristband = fromWristbandBuffer.toString();
            break;
            }
            Log.d(TAG_WRISTBAND, String.valueOf(inChar));
        }
    }