using IBM.Data.DB2.Core;
using System.Data;
using IBM.Data.DB2;
using UnityEngine;

public class db2
{
    private static string connectionString = "Database=Space-Escape-dB2;Hostname=bs2ipcul0apon0jufi80lite.db2.cloud.ibm.com;Port=31929;Protocol=TCPIP;UID=frx98001;PWD=rFKWq6qM3zKKP7pd;";

    //[RuntimeInitializeOnLoadMethod]
    static void Start()
    {
        // Create connection
        using (DB2Connection connection = new DB2Connection(connectionString))
        {
            connection.Open();

            // Create a SQL command object
            using (DB2Command command = connection.CreateCommand())
            {
                command.CommandText = "SELECT * FROM USERS";
                command.CommandType = CommandType.Text;

                // Execute the SQL command and read the results
                using (DB2DataReader reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        // Access column values using reader methods
                        int id = reader.GetInt32(0);
                        string username = reader.GetString(1);
                        string password = reader.GetString(2);
                    }
                }
            }

            // Close connection
            connection.Close();
        }
    }
}
