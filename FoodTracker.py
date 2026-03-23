import re 
import csv
from datetime import datetime 

Users = []

class AccountInfo: 
    def _init_(self, username, password):
        if not  username:
            raise ValueError ("Missing Username ")
        if not password:
            raise ValueError (" Missing Password")
        self.username = username 
        self.password = password

class User(AccountInfo):
    def _init_(self, username, password):
        super()._init_(username,password)
        self.meals =[]

    def add_meal(self, meal_type, fats, carbs, protein, calories, date):
        entry = FoodEntry(meal_type, fats, carbs, protein, calories, date)
        self.meals.append(entry)



class FoodEntry:
    def __init__(self,meal_type, fats, carbs, protein, calories,date):
        self.meal_type = meal_type
        self.fats = fats
        self.carbs = carbs 
        self.protein = protein
        self.calories = calories 
        self.date = date 

def SignUp():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user = User(username, password)
    Users.append(user)
    print("Account has been made, goodluck on your journey!") 
    
def SignIn():
    username = input("Entere your username: ")
    password = input("Enter your password: ")
    for user in Users:
        if username == user.username and password == user.password:
            print("Welcome back, " + username + "Hope you have a good day!")
            return user 
    print("Invalid username or password has been entered please try again")


    





        





        



