using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class WorldController : MonoBehaviour
{
    public bool AIDone;
    public bool CloudDone;
    public bool DataScienceDone;
    public bool SecurityDone;

    public GameObject FinishButton;

    // Update is called once per frame
    void Update()
    {
        if(AIDone && CloudDone && DataScienceDone && SecurityDone)
        {
            FinishButton.SetActive(true);
        }
    }

    public void endGame()
    {
        Application.Quit();
        Debug.Log("Quit Game");
    }

    public void WinAI(){
        AIDone = true;
    }

    public void WinCloud(){
        CloudDone = true;
    }

    public void WinDataScience(){
        DataScienceDone = true;
    }

    public void WinSecurity(){
        Debug.Log("WinSecurity!!!" + AIDone);
        SecurityDone = true;
    }

}
