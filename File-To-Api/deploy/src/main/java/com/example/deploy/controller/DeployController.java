package com.example.deploy.controller;

import com.example.deploy.service.DeployService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
@CrossOrigin("http://localhost:3000")
public class DeployController {

    @Autowired
    DeployService deployService;


    @PostMapping("/run")
    public String runner(@RequestParam("userport") String userport,@RequestParam("user") String user) {
        //deployService.execute("java -jar C:/Users/HPE/Work/git/File-To-Api/ApiServer/target/csvtosql-0.1.jar");
        //deployService.execute("ipconfig");
        deployService.execute(userport,user);
        return "success";
    }

    @PostMapping("/delete")
    public String delete(@RequestParam("user") String user){
        deployService.delete(user);
        return "delete";
    }
}
