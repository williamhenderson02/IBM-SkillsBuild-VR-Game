using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class QuizController : MonoBehaviour
{
    public GameObject welcomeScreen;
    public GameObject questionScreen;
    public GameObject a1Object;
    public GameObject a2Object;
    public GameObject a3Object;
    public GameObject a4Object;

    public void StartQuiz()
    {
        welcomeScreen.SetActive(false);
        questionScreen.SetActive(true);
        a1Object.SetActive(true);
        a2Object.SetActive(true);
        a3Object.SetActive(true);
        a4Object.SetActive(true);
    }
}
