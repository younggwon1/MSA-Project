package com.example.csvtosql.consumer;

import com.example.csvtosql.data.FileData;
import com.example.csvtosql.data.FileEvent;
import com.example.csvtosql.data.FileEventType;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.extern.slf4j.Slf4j;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


@Component
@Slf4j
public class FileEventsConsumer {


    @Autowired
    FileData fileData;

    @Autowired
    ObjectMapper objectMapper;

    List<String> line = new ArrayList<>();
    List<Map<String, String>> list_map = new ArrayList<>();
    Map<String, String> map;
    JSONObject jsonObject;
    static JSONArray jsonArray;

    @KafkaListener(topics = {"file-events"})
    public void onMessage(ConsumerRecord<String, String> consumerRecord) throws IOException, JSONException {

        FileEvent fileEvent = objectMapper.readValue(consumerRecord.value(), FileEvent.class);

        if (fileEvent.getFileEventType() == FileEventType.NOFILE) {
            log.info("파일이 없습니다");
            jsonObject = new JSONObject();
            jsonObject.put("1","파일이 없습니다.");
            jsonArray.put(jsonObject);
            kafkaMessage();


        } else if (fileEvent.getFileEventType() == FileEventType.CREATE) {
            log.info("파일 시작");
            jsonObject = new JSONObject();
            jsonObject.put("1","로딩중");
            jsonArray.put(jsonObject);
            kafkaMessage();

            line = new ArrayList<>();


        } else if (fileEvent.getFileEventType() == FileEventType.SEND) {
            line.add(fileEvent.getData());

        } else if (fileEvent.getFileEventType() == FileEventType.END) {
            log.info("파일 다 받았음");
            log.info(String.valueOf(line));

            String header = line.get(0).substring(1, line.get(0).length() - 1);
            String editHeader = header.replace(" ", "");
            String[] keys = editHeader.split(",");


            for (int i = 1; i < line.size(); i++) {

                String body = line.get(i).substring(1, line.get(i).length() - 1);
                String[] values = body.split(",");
                map = new HashMap<>();

                for (int j = 0; j < values.length; j++) {
                    map.put(keys[j], values[j]);
                }
                list_map.add(map);
            }
            jsonArray = new JSONArray(list_map);

            kafkaMessage();
        }
    }

//        return String.valueOf(jsonArray);


    public JSONArray kafkaMessage() {
        return jsonArray;
    }
}



