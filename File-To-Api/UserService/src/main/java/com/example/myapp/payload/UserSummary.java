package com.example.myapp.payload;

public class UserSummary {
    private Long id;
    private String username;
    private String name;
    private String userkey;

    public UserSummary(Long id, String username, String name, String userkey) {
        this.id = id;
        this.username = username;
        this.name = name;
        this.userkey = userkey;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getUserkey() {
        return userkey;
    }

    public void setUserkey(String userkey) {
        this.userkey = userkey;
    }
}