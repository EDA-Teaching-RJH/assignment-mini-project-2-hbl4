import re 
import csv
from datetime import datetime 

class AccountInfo: 
    def _init_(self, username, password):
        if not  username:
            raise ValueError ("Missing Username ")
        if not password:
            raise ValueError (" Missing Password")
        self.username = username 
        self.password = password

class user(AccountInfo):
    def _init_(self, username, password):
        super()._init_(username,password)



