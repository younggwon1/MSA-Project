package com.example.csvtosql.service;


import com.example.csvtosql.consumer.FileEventsConsumer;
import org.json.JSONArray;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.io.*;
import java.net.*;
import java.util.ArrayList;
import java.util.List;

@Service
public class OneToFourServiceIm implements OneToFourService {

    public OneToFourServiceIm() {
    }
    @Autowired
    FileEventsConsumer fileEventsConsumer;

    @Override
    public JSONArray getURL(String filename) {
        try {
            String requestUrl = "http://localhost:8081/" + filename + "?key=abc";

            URL url = new URL(requestUrl);

            URLConnection con = url.openConnection();
//            con.setConnectTimeout(3000);
//            con.setReadTimeout(3000);
            InputStream is = con.getInputStream();
            int connectOk = ((HttpURLConnection) con).getResponseCode();

            if(connectOk == 200) {
                System.out.println("Request GET Method " + ((HttpURLConnection) con).getResponseCode() + " OK!");
                JSONArray jsonArray = fileEventsConsumer.kafkaMessage();
                return jsonArray;
            }

        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

}
