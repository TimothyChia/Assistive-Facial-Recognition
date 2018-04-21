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



    byte[] b = new byte[1000000];

    Log.d(BT_TAG, "Attempting to read");
    fromWristband=in.readLine();
    long startTime = System.nanoTime();
//                            mmInStream.read(b,0,10);
    long endTime = System.nanoTime();
    Log.d(BT_TAG, fromWristband);
    Log.d(BT_TAG, String.valueOf(b[9]));
    Log.d(BT_TAG, String.valueOf(startTime));
    Log.d(BT_TAG, String.valueOf(endTime));


        //            @ new function
        public void inputSize(){
            Log.d(TAG_WRISTBAND, "Checking inputStreamSize");
    
            try {
                int inputStreamSize = mBluetoothConnectedThread.mmInStream.available();
                Log.d(TAG_WRISTBAND, String.valueOf(inputStreamSize));
            } catch (IOException e) {
                Log.e(TAG_WRISTBAND, "Error checking inputStreamSize", e);
            }
    
    
        }


// this version doesn't do anything with the output of read, just trying to get through it all.

        //                            byte[] b = new byte[1000000];
//                            int result = 0;

//                            Log.d(TAG_WRISTBAND, "Attempting to read");
//
//                            for(int i = 0;i<6;i++)
//                                mmInStream.read();
//                            Log.d(TAG_WRISTBAND, "Read 6 characters");
//                            long startTime = System.nanoTime();
//                            for(int i = 0;i<100000;i++){
//                                Log.d(TAG_WRISTBAND, String.valueOf(i));
//                                try {
//                                    result =  mmInStream.read();
//                                } catch (IOException e) {
//                                    Log.e(TAG_WRISTBAND, "Error reading", e);
//                                }
////                                Log.d(TAG_WRISTBAND, String.valueOf(result));
//
//                            }
//                            result = mmInStream.read(); // read one more to check what these chars are
//                            Log.d(TAG_WRISTBAND, String.valueOf(result));
//
//                            long endTime = System.nanoTime();
//                            Log.d(TAG_WRISTBAND, String.valueOf(startTime));
//                            Log.d(TAG_WRISTBAND, String.valueOf(endTime));



// used this to debug the maximum length readable in a single line
BufferedReader in = new BufferedReader(new InputStreamReader(mmInStream),200000);
// then inside the while and inside the try,  :
fromWristband=in.readLine();
Log.d(TAG_WRISTBAND, "Line length of: " + String.valueOf(fromWristband.length()));
