# 5. API Request Builder using *args and **kwargs
'''
**Concepts Covered:**
Variable Length Arguments (`*args`, `**kwargs`)

### Problem Statement

APIs often accept dynamic parameters depending on the request. A flexible request builder allows developers to pass varying numbers of parameters.

Design a function that constructs an API request dynamically.

### Requirements

1. The function should accept:

   * An endpoint
   * Any number of positional arguments (`*args`)
   * Any number of keyword arguments (`**kwargs`)
2. Display the request structure including:

   * Endpoint
   * Positional parameters
   * Query parameters

### Implementation Guidelines

* Use `*args` to accept variable positional inputs.
* Use `**kwargs` to accept named parameters.
* Print or structure the request parameters clearly.

### Expected Outcome

The function should dynamically handle multiple inputs and simulate building an API request.
'''

def api_request_builder(endpoint, *args, **kwargs):
    
   print("Endpoint :", endpoint)

   print("\nPositional Arguments:")
   for item in args:
      print(item)

   print("\nKeyword Arguments:")
   for key, value in kwargs.items():
      print(key, ":", value)
      
api_request_builder(
    "/users",
    "id=101",
    "active=true",
    method="GET",
    timeout=30
)