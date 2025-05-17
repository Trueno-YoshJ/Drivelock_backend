package com.Backend.backend;

import com.Backend.backend.GpsData;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("api")
@CrossOrigin(origins= "*")
public class GpsController {
    @PostMapping("/gps")
    public String recieveGpaData(@RequestBody GpsData data){
        System.out.println("Latitude : " + data.getLatitude());
        System.out.println("Longitude : " + data.getLongitude());
        return "GPS Data Received Successfully.";
    }
    @GetMapping("/test")
    public String testConnection(){
        return "Backend is connected.";
    }
}
