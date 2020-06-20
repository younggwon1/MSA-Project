package com.yb.spring.files.upload.message;

public class ResponseMessage {
  private String message;
  private  String filename;

  public ResponseMessage(String message,  String filename) {
    this.message = message;
    this.filename = filename;
  }
  public ResponseMessage(String message) {
    this.message = message;
  }

  public String getMessage() {
    return message;
  }

  public void setMessage(String message) {
    this.message = message;
  }

  public String getFilename() {
    return filename;
  }

  public void setFilename(String filename) {
    this.filename = filename;
  }
}
