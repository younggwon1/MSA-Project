package com.example.deploy;

import com.example.deploy.service.DeployService;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import javax.annotation.Resource;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

@SpringBootApplication
public class DeployApplication{

    public static void main(String[] args) {

        SpringApplication.run(DeployApplication.class, args);

    }

}


