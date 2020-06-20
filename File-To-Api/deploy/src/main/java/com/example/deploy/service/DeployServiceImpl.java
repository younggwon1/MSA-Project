package com.example.deploy.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

@Service
public class DeployServiceImpl implements DeployService {

    //    String cmd1 = "docker run -d -p ";
//    String cmd2 = ":10004 --name ";
//    String cmd3 = " -v /c/shared/:/var/lib/restapi/ d8913aa8893d";
//    String cmd1 = "docker run -d -p ";
//    String cmd2 = ":8080 --name ";
//    String cmd3 = " dbsqud1105/hello";
    String cmd1 = "docker run -d -p ";
    String cmd2 = ":";
    String cmd3 = " --name ";
    String cmd4 = " -e server.port=";
    String cmd5 = " -v /var/lib/shared_data/:/var/lib/shared_data/ whdvlf94/api-server-linux";
//    String cmd5 = " -v /c/shared:/var/lib/shared_data whdvlf94/api-server-linux";


    String cmd7 = "docker rm ";
    String cmd8 = " -f";

    @Override
    public void execute(String userport, String user) {

        String cmd6 = new StringBuilder().append(cmd1).append(userport).append(cmd2).append(userport)
                .append(cmd3).append(user).append(cmd4).append(userport).append(cmd5).toString();

        Process process = null;
        Runtime runtime = Runtime.getRuntime();
        StringBuffer successOutput = new StringBuffer(); // 성공 스트링 버퍼
        StringBuffer errorOutput = new StringBuffer(); // 오류 스트링 버퍼
        BufferedReader successBufferReader = null; // 성공 버퍼
        BufferedReader errorBufferReader = null; // 오류 버퍼
        String msg = null; // 메시지

        List<String> cmdList = new ArrayList<String>();

        // 운영체제 구분 (window, window 가 아니면 무조건 linux 로 판단)
        if (System.getProperty("os.name").indexOf("Windows") > -1) {
            cmdList.add("cmd");
            cmdList.add("/c");

        } else {
            cmdList.add("/bin/sh");
            cmdList.add("-c");
        }
        // 명령어 셋팅
        cmdList.add(cmd6);
        String[] array = cmdList.toArray(new String[cmdList.size()]);

        try {

            // 명령어 실행
            process = runtime.exec(array);

            // shell 실행이 정상 동작했을 경우
            successBufferReader = new BufferedReader(new InputStreamReader(process.getInputStream(), "EUC-KR"));

            while ((msg = successBufferReader.readLine()) != null) {
                successOutput.append(msg + System.getProperty("line.separator"));
            }

            // shell 실행시 에러가 발생했을 경우
            errorBufferReader = new BufferedReader(new InputStreamReader(process.getErrorStream(), "EUC-KR"));
            while ((msg = errorBufferReader.readLine()) != null) {
                errorOutput.append(msg + System.getProperty("line.separator"));
            }

            // 프로세스의 수행이 끝날때까지 대기
            process.waitFor();

            // shell 실행이 정상 종료되었을 경우
            if (process.exitValue() == 0) {
                System.out.println("성공");
                System.out.println(successOutput.toString());
            } else {
                // shell 실행이 비정상 종료되었을 경우
                System.out.println("비정상 종료");
                System.out.println(successOutput.toString());
            }

            //shell 실행시 에러가 발생
//            if (CommonUtil.notEmpty(errorOutput.toString())) {
//                // shell 실행이 비정상 종료되었을 경우
//                System.out.println("오류");
//                System.out.println(successOutput.toString());
//            }

        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            try {
                process.destroy();
                if (successBufferReader != null) successBufferReader.close();
                if (errorBufferReader != null) errorBufferReader.close();
            } catch (IOException e1) {
                e1.printStackTrace();
            }
        }
    }

    @Override
    public void delete(String user) {

        String cmd9 = new StringBuilder().append(cmd7).append(user).append(cmd8).toString();

        Process process = null;
        Runtime runtime = Runtime.getRuntime();
        StringBuffer successOutput = new StringBuffer(); // 성공 스트링 버퍼
        StringBuffer errorOutput = new StringBuffer(); // 오류 스트링 버퍼
        BufferedReader successBufferReader = null; // 성공 버퍼
        BufferedReader errorBufferReader = null; // 오류 버퍼
        String msg = null; // 메시지

        List<String> cmdList = new ArrayList<String>();

        // 운영체제 구분 (window, window 가 아니면 무조건 linux 로 판단)
        if (System.getProperty("os.name").indexOf("Windows") > -1) {
            cmdList.add("cmd");
            cmdList.add("/c");

        } else {
            cmdList.add("/bin/sh");
            cmdList.add("-c");
        }
        // 명령어 셋팅
        cmdList.add(cmd9);
        String[] array = cmdList.toArray(new String[cmdList.size()]);

        try {

            // 명령어 실행
            process = runtime.exec(array);

            // shell 실행이 정상 동작했을 경우
            successBufferReader = new BufferedReader(new InputStreamReader(process.getInputStream(), "EUC-KR"));

            while ((msg = successBufferReader.readLine()) != null) {
                successOutput.append(msg + System.getProperty("line.separator"));
            }

            // shell 실행시 에러가 발생했을 경우
            errorBufferReader = new BufferedReader(new InputStreamReader(process.getErrorStream(), "EUC-KR"));
            while ((msg = errorBufferReader.readLine()) != null) {
                errorOutput.append(msg + System.getProperty("line.separator"));
            }

            // 프로세스의 수행이 끝날때까지 대기
            process.waitFor();

            // shell 실행이 정상 종료되었을 경우
            if (process.exitValue() == 0) {
                System.out.println("성공");
                System.out.println(successOutput.toString());
            } else {
                // shell 실행이 비정상 종료되었을 경우
                System.out.println("비정상 종료");
                System.out.println(successOutput.toString());
            }

            //shell 실행시 에러가 발생
//            if (CommonUtil.notEmpty(errorOutput.toString())) {
//                // shell 실행이 비정상 종료되었을 경우
//                System.out.println("오류");
//                System.out.println(successOutput.toString());
//            }

        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            try {
                process.destroy();
                if (successBufferReader != null) successBufferReader.close();
                if (errorBufferReader != null) errorBufferReader.close();
            } catch (IOException e1) {
                e1.printStackTrace();
            }
        }
    }


}
