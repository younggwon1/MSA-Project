package com.example.api.service;


import com.example.api.consumer.FileEventsConsumer;
import org.json.JSONArray;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;

@Service
public class OneToFourServiceIm implements OneToFourService {

    public OneToFourServiceIm() {
    }
    @Autowired
    FileEventsConsumer fileEventsConsumer;

    @Override
    public JSONArray getURL(String filename) {
        try {
            String requestUrl = "http://59.29.224.136:8099/file/readfile/" + filename;

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
