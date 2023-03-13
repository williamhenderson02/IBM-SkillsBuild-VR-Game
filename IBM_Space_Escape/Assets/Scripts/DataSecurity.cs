using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class DataSecurity : MonoBehaviour
{
    public TextMeshProUGUI responseText;
    public string[,] rows;
 
    public void NewResponse()
    {
        Response r = DB2apiSecurity.GetNewResponse();
        rows = r.rows;

    }

    public void Display(int qNo)
    {
        string questionText = rows[qNo, 1];

        string option1 = rows[qNo, 2];
        string option2 = rows[qNo, 3];
        string option3 = rows[qNo, 4];
        string option4 = rows[qNo, 5];
    }

    public void Check(int num, int qNo)
    {
        string answer = rows[qNo, 6];

        if (num == int.Parse(answer))
        {
            // do something
        }
        else
        {
            // incorrect
        }
    }
}

