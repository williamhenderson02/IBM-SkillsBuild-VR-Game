using UnityEngine;
using System.Net;
using System.IO;

public static class DB2apiCloud
{
    public static Response GetNewResponse()
    {
        HttpWebRequest request = (HttpWebRequest)WebRequest.Create("http://127.0.0.1:5000/cloud");
        request.UseDefaultCredentials = true;

        HttpWebResponse response = (HttpWebResponse)request.GetResponse();
        StreamReader reader = new StreamReader(response.GetResponseStream());

        string json = reader.ReadToEnd();

        return JsonUtility.FromJson<Response>(json);

    }
}