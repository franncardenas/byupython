import pytest
import mysql.connector
from window import window
from finalproject import Students

cnn = mysql.connector.connect(host="localhost", user="root", 
            passwd="root", database="school")

student = Students()
window = window()
def test_num_charac_InText():

    #Verify num_charac_InText function with numbers and special character
    assert window.num_charac_InText('James#%') == False
    assert window.num_charac_InText('James') == True
    assert window.num_charac_InText('1481298') == False
    assert window.num_charac_InText('J4mes') == False
    assert window.num_charac_InText('+}{,}}') == False

def test_delete_student():

    key = 2
    data = student.delete_student(key)
    assert isinstance(data, int)

def test_query_allstudents():

    # Verify that the query_allstudents function returned a string.
    data = student.query_allstudents()

    assert isinstance(data, list)
    assert len(data) >= 0


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])