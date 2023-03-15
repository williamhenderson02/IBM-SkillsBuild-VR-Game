using UnityEngine;
using System.Net;
using System.IO;

public static class DB2apiSecurity
{
    public static Response GetNewResponse()
    {
        HttpWebRequest request = (HttpWebRequest)WebRequest.Create("http://127.0.0.1:5000/security");
        request.UseDefaultCredentials = true;

        HttpWebResponse response = (HttpWebResponse)request.GetResponse();
        StreamReader reader = new StreamReader(response.GetResponseStream());

        string json = reader.ReadToEnd();

        Debug.Log(json);
        Debug.Log("hi" + JsonUtility.FromJson<Response>(json).rows);

        return JsonUtility.FromJson<Response>(json);

    }
}