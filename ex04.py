record=set()     #define a null global set type to save the letters of formulas, for
                 #the challenge 3 and 4. the reason why chose set because it has the function of remove repititions.

class Expr: #superclass for connecting class Var and sign.
    pass

class Var (Expr) : # class Var is for saving the keys and values of letters.
    def __init__(self,letter): # save the keys of these letters
        self.name = letter    
        record.add(self.name)  # record them by global set type
    def eva(self):             # def eva for withdraw these keys of Var saved if other class wanna use
        return f"{self.name}"  # control the return type to confirm it can be used by dict type
    def eval(self,dic):          # def op to withdraw the values based on these keys 
        return dic[self.eva()] # use the key to get the value(use self.name is also ok in there) 
    def __str__(self):         # def __str__ for exporting in print
        record.clear()         # clean the record up to ensure it dont save unnecessary key after a print().
        return f"{self.name}"  # back the outcome for print()
    def add(self):             # def a add for challenge 4. because in this we dont use print to run
        record.add(self.name)  # these classes, so we need another way to add letters to record
        return


class sign(Expr):
    def __init__(self,imp1,imp2): # save the two Var between the sign  
        self.left = imp1          # save the left 
        self.right = imp2         # save the right
    def add(self): # def add() to send argue of adding new key in record for challenge 3,4
        self.left.add()
        self.right.add()
    def make_tt(self):            # def make_tt for the challenge 3
        dic={}                    # def a null dictionary
        global truthtable         # def a global list
        truthtable = ""           # give it a value
        self.add()                # it a recursion for different signs until the Var()
        for i in sorted(record):          # transfer the keys from record to this dictionary
            dic[str(i)]=None      # get these key values of None
        lis=(list(dic.keys()))    # create a list to save all keys 
        lis.sort()                #modify the sequence
        lis = lis[::-1]           # i dont like this , it just for keeping the similar sequence with test04, our design thinking have some difference
        for i in range(len(lis)):
            truthtable += f"{lis[i]}"+" "*6+"|" # and print these key as the first line of titles
        if dic =={}:              # it is a mechanism to protect the correct import type(to test if the record is null)
            print("import error,please check it (-_-)")
            return
        truthtable += f"{self}\n"          # print the self of class(formula,lke x&(y|z) )
        self.recur(dic,lis,0)     # run the recursion to let the values of these key to be True and False sucessively
        record.clear()            # clean up the record
        return truthtable                 # to avoid print none in print,because we would use like(print(e4.make_tt())),so if we dont give a return for the outside print, it will export None
    def recur(self,dic,lis,n):    # def the recursion like i said
        if n == len(lis):         # firtly, i need to check the length of the list to avoid unlimited running
            return
        for m in [True,False]:    # let the values of the dic we defined in make_tt() equal True and False sucessively
            dic[lis[n]]= m        # locate these key and their values by the list we defined in make_tt()
            if None not in dict(dic).values():# we can export it if there are not Nones in the values of this dict
                self.run(dic)     # i would define run() to print the values by specific type
            self.recur(dic,lis,n+1) # do recursion
        if n>0:                   # except for the node1, other nodes' values should back to None
            dic[lis[n]]=None
            return
        # the designing thinking of this recursion is binary tree
        # so we can use node1 as base to do traversing
        #   x      y     z   
        #  True  True  True
        #              False
        #        False True
        #              False
        #  False True  True
        #              False
        #        False True
        #              False   
    def run(self,dic): # def run to print the values of dict by specific type
        global truthtable # we would change its value
        for i in dic:  # traversing the key of a dict
            if dic[i]==True: # because the lenth of letters of Flase are long than True, so we need to print by if to retain alignment
                truthtable += f"{dic[i]}"+" "*3+"|"# the amount of " " depends of many tries.
            else: 
                truthtable += f"{dic[i]}"+" "*2+"|"# False is long than True, so it just need two " "
        truthtable += f"{self.eval(dic)}\n"#  print the outcome of calculations
        return truthtable
    def isTauto(self): # def isTauto for challenge 4
        dic = {}       # like the effect of dic in make_tt()
        self.add()     # it a recursion for different signs until the Var()
        for i in set(record): # transfer the key from records to dict
            dic[str(i)]=None
        lis=(list(dic.keys())) # save the keys of records
        que=[]                 # define que to save dicts which saved the outcome of different calculations
        self.Tauto(dic,lis,0,que) # do recursion by giving different values to keys
        record.clear()         # clean up the record
        if False not in que :  #judge if the proposition is a tautology(if there is a False in its outcome,it isnt a tauto, else it is)
            print(True)
        else : print(False)
        return ""
    def Tauto(self,dic,lis,n,que): # get the list of outcomes when key get various values(True or False)
        if n == len(lis):  #like the recur()
            return
        for m in [True,False]:
            dic[lis[n]]= m
            if None not in dict(dic).values():
                que+=[self.eval(dic)] # que add this outcome
            self.Tauto(dic,lis,n+1,que)
        if n>0:
            dic[lis[n]]=None
        return    
    

class Not(sign):
    def __init__(self,imp1):# to overwrite the __init__ in sign because not just one key to tackle
        self.name=imp1    
    def eva(self): # return the Not execute as the type "!" and it would be the judging condition of __str__
        return f"!{self.name}"    
    def eval(self,dic): # use recursion to return Not execute and argue the Var(key) from next object class until class Var
        return not self.name.eval(dic)    # deliver the dic to is next object
    def __str__(self):  # define the type when it would be printed
        if ('&' in self.name.eva())or('|'in self.name.eva())or('=='in self.name.eva()): #becuase the priority of Not is highest, so when it check & or | or == inslef.name.eva()(i defined it for judge in there)
            return f"!({self.name})" # if it has, add ()
        else: 
            return f"!{self.name}" # if not, dont need to add ()
    def add(self): # overwrite add() in sign and def add() to send argue of adding new key in record for challenge 4
        self.name.add() # send argue to next object
        

class And(sign):
    def eval(self,dic):# use recursion to return And execute and argue the Var(key) from next object class until class Var
        return self.left.eval(dic) and self.right.eval(dic)
    def eva(self):# return the Not execute as the type "&" and it would be the judging condition of __str__
        return f"{self.left}&{self.right}"
    def __str__(self):# becuase the priority of And is second highest, so when it check | or == inslef.name.eva()(i defined it for judge in there)
        if (('|'in self.left.eva())or('=='in self.left.eva())) and (('|' in self.right.eva()) or ('==' in self.right.eva())):# if there has a lower prority sign in self.right and not in self.left, add () in self.right
            return f"({self.left})&({self.right})"
        elif (('|'in self.left.eva())or('=='in self.left.eva()))and not(('|' in self.right.eva()) or ('==' in self.right.eva())):# if there has a lower prority sign in self.left and not in self.right, add () in self.left
            return f"({self.left})&{self.right}"
        elif not(('|'in self.left.eva())or('=='in self.left.eva()))and (('|'in self.right.eva()) or ('==' in self.right.eva())):# if these signs exist in two sides, add () in self.left and right
            return f"{self.left}&({self.right})"
        else:# if not, dont need add ()
            return f"{self.left}&{self.right}"


class Or(sign):
    def eval(self,dic):# use recursion to return And execute and argue the Var(key) from next object class until class Var
        return self.left.eval(dic) or self.right.eval(dic)
    def eva(self):# return the Not execute as the type "|" and it would be the judging condition of __str__
        return f"{self.left}|{self.right}" 
    def __str__(self):# becuase the priority of And is third highest, so when it check == inslef.name.eva()(i defined it for judge in there)
        if('=='in self.left.eva()) and ('==' in self.right.eva()): # if these signs exist in two sides, add () in self.left and right 
            return f"({self.left})|({self.right})"
        elif ('=='in self.left.eva()) and not('==' in self.right.eva()):# if there has a lower prority sign in self.left and not in self.right, add () in self.left
            return f"({self.left})|{self.right}"
        elif not('=='in self.left.eva()) and ('==' in self.right.eva()):# if there has a lower prority sign in self.right and not in self.left, add () in self.right
            return f"{self.left}|({self.right})"
        else:# if not, dont need add bracket
            return f"{self.left}|{self.right}"


class Eq(sign):
    def eval(self,dic):# use recursion to return And execute and argue the Var(key) from next object class until class Var
        return self.left.eval(dic) == self.right.eval(dic)
    def eva(self):# because it is the lowest prority, done need to do more judges
        return f"{self.left}=={self.right}"
    def __str__(self):  
        return f"{self.left}=={self.right}"


e1 = Or(Var("x"),Not(Var("x")))
e2 = Eq(Var("x"),Not(Not(Var("x"))))
e3 = Eq(Not(And(Var("x"),Var("y"))),Or(Not(Var("x")),Not(Var("y"))))
e4 = Eq(Not(And(Var("x"),Var("y"))),And(Not(Var("x")),Not(Var("y"))))
e5 = Eq(Eq(Eq(Var("p"),Var("q")),Var("r")),Eq(Var("p"),Eq(Var("q"),Var("r"))))

print(e1)
print(e2)
print(e3)
print(e4)
print(e5)

print(And(Not(Var("p")),Var("q")))
print(Not(And(Var("p"),Var("q"))))
print(Or(And(Var("p"),Var("q")),Var("r")))
print(And(Var("p"),Or(Var("q"),Var("r"))))
print(Eq(Or(Var("p"),Var("q")),Var("r")))
print(Or(Var("p"),Eq(Var("q"),Var("r"))))

print (e2.eval({"x" : True}))
print (e3.eval({"x" : True, "y" : True}))
print (e4.eval({"x" : False, "y" : True}))

print(e1.make_tt())
print(e2.make_tt())
print(e3.make_tt())
print(e4.make_tt())
print(e5.make_tt())

print (And(Var("x"),And(Var("y"),Var("z"))))
print (And(And(Var("x"),Var("y")),Var("z")))
print("")

print (e1.isTauto())
print (e2.isTauto())
print (e3.isTauto())
print (e4.isTauto())
print (e5.isTauto())

#do a pause
input("Is okay?")
