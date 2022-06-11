#Libraries
import pandas as pd
import mysql.connector as mysql
from db_credential import * #(import mysql_db_config)

#I've just set up the queries that I will most likely use
load_applicants_query=("""INSERT INTO GPE_DATABASE.Applicants
    (student_code,
     name,
     email,
     student_id,
     address,
     neighborhood,
     city,
     phone_number,
     current_status,
     internet_access,
     highschool,
     secoundary_school,
     race,
     father_education,
     mother_education,
     tutelary_ecucation,
     avg_income_percapita,
     father_occuparion,
     mother_occupation,
     personal_occupation,
     matao_residence,
     who_living_with_you,
     age,
     vehicle,
     marital_status,
     books,
     books_type,
     movie_theather,
     museum,
     additional_courses,
     career,
     study_room,
     computers,
     smartphones,
     parents_conversation)
    
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                      )

load_studens_query =("""INSERT INTO GPE_DATABASE.Students
        (student_code,NSE,start_date, end_date, volunteer_id)
        VALUES (%s, %s,%s, %s, %s) """)


load_exams_query =("""INSERT INTO GPE_DATABASE.Exams (
     student_code,
     exame_number,
     geography,
     biology,
     chemistry,
     history,
     math,
     physics,
     portuguese,
     literature,
     english,
     interdisciplinary)
     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"""
                  )
#Generic drop query to drop records if needing
drop_query = ("""
    DELETE FROM GPE_DATABASE.{table_name}
    WHERE {column_name} {operator} {values}
    """)

# Since most of fields of Students table don't have a data source (Someone has to insert values manually.), I set up a query to quickly update values. (I don't activate it yet)
update_students = ("""
        UPDATE GPE_DATABASE.Students
        SET NSE = %(value1)s, start_date = %(value2)s, end_date = %(value3)s, volunteer_id = %(value4)s
        WHERE student_code = %(condition)s
        """)



class MySQL_Queries:
    def __init__(self,db_connection: dict, table_name: str):
        self.db_connection = db_connection
        self.table_name = table_name
        
    #Function to insert data into MySQL database
    def insert_data(self, data: pd.DataFrame):
        "The input obj must be a  proper pandas dataframe"
        
        #Signing the sql query
        if self.table_name == "Applicants":
            add,values = load_applicants_query.split('VALUES')
            values = 'VALUES' + values
            
        elif self.table_name == "Students":
            add,values = load_studens_query.split('VALUES')
            values = 'VALUES' + values
            
        elif self.table_name == "Exams":
            add,values = load_exams_query.split('VALUES')
            values = 'VALUES' + values
     
        #target database > mysql
        conn = mysql.connect(**self.db_connection)
        cursor = conn.cursor(buffered=True)

        #Insert new candidate
        try:
            row_num =len(data) 

            if row_num == 1:
                insert_query = add + values
                cursor.execute(operation =insert_query, params= tuple(data.to_numpy()[0]))
                conn.commit()
                cursor.close()
                conn.close()
                print(f"The query of inserting values into the {self.table_name} Table was successfully executed")

            else:
                values = (values + ',\n' + (values.strip('VALUES ') + ',\n ') *(row_num-1)).strip(',\n ')
                insert_query = add + "\n" + values

                multi_rows= ()
                for  row in data.itertuples(index = False, name = None):
                    multi_rows += row

                cursor.execute(operation =insert_query, params=  multi_rows)
                conn.commit()
                cursor.close()
                conn.close()
                print(f"The query of inserting values into the {self.table_name} Table was successfully executed")

        except BaseException as e:
            print(e)
            print(f"Query of inserting values into the {self.table_name} Table was not executed")
            cursor.close()
            conn.close()   

    #Function to drop data from MySQL database
    def drop_data(self, condition: dict):
        """The input obj must be a dictionary.
        The dictionary has only 1 item in which the key is the column name of the db,
        and the value is a string or tuple containing all desired values from that column

        e.g., condition = {'student_code':('100022', '100222', '100322', '100522')} """
        
        #target database > mysql
        conn = mysql.connect(**self.db_connection)
        cursor = conn.cursor(buffered=True)
    
        #Setting and Running the query
        try: 
            column_name = list(condition.keys())[0]
            values = list(condition.values())[0]

            #setting operator for WHERE clause
            if type(values) is tuple:
                operator = "in"
            else:
                operator = '='
            
            #MySQL Query
            
            
            cursor.execute(operation= drop_query.format(table_name = self.table_name, column_name =
                                                        column_name , operator = operator,values = values))
            conn.commit()
            cursor.close()
            conn.close()
            print(f"The query of dropping values from the {self.table_name} Table was successfully executed")

        except BaseException as e:
            print(e)
            cursor.close()
            conn.close()
            print(f"Query of dropping values from the {self.table_name} Table was not executed")
       