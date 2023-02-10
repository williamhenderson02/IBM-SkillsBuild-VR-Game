using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour
{
    void Start()
    {
        string connectionString = "Server=<f0f1180a-bfe5-45db-9189-9a2780c7eb16.bs2io90l08kqb1od8lcg.databases.appdomain.cloud>;Port=<30098>;Database=<bludb>;User ID=<tgpz35@durham.ac.uk>;Password=<Z7dE6pMk02owfRTjp!6B>;";

        using (SqlConnection connection = new SqlConnection(connectionString))
        {
            connection.Open();
            using (SqlCommand command = new SqlCommand("SELECT * FROM <table>", connection))
            {
                using (SqlDataReader reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        for (int i = 0; i < reader.FieldCount; i++)
                        {
                            Debug.Log(reader.GetValue(i));
                        }
                    }
                }
            }
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}