// since this line runs in the UI thread, don't need to initialize loopers or anything. override handleMessage if you need messages.
mWristbandHandler = new Handler();



    void startWristbandThread(BluetoothSocket mmSocket ){
        mBluetoothConnectedThread = new BluetoothConnectedThread(  mmSocket , mWristbandHandler ){
            @Override
            public void run() {
                    mmBuffer = new byte[1024];
                    int numBytes; // bytes returned from read()

//             Keep listening to the InputStream until an exception occurs.
                    while (true) {
                        try {
                            Log.d(TAG_WRISTBAND, "Attempting to read");

//                     Read from the InputStream.
                            numBytes = mmInStream.read(mmBuffer);

//                     testing by constantly printing the read buffer
                            String s = new String(mmBuffer);
                            Log.d(TAG_WRISTBAND, s);
                            mHandler.post(new Runnable() {
                                @Override
                                public void run() {
                                    // this will run in the main thread
                                    testRunnable();
                                }
                            });

//                    // Send the obtained bytes to the UI activity.
//                    Message readMsg = mHandler.obtainMessage(
//                            MessageConstants.MESSAGE_READ, numBytes, -1,
//                            mmBuffer);
//                    readMsg.sendToTarget();
                        } catch (IOException e) {
                            Log.d(TAG_WRISTBAND, "Input stream was disconnected", e);
                            break;
                        }
                    }


            }
        };
        mBluetoothConnectedThread.start();

    }

    public void testRunnable(){
        mTextView.setText("Runnable executed!");
    }