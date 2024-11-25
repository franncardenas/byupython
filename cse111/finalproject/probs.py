def query_examplestudent(self):
        cur = self.cnn.cursor()
        sql= ('''CREATE DATABASE IF NOT EXISTS school;
        USE school;

        -- schema
        CREATE TABLE students  (
            Id INT NOT NULL AUTO_INCREMENT,
            first_name VARCHAR(256) NOT NULL,
            last_name VARCHAR(256) NOT NULL,
            country_birth VARCHAR(256) NOT NULL,
            age int NOT NULL,
            PRIMARY KEY(Id)
        );
        INSERT INTO students (first_name, last_name, country_birth, age)
        VALUES ({},{},{},{},{},{},{},{},{});''').format(('Franco', 'Cardenas', 'Argentina', '24'),
                     ('Valentin', 'Mendez', 'Mexico', '23'),
                     ('Cecilia', 'Cuadrado', 'Germany', '22'),
                     ('Leah', 'Streber', 'switzerland ', '20'),
                     ('Harry', 'Davies', 'Canada', '25'),
                     ('Noah', 'Taylor', 'United States', '21'),
                     ('Charles', 'Johnson', 'England', '21'),
                     ('James', 'Murphy', 'United States', '23'),
                     ('Dustin', 'Hunt', 'United States', '25'))
        cur.execute(sql)
        self.cnn.commit()    
        cur.close()