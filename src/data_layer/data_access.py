from src.redbus_constants import DB_HOST_NAME ,  DB_USER_NAME ,DB_PASSWORD
import pymysql
class RedBusData:
    '''
     blueprint for performimg
     DB CRUD operations
    '''


    def __init__(self):
        self.connection =None
    def create_connection(self , database):
        self.connection= pymysql.connect(
            host=DB_HOST_NAME ,       
            user= DB_USER_NAME ,      
            password=DB_PASSWORD  , 
            database=database   
        )
    
    def execute_query(self,query, fetch=False):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                if fetch:
                    result = cursor.fetchall()
                    return result
            self.connection.commit()
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
            self.connection.rollback()

    def create_table_if_not_exists(self, table_name, table_schema):
        query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            {table_schema}
        );
        """
        self.execute_query(query)

    def insert_data(self, table_name, columns, values):
        query = f"""
        INSERT INTO {table_name} ({columns})
        VALUES ({values});
        """
        self.execute_query(query)

    def fetch_data(self, query):
        return self.execute_query(query,  fetch=True)

        