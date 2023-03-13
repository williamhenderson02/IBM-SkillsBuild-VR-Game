using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RoomTeleportController : MonoBehaviour
{
    public GameObject origin;
    public GameObject destinationObject;

    public void TeleportToRoom()
    {
        origin.transform.position = destinationObject.transform.position;
    }
}
