'''
5) create_account(name, role="User")

**Question:**
Create a function with default role.

**Test Case 1:**
Input:
create_account("Rahul")

Expected Output:
Account created for Rahul with role User
'''
def create_account(name, role = "User"):
    print(f"Account created for {name} with role {role}")       # Account created for Rahul with role User
    
create_account("Rahul")