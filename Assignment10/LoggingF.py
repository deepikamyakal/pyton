# 7. Logging Framework Simulation
'''
**Concepts Covered:**
Duck Typing, Polymorphism

### Problem Statement

Logging frameworks are used in applications to record system events. Logs can be written to different outputs such as files, databases, or consoles.

Create a simple logging framework simulation using Python.

### Requirements

1. Create multiple logger classes such as:

   * `FileLogger`
   * `ConsoleLogger`
2. Each class should implement a method called `log(message)`.
3. Create a function that accepts a logger object and calls the `log()` method.

### Implementation Guidelines

* The function should not check the object type explicitly.
* It should rely on **duck typing** (if the object has a `log()` method, it works).
* Demonstrate **polymorphism** by passing different logger objects.
+
### Expected Outcome

The same logging function should work with multiple logger types without modification.

'''

class FileLogger:
   
   def log(self, message):
      print("File Log :", message)

class ConsoleLogger:

   def log(self, message):
      print("Console Log :", message)

def logger_system(logger, message):

   logger.log(message)

f1 = FileLogger()
c1 = ConsoleLogger()

logger_system(f1, "Server Started")
logger_system(c1, "Database Connected")
