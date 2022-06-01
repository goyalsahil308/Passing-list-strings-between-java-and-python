package com.APIMain;
import java.io.IOException;
import java.net.HttpRetryException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
public class APIMain
{
    public static void main(String[] args) throws IOException,InterruptedException
    {
        var url="http://127.0.0.1:5000/";
        var request=HttpRequest.newBuilder().GET().uri(URI.create(url)).build();
        var client=HttpClient.newBuilder().build();
        var response=client.send(request, HttpResponse.BodyHandlers.ofString());
        // System.out.println(response.statusCode());
        System.out.println(response.body());
        System.out.println(response.getClass().getSimpleName());
    }  
 
}