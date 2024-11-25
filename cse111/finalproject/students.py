import mysql.connector

class Students:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="root", database="school")

    def __str__(self):
        data=self.query_allstudents()        
        aux=""
        for row in data:
            aux=aux + str(row) + "\n"
        return aux

    def query_allstudents(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM students")
        data = cur.fetchall()
        cur.close()    
        return data
    
    def insert_student(self, first_name, last_name, country_birth, age):
        cur = self.cnn.cursor()
        sql='''INSERT INTO students (first_name, last_name, country_birth, age) 
        VALUES('{}', '{}', '{}', '{}')'''.format(first_name, last_name, country_birth, age)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n 
    
    def delete_student(self, Id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM students WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()
        cur.close()
        return n
    