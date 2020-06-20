package com.example.deploy.repository;

import com.example.deploy.entity.Deploy;
import org.springframework.data.jpa.repository.JpaRepository;

public interface DeployRepository extends JpaRepository<Deploy, Integer> {
}
