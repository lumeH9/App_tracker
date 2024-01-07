import pypyodbc as odbc

# function saves the gathered data into a database
# response contains dictionary of all the data that was gathered ie. app names and seconds used

def save_data(response):
    # setting up the needed variables to establish database connection
    DRIVER_NAME = 'SQL SERVER'
    SERVER_NAME = 'VERNERI-LENOVO\SQLEXPRESS'
    DATABASE_NAME = 'App_tracker'

    connection_string = f"""
        DRIVER={{{DRIVER_NAME}}};
        SERVER={SERVER_NAME};
        DATABASE={DATABASE_NAME};
        Trust_Connection=yes;
    """
    # connecting to database
    conn = odbc.connect(connection_string)
    print(conn)

    # creating cursor to execute SQL code
    cursor = conn.cursor()

    # making sure database table doesnt already exist before we create it
    cursor.execute('''
        IF OBJECT_ID(N'dbo.Tracking', N'U') IS NULL
        CREATE TABLE dbo.Tracking (
        App_name TEXT NOT NULL,
        Seconds_used INT NOT NULL
        );
    ''')
    # looping through all the dictionary key-value pairs and inserting them into database
    for key in response.keys():
        cursor.execute("INSERT INTO Tracking VALUES (?, ?)", (key, response[key]))
        
    # committing changes and closing cursor and connection just in case
    conn.commit()
    cursor.close()
    conn.close()
    return conn, cursor