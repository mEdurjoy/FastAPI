def insert_patient_data(name: str,age: int):

    if type(name)== str and type(age)== int:
        if age < 0:
            raise TypeError("Age can't be negeative")
        else:
            print(name, age)
            print("Inserted into DB")
    else:
        raise TypeError('Incorrect data type')
insert_patient_data(54,40)



"""
Amar ai problem ta somadan er jonno bar bar same vabha code likta hossa
But pydantic ai tar somadhan dai
"""