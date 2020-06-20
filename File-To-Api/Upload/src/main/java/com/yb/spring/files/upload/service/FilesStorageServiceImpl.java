package com.yb.spring.files.upload.service;

import java.io.File;
import java.io.IOException;
import java.net.MalformedURLException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.stream.Stream;

import com.yb.spring.files.upload.model.FileInfo;
import com.yb.spring.files.upload.repository.FileRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.Resource;
import org.springframework.core.io.UrlResource;
import org.springframework.stereotype.Service;
import org.springframework.util.FileSystemUtils;
import org.springframework.web.multipart.MultipartFile;

@Service
public class FilesStorageServiceImpl implements FilesStorageService {



  FileRepository fileRepository;

//  private Path root = Paths.get("./shared");
  private Path root = Paths.get("C:\\shared");

  private String root2 ="";



  @Autowired
  public FilesStorageServiceImpl(FileRepository fileRepository){

    this.fileRepository = fileRepository;
  }

//  @Override
//  public void init() {
//    try {
//      Files.createDirectory(root);
//    } catch (IOException e) {
//      throw new RuntimeException("Could not initialize folder for upload!");
//    }
//  }

  @Override
  public void save(MultipartFile file, String user, String userkey) {

    try {
      String path = new StringBuilder().append(root).append("\\").append(user).toString();
//      String path = new StringBuilder().append(root).append("/").append(user).toString();
      Path roots = Paths.get(path);
      if(!new File(path).exists()) {
        Files.createDirectory(Paths.get(path));
      }


      Files.copy(file.getInputStream(), roots.resolve(file.getOriginalFilename()));

      FileInfo fileInfo = new FileInfo(file.getOriginalFilename(), user, userkey);
      fileRepository.save(fileInfo);

    } catch (Exception e) {
      throw new RuntimeException("Could not store the file. Error: " + e.getMessage());
    }
  }

  @Override
  public Resource load(String filename) {
    try {
      Path file = root.resolve(filename);
      Resource resource = new UrlResource(file.toUri());

      if (resource.exists() || resource.isReadable()) {
        return resource;
      } else {
        throw new RuntimeException("Could not read the file!");
      }
    } catch (MalformedURLException e) {
      throw new RuntimeException("Error: " + e.getMessage());
    }
  }

  @Override
  public void deleteAll(String user) {
    Path root = Paths.get("C:\\shared\\"+user);
//    Path root = Paths.get("./shared/"+user);
    FileSystemUtils.deleteRecursively(root.toFile());
  }

  @Override
  public Stream<Path> loadAll( String user) {

    String path = new StringBuilder().append(root).append("\\").append(user).toString();
//    String path = new StringBuilder().append(root).append("/").append(user).toString();
    root2 = path;
    try {
      return Files.walk(Paths.get(this.root2)).filter(Files::isRegularFile).map(root::relativize);
    } catch (IOException e) {
      throw new RuntimeException("Could not load the files!!");
    }
  }

}
