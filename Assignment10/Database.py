# 4. Database Connection Class
'''
**Concepts Covered:**
Inheritance, Constructor Overriding

### Problem Statement

Most applications interact with databases such as MySQL, PostgreSQL, or MongoDB. To simplify connection management, developers often design base classes that provide common database connection functionality.

Design a database connection system using inheritance.

### Requirements

1. Create a base class named `DatabaseConnection`.
2. The constructor should accept parameters such as:

   * Host
   * Port
3. Create a subclass named `MySQLDatabase`.
4. Override the constructor in the subclass to include additional attributes such as:

   * Username
   * Password

### Implementation Guidelines

* Use `super()` to call the parent constructor.
* Demonstrate how child classes extend functionality from the base class.

### Expected Outcome

The program should simulate connecting to a database using inherited properties and overridden constructors.
'''
class DatabaseConnection:
    
   def __init__(self, host, port):
      self.host = host
      self.port = port

   def display(self):
      print("Host :", self.host)
      print("Port :", self.port)

class MySQLDatabase(DatabaseConnection):
   
   def __init__(self, host, port, username, password):
      super().__init__(host, port) 

      self.username = username
      self.password = password

   def connect(self):
      print("Connected to MySQL Database")
      print("Username :", self.username)

db = MySQLDatabase(
   "localhost",
   3306,
   "root",
   "root123"
)

db.display()
db.connect()