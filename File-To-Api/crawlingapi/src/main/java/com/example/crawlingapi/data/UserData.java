package com.example.crawlingapi.data;

import lombok.Data;

import javax.persistence.*;
import java.io.Serializable;


@Data
@Entity
@Table(name ="seouldatadb")
public class UserData implements Serializable {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String location;

    @Column(nullable = false)
    private String category;

    @Column(nullable = false)
    private String info;

    @Column(name = "classification",nullable = false)
    private String classification;

    @Column(name = "classification_info",nullable = false)
    private String classificationInfo;

    @Column(nullable = false)
    private String provider;

    @Column(nullable = false)
    private String providerInfo;

    @Column(nullable = false)
    private String providerdep;

    @Column(nullable = false)
    private String providerdepInfo;

    @Column(nullable = false)
    private String rangeuse;

    @Column(nullable = false)
    private String rangeuseInfo;

    @Column(nullable = false)
    private String enrollment;

    @Column(nullable = false)
    private String enrollmentInfo;

    @Column(nullable = false)
    private String modify;

    @Column(nullable = false)
    private String modifyInfo;

    @Column(nullable = false)
    private String url;

    private UserData(){

    }
}