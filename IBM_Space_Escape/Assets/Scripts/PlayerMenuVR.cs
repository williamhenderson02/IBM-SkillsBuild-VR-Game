using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.XR;

public class PlayerMenuVR : MonoBehaviour
{
    public GameObject PlayerMenu;
    public GameObject Anchor;
    bool UIActive;
    public InputDeviceCharacteristics controllerCharacteristics;

    private void Start()
    {
        List<InputDevice> devices = new List<InputDevice>();

        PlayerMenu.SetActive(false);
        UIActive = false;

        foreach (var item in devices)
        {
            Debug.Log(item.name + item.characteristics);
        }

        /*
        if(devices.Count > 0)
        {
            targetDevice = devices[0];
        }
        */
        
    }

    private void Update()
    {
        /*
        if (targetDevice.TryGetFeatureValue(CommonUsages.menuButton, out bool primaryButtonValue) && menuButtonValue)
        {
            UIActive = !UIActive;
            PlayerMenu.SetActive(UIActive);
        }
        if (UIActive)
        {
            PlayerMenu.transform.position = Anchor.transform.position;
            PlayerMenu.transform.eulerAngles = new Vector3(Anchor.transform.eulerAngles.x + 15, Anchor.transform.eulerAngles.y, 0);
        }
        */
    }
}
