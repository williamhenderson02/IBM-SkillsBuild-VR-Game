using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class DataSecurity : MonoBehaviour
{
    public TextMeshProUGUI responseText;

    public void NewResponse()
    {
        Response c = DB2apiSecurity.GetNewResponse();
        responseText.text = c.command;
    }
}

