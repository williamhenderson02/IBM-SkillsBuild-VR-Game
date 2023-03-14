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
    public string[,] rows;
    public int qNo;
 
    public string[,] NewResponse()
    {
        Response r = DB2apiAI.GetNewResponse();
        rows = r.rows;
        return rows;
    }

    public void Display()
    {
        rows = NewResponse();
        string questionText = rows[qNo, 1];
        Debug.Log("::::" + questionText);
        qText.text = "[]" + qNo + ".] " + questionText;

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
        string answer = rows[qNo, 6];

        if (num == int.Parse(answer))
        {
            // do something
            Debug.Log("");
        }
        else
        {
            Debug.Log("");
            // incorrect
        }
    }
}

