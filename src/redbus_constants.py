DB_HOST_NAME = "sql12.freesqldatabase.com"
DB_USER_NAME = "sql12725153"
DB_PASSWORD = "7ktkxKAi64"
DBNAME = "sql12725153"
RED_BUS_URL = "https://www.redbus.in/online-booking/rtc-directory"

DB_SCHEMA = """
                id INT AUTO_INCREMENT PRIMARY KEY,
                Text VARCHAR(255) NOT NULL,
                Link VARCHAR(255) NOT NULL

                """
RED_BUS_INFO = """

                id INT PRIMARY KEY AUTO_INCREMENT,         
                route_name TEXT NOT NULL,               
                route_link TEXT NOT NULL,                   
                busname TEXT NOT NULL,                      
                bustype TEXT NOT NULL,                      
                departing_time TIME NOT NULL,               
                duration TEXT NOT NULL,                     
                reaching_time TIME NOT NULL,                
                star_rating FLOAT,                        
                price DECIMAL(10, 2) NOT NULL,              
                seats_available INT NOT NULL 
                
                """
RED_BUS_MAIN_TABLE = "live_redbus_data"