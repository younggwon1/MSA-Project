package com.example.crawlingapi.repository;
import com.example.crawlingapi.data.UserData;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.domain.Specification;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;


import java.util.List;

public interface UserEntiRepository extends JpaRepository<UserData, Long> {

    List<UserData> findAll();
    Page<UserData> findByLocation(String location, Pageable pageable);


}
