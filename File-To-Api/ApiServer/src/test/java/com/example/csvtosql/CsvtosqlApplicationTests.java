package com.example.csvtosql;

import lombok.extern.slf4j.Slf4j;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@SpringBootTest
@Slf4j
class CsvtosqlApplicationTests {

    @Test
    void contextLoads() throws JSONException {
        JSONObject jsonObject;
        JSONArray jsonArray = new JSONArray();

        jsonObject = new JSONObject();
        jsonObject.put("로딩중","로딩중");
        jsonArray.put(jsonObject);

        log.info(String.valueOf(jsonArray));

    }



}
