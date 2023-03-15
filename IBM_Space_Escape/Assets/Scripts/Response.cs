[System.Serializable]

public class Response
{
    public string[] columns;
    public string[] columns_type;
    public string command;
    public int index;
    public int limit;
    public string[,] rows;
    public int rows_count;
    public double runtime_seconds;

}
