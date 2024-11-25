from tkinter import *
from window import *
import mysql.connector



def main():
    root = Tk()
    root.wm_title("List of students")
    app = window(root)
    app.mainloop()



class Students:
    
    def __init__(self):
        try:
            self.cnn = mysql.connector.connect(host="localhost", user="root", 
            passwd="root", database="school")
        except:
            print("Verify user and password")


    def query_allstudents(self):
        try:
            cur = self.cnn.cursor()
            cur.execute("SELECT * FROM students")
            data = cur.fetchall()
            cur.close()    
            return data
        except:
            print("This table not exist")
    
    def insert_student(self, first_name, last_name, country_birth, age):
        try:
            cur = self.cnn.cursor()
            sql='''INSERT INTO students (first_name, last_name, country_birth, age) 
            VALUES('{}', '{}', '{}', '{}')'''.format(first_name, last_name, country_birth, age)
            cur.execute(sql)
            n=cur.rowcount
            self.cnn.commit()    
            cur.close()
            return n 
        except:
            print('Error Code: Incorrect integer value in the "Age" column')
                
    def delete_student(self, Id):
        
            cur = self.cnn.cursor()
            sql='''DELETE FROM students WHERE Id = {}'''.format(Id)
            cur.execute(sql)
            n=cur.rowcount
            self.cnn.commit()
            cur.close()
            return n
    



if __name__=='__main__':
    main()
