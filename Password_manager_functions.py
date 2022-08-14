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
    
    
    
    #You must have to create a txt file a name that file on 34
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

    
    #You must have to create a txt file a name that file on 43
    def Add_Pass_Manually(self, user_name:str="account name", user_password:str="password"):
        self.usr_name=user_name
        self.passwd=user_password
        with open('file.txt', "a")as f:
            f.write(self.usr_name+" : "+self.passwd)
            
            
    #Also change name of file in 52 or 56
    def View_Passwords(self, user_choice:str="generator history" ):
        self.choice=user_choice
        if self.choice =="generator history":
            with open("file.txt0", "r")as f:
                for data in f.readlines():
                    print(data)
        if self.choice=="Mannual pass":
            with open("file.txt1", "r")as file:
                for data in file.readlines():
                    print(data)
