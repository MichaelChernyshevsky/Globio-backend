class SQLConstants:
    user_table_file = "data/user_database.db"
    user_table_name ='user_table'
    user_table_create_request = """
        CREATE TABLE IF NOT EXISTS my_table (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
        );
        """
    def getAllRequest(name):
        return f"SELECT * FROM {name}"

    def getTable(name):
        return f"""
                CREATE TABLE IF NOT EXISTS {name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER
                );
            """
     
    

    
