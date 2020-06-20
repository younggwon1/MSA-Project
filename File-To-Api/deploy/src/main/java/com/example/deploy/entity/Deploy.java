package com.example.deploy.entity;

import lombok.Data;

import javax.persistence.*;

@Entity
@Data
public class Deploy {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column
    private Long id;

    @Column
    private String user;


}
