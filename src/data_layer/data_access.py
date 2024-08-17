from src.redbus_constants import DB_HOST_NAME ,  DB_USER_NAME ,DB_PASSWORD
from src.logger import logging
import pymysql
class RedBusData:
    '''
     blueprint for performimg
     DB CRUD operations
    '''


    def __init__(self):
        self.connection =None
    def create_connection(self , database):
        logging.info("Creating DB Connection")
        self.connection= pymysql.connect(
            host=DB_HOST_NAME ,       
            user= DB_USER_NAME ,      
            password=DB_PASSWORD  , 
            database=database ,
            port=3306,
            connect_timeout=20   
        )
        if not self.connection:
            return False
        return True
    
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
       
        drop_query = f"DROP TABLE IF EXISTS {table_name};"
        self.execute_query(drop_query)
        
        
        create_query = f"""
        CREATE TABLE {table_name} (
            {table_schema}
        );
        """
        self.execute_query(create_query)


    def insert_data(self, table_name, columns, values):
        print(values)
        col = ','.join(columns)
        val = ','.join(str(element) for element in values)
        parts = val.split(',')
        formatted_val = f"'{parts[0]}','{parts[1]}'"
        print("VAL" ,formatted_val)
        query = f"""
        INSERT INTO {table_name} ({col})
        VALUES {values};
        """
        print("QUERY" ,query)
        cursor = self.connection.cursor()
        #cursor.execute(query,values)
        self.execute_query(query)

    def fetch_data(self, query):
        return self.execute_query(query,  fetch=True)

        