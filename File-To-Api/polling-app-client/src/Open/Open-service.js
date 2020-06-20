// import http from "./open-http"


import axios from "axios";

class OpenService{

    openupload(userport,username, userkey){
        const http = axios.create({
            baseURL: "http://localhost:"+userport,
            headers: {
              "Content-type": "application/json"
            }
          });

        return http.post("/start?user=" + username +"&userKey="+userkey)
    }

    opendelte(userport,tablename,userkey){
        const http = axios.create({
            baseURL: "http://localhost:"+userport,
            headers: {
              "Content-type": "application/json"
            }
          });
        //   console.log(http.delete(tablename + "/delete?key=" + userkey))
        return http.delete(tablename + "/delete?key=" + userkey)
    }
}
export default new OpenService();