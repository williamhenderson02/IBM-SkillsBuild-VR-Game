using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class DataDataScience : MonoBehaviour
{
    public TextMeshProUGUI responseText;

    public void NewResponse()
    {
        Response r = DB2apiDataScience.GetNewResponse();
        string[] columns = r.columns;
        string[] rows = r.rows;
        responseText.text = columns[0];
    }
}

