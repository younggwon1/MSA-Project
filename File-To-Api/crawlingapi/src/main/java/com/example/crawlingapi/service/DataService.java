package com.example.crawlingapi.service;
import com.example.crawlingapi.data.UserData;
import com.example.crawlingapi.repository.UserEntiRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import javax.transaction.Transactional;


import java.util.List;

@Service
@Transactional
public class DataService {

    private UserEntiRepository userRepository;

    @Autowired
    public DataService(UserEntiRepository userRepository) {
        this.userRepository = userRepository;
    }

    public List<UserData> getCategories() {
        List<UserData> userEntities = userRepository.findAll();
        return userEntities;
    }


    public Page<UserData> getReservationByEmail(String location, Pageable pageable) {
        return (Page<UserData>) userRepository.findByLocation(location,pageable);
    }



//       public Page<UserData> getBoardList(Pageable pageable) {
//           int page = (pageable.getPageNumber() == 0) ? 0 : (pageable.getPageNumber() - 1); // page는 index 처럼 0부터 시작
//           pageable = PageRequest.of(page, 10);
//
//           return userRepository.findAll(pageable);
//       }
}