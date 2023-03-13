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
        Response c = DB2apiDataScience.GetNewResponse();
        responseText.text = c.command;
    }
}

