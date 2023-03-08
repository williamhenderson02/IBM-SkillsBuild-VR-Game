using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class MenuController : MonoBehaviour
{
    public void StartBtn()
    {
        SceneManager.LoadScene("Lobby");
    }

    public void QuitBtn()
    {
        Application.Quit();
        Debug.Log("Quit Game");
    }
}