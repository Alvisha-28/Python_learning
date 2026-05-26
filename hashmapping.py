'''technique store data quickly
search data quickly
delete data quickly
access data in 0(n)
frequently used in database and caching
it converts key into hash code and stores the value in that location'''
# advith is developing manage membership id system for gym



# Advith is developing a program to manage memberships for a local gym. Each member has a 
# unique ID number, and Advith have two lists: one containing the IDs of all current gym 
# members, and another containing the IDs of members who have signed up for a special class. 
# Advith task is to determine whether all the members who signed up for the class are already 
# existing gym members. Help Advith  to solve this problem using a hashing technique.
n,m = map(int, input("Enter the number of gym members and class sign-ups: ").split())
gym_members = list(map(int, input("Enter the IDs of gym members: ").split()))
class_signups = list(map(int, input("Enter the IDs of class sign-ups: ").split()))
gym_member_set = set(gym_members)
count = 0
for num in class_signups:
    if num in gym_member_set:
        count += 1
        if count == m:
            print("its a subset")
            




