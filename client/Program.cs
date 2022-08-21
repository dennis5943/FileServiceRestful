using System.Net.Http.Headers ;
using System.Net.Http;
using Microsoft.Extensions.DependencyInjection;

public static class MainClass{
    public static async Task Main(string[] args){
        // See https://aka.ms/new-console-template for more information
        Console.WriteLine("Hello, World!11");


        var filePath = @"任賢齊 心太軟.mp3";

        using (var multipartFormContent = new MultipartFormDataContent())
        {
            //Load the file and set the file's Content-Type header
            var fileStreamContent = new StreamContent(File.OpenRead(filePath));
            fileStreamContent.Headers.ContentType = new MediaTypeHeaderValue("audio/mpeg");

            //Add the file
            multipartFormContent.Add(fileStreamContent, name: "file", fileName: "heart.mp3");

            //Send it

            var httpClient = new HttpClient();

            var response = await httpClient.PostAsync("http://localhost:8006/upload-file", multipartFormContent);
            response.EnsureSuccessStatusCode();
            var res =  await response.Content.ReadAsStringAsync();
        }

    }
}