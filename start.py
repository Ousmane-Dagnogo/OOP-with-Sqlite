import sqlite3

#Connecting to a database
conn = sqlite3.connect("mydata.db")

#This is important to start making queries
c = conn.cursor()


class Person:
    def __init__(self, first=None, last=None,age=None):
        self.first = first
        self.last = last
        self.age = age

    def clone_person(self, result):
        self .first = result[0]
        self .last = result[1]
        self .age = result[2]

c.execute("""SELECT * FROM persons WHERE last_name = 'Smith'""")
person1 = Person()
person1.clone_person(c.fetchone())



print(person1.first)
print(person1.last)
print(person1.age)


person2 = Person("Bob", "Davis", 23)
c.execute("""INSERT INTO persons VALUES( ? , ? ,? )""".format(person2.first,person2.last,person2.age))

#conn.commit()
#conn.close()



c.execute("SELECT * FROM persons")
print(c.fetchall())

