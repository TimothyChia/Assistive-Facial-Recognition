package com.example.timothychia.faces;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

import com.android.volley.AuthFailureError;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.JsonRequest;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // For some reason, the JSONObject.put method has to be wrapped in try/catch before android studio will take it
        JSONObject gallery_name = new JSONObject();
        try {
            gallery_name.put("gallery_name","Office");
        } catch (JSONException e) {
            e.printStackTrace();
        }

        //  R.id.textView2 should be changed to match the actual id in the layout.xml
        final TextView mTextView = (TextView) findViewById(R.id.textView2);
// ...

        // A more complicated queue instantiation may be needed to make this safe from even orientation changes
        RequestQueue queue = Volley.newRequestQueue(this);
        String url = "https://api.kairos.com/gallery/view";

        
/**
 * JsonObjectRequest takes in five paramaters
 * Request Type - This specifies the type of the request eg: GET,POST
 * URL          - This String param specifies the Request URL
 * JSONObject   - This parameter takes in the POST parameters."null" in
 *                  case of GET request.
 * Listener     -This parameter takes in a implementation of Response.Listener()
 *                 interface which is invoked if the request is successful
 * Listener     -This parameter takes in a implementation of Error.Listener()
 *               interface which is invoked if any error is encountered while processing
 *               the request
 **/
 // After the parameters, more methods can be overriden such as getHeaders
        JsonObjectRequest jReq = new JsonObjectRequest(Request.Method.POST, url,gallery_name,
                new Response.Listener() {
                    // online tutorial doesn't use "Object response", but android studio won't recognize it as an override otherwise
                    public void onResponse(Object response) {
                        // Display the first 500 characters of the response string.
                        mTextView.setText("Response is: "+ response.toString());
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(
                /**
                 * JsonObjectRequest takes in five paramaters
                 * Request Type - This specifies the type of the request eg: GET,POST
                 * URL          - This String param specifies the Request URL
                 * JSONObject   - This parameter takes in the POST parameters."null" in
                 *                  case of GET request.
                 * Listener     -This parameter takes in a implementation of Response.Listener()
                 *                 interface which is invoked if the request is successful
                 * Listener     -This parameter takes in a implementation of Error.Listener()
                 *               interface which is invoked if any error is encountered while processing
                 *               the request
                 **/VolleyError error) {
                mTextView.setText("That didn't work!");
            }
        }){

            /** Passing some request headers* */
            @Override
            // online tutorial uses some strange syntax in the angular brackets. Changed it to this instead.
            public Map<String, String> getHeaders() throws AuthFailureError {
                HashMap<String, String> headers = new HashMap<String, String>();
                headers.put("Content-Type", "application/json");
                headers.put("app_id","a1731ed8");
                headers.put("app_key", "d3a579a339de2805b54e53dcd72ee40c");
                return headers;
            }
        };

// Add the request to the RequestQueue.
        queue.add(jReq);

    }
}
