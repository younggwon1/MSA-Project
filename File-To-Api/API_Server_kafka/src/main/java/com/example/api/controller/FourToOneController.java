package com.example.api.controller;

import com.example.api.service.OneToFourService;
import org.json.JSONArray;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;


@RestController
@RequestMapping("/request")
public class FourToOneController {

    @Autowired
    private OneToFourService otfs;

    @GetMapping(value = "/{filename}", produces = MediaType.APPLICATION_JSON_VALUE)
    public String response(@PathVariable String filename) {

        JSONArray jsonArray = otfs.getURL(filename);
        return String.valueOf(jsonArray);

    }


}


