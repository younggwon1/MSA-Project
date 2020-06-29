package com.example.api.data;


import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@AllArgsConstructor
@NoArgsConstructor
@Data
public class FileEvent {

    private String fileName;
    private FileEventType fileEventType;
    private String data;

}
