package com.example.crawlingapi.controller;
import com.example.crawlingapi.data.UserData;
import com.example.crawlingapi.repository.UserEntiRepository;
import com.example.crawlingapi.service.DataService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;



import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;
import java.util.List;

//@CrossOrigin
@RestController
@RequestMapping("/seouldatadb")
public class DataController {

    @Autowired
    private UserEntiRepository userEntiRepository;

    @Autowired
    private DataService categoryService;

    @GetMapping
    public List<UserData> list() {
        List<UserData> userEntities = categoryService.getCategories();

        return userEntities;
    }

    @GetMapping(value = "/detail",
            produces = {MediaType.APPLICATION_JSON_VALUE})
    @ResponseBody
    public Page<UserData> getReservations(
            @RequestParam String location, Pageable pageable) throws UnsupportedEncodingException {

        String queryString = URLDecoder.decode(location, "UTF-8");
//        String location = '"' + queryString + '"';

        return categoryService.getReservationByEmail(queryString,pageable);
    }
//
//    @GetMapping("/boards")
//    public Page<UserData> boardView(@PageableDefault Pageable pageable, Model model) {
//        Page<UserData> boardList = categoryService.getBoardList(pageable);
//        model.addAttribute("boardList", boardList);
//        return boardList;
//    }

    @GetMapping("/articles")
    public Page<UserData> getAllArticles(Pageable pageable) {
        return userEntiRepository.findAll(pageable);
    }


}
