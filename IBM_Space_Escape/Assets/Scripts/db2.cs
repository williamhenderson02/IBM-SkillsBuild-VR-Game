using IBM.Data.DB2.Core;
using System.Data;

public class DB2Connector
{
    private string connectionString = "Database=<database_name>;UserID=<user_id>;Password=<password>;Server=<server_name>.databases.appdomain.cloud:50000/;";

    public void QueryDatabase(string query)
    {
        using (DB2Connection connection = new DB2Connection(connectionString))
        {
            connection.Open();

            using (DB2Command command = connection.CreateCommand())
            {
                command.CommandType = CommandType.Text;
                command.CommandText = query;

                using (DB2DataReader reader = command.ExecuteReader())
                {
                    // Handle the returned data
                }
            }

            connection.Close();
        }
    }
}