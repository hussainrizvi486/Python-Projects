import string
import random
import sys

class Functions():
    
    def sets(self):
        Alpha_set = string.ascii_letters
        num_set = string.digits
        symb_set = string.punctuation
        main_set = []
        main_set.extend(Alpha_set)
        main_set.extend(num_set)
        main_set.extend(symb_set)
        return main_set
    
    def Generator(self,name="account name", length:float=9):
        self.name=name
        self.length=length
        main_set = []
        main_set = self.sets()
        random.shuffle(main_set)
        password="".join(main_set[0:self.length])
        F_line=f'The password for {self.name} is : {password}'
        print(F_line)
        usr_options=input(''' 
        2) Exit
        1) Save password
        ''')
        if usr_options=="1":
            with open('file.txt', 'a')as f:
                f.write(self.name+" : "+password+"\n")
        elif usr_options=="2":
            sys.exit()
        else:
            sys.exit()

    
    def Add_Pass_Manually(self, user_name:str="account name", user_password:str="password"):
        self.usr_name=user_name
        self.passwd=user_password
        with open('Hand_pass', "a")as f:
            f.write(self.usr_name+" : "+self.passwd)
    
    def View_Passwords(self, user_choice:str="generator history" ):
        self.choice=user_choice
        if self.choice =="generator history":
            with open("file.txt", "r")as f:
                for data in f.readlines():
                    print(data)
        if self.choice=="Mannual pass":
            with open("Hand_pass", "r")as file:
                for data in file.readlines():
                    print(data)
