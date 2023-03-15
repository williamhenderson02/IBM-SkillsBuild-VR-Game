using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class DataAI : MonoBehaviour
{
    public TextMeshProUGUI qText;
    public TextMeshProUGUI aText1;
    public TextMeshProUGUI aText2;
    public TextMeshProUGUI aText3;
    public TextMeshProUGUI aText4;

    public GameObject CorrectPrompt;
    public GameObject IncorrectPrompt;
    public GameObject CompleteScreen;
    public GameObject QuestionScreen;

    public GameObject aButton1;
    public GameObject aButton2;
    public GameObject aButton3;
    public GameObject aButton4;

    public string[,] rows;
    public int qNo;
    public int rows_count;
 
    public void NewResponse()
    {
        Response r = DB2apiAI.GetNewResponse();
        rows = new string[r.rows_count,7];
        rows_count = r.rows_count;
        for (int i = 0; i < r.rows_count; i++){
            for (int j = 0; j < 7; j++){
                rows[i,j] = r.rows[i*7 + j];
            }
        }
        Debug.Log(rows[0,0]);
    }

    public void Display()
    {
        CorrectPrompt.SetActive(false);
        IncorrectPrompt.SetActive(false);

        aButton1.SetActive(true);
        aButton2.SetActive(true);
        aButton3.SetActive(true);
        aButton4.SetActive(true);

        Debug.Log(rows);
        string questionText = rows[qNo, 1];
        qText.text = "[" + (qNo+1) + ".] " + questionText;

        string option1 = rows[qNo, 2];
        aText1.text = "Answer 1: " + option1;
        string option2 = rows[qNo, 3];
        aText2.text = "Answer 2: " + option2;
        string option3 = rows[qNo, 4];
        aText3.text = "Answer 3: " + option3;
        string option4 = rows[qNo, 5];
        aText4.text = "Answer 4: " + option4;
    }

    public void Check(int num)
    {
        aButton1.SetActive(false);
        aButton2.SetActive(false);
        aButton3.SetActive(false);
        aButton4.SetActive(false);

        string answer = rows[qNo, 6];
        Debug.Log("Pressed answer button, qNo is: " + qNo);

        if (num == int.Parse(answer))
        {
            Debug.Log("num " + num + " is equal to " + rows_count);
            qNo++;
            if(qNo >= rows_count){
                CompleteScreen.SetActive(true);
                CorrectPrompt.SetActive(false);
                IncorrectPrompt.SetActive(false);
                QuestionScreen.SetActive(false);
            }
            else{
                CorrectPrompt.SetActive(true);
            }
        }
        else
        {
            Debug.Log("num " + num + " is not equal to " + int.Parse(answer));
            IncorrectPrompt.SetActive(true);
        }
    }
}

