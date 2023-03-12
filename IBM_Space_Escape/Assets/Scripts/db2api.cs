using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;

public class db2api : MonoBehaviour
{
    private static string url = "http://localhost:5000/api/users"; // Replace with the actual URL of your Python API endpoint

    [RuntimeInitializeOnLoadMethod]
    static void Init()
    {
        GetUsers();
    }

    static void GetUsers()
    {
        UnityWebRequest www = UnityWebRequest.Get(url);
        www.SendWebRequest();

        while (!www.isDone)
        {
            // Wait for the request to complete
        }

        if (www.result == UnityWebRequest.Result.ConnectionError || www.result == UnityWebRequest.Result.ProtocolError)
        {
            Debug.LogError("Error: " + www.error);
        }
        else
        {
            string jsonResponse = www.downloadHandler.text;
            List<User> users = JsonUtility.FromJson<List<User>>(jsonResponse);

            foreach (User user in users)
            {
                Debug.Log("User ID: " + user.id + ", Username: " + user.username + ", Password: " + user.password);
            }
        }
    }

    [System.Serializable]
    public class User
    {
        public int id;
        public string username;
        public string password;
    }
}
