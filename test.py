
##Klasse bilden für Bingospiel
## Was muss die Klasse können?
## Bingo-Prüfung
## Set-data


from multiprocessing import Value
from telnetlib import theNULL


class Bingo():
    __field=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    __checkfield=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

    def __validate_values(self,bingodata):
        print("...start validate_values")
        checklist = []
        testnumber = -1
        for collum in bingodata:
            for row in collum:
                
                checklist.append(int(row))
        print("...check")
        print(sorted(checklist))
        for value in sorted(checklist):
            
            if value > testnumber:
                testnumber = value
            else:
                print("Error: Same Values")
                return False
        return True
        
    def __validate_collums(self,bingodata):
        print("...Start validate_collums")
        for collum in bingodata:
            
            if len(collum) != 5:
                print("Error: False collum count!")
                return False
        print("Bingo collums ok")
        return True  

    def __validate_rows(self,bingodata):
        print("...Start validate_rows")
        #check rows
        if (len(bingodata)) == 5:
            print("Bingozeilen ok")
            return True
        else:
            print("Error: False row count!")
            return False

    def __init__(self,bingodata):
        print("...Start init class of Bingo")
        if self.__validate_rows(bingodata) and self.__validate_collums(bingodata) and self.__validate_values(bingodata):
            print("Bingo Syntax OK")
            self.__field=bingodata
        else:
            print("Error: Validateerror")

    def check_numbers(self,number):
        print("...start check number:",number)
        counter = 0
        for collum in self.__field:
            for row in collum:
                if number == row:
                    self.__checkfield[int(counter/5)][counter%5] = 1
                    print("correct Number!!!")
                    print(self.__checkfield)
                    self.check_bingo()
                    return True
                counter+=1
        print("False Number!")
        return False
        
    def check_bingo(self):
        print("...start check bingo")
        x=0
        y=0
        counter_collums = 0
        counter_rows = 0
        #check rows
        for x in range(5):
            for y in range(5):
                if self.__checkfield[x][y]==1:
                    counter_rows+=1
                if self.__checkfield[y][x]==1:
                    counter_collums+=1
                if counter_collums==5 or counter_rows==5:
                    print("!!!Bingo!!!")
                    return True
            counter_rows=0
            counter_collums=0
        #END

        print("NO BINGO!")
        return False


bingo1 = Bingo([[1,6,4,20,7],[16,9,8,19,50],[39,46,59,67,21],[48,23,5,34,45],[56,65,87,55,98]])
bingo1.check_numbers(20)
bingo1.check_numbers(19)
bingo1.check_numbers(67)
bingo1.check_numbers(34)
bingo1.check_numbers(1)
bingo1.check_numbers(6)
bingo1.check_numbers(4)
bingo1.check_numbers(10)
bingo1.check_numbers(7)

test=[]
with open("Text.txt") as f:
    for line in f:
        line = line.replace("  "," ")
        line = line.strip("\n ")
        line = line.split(" ")
        test.append(line)
        
        
print(test)

firstline = test[0]

print(firstline)
#manual readin
bingo2 = Bingo([test[2],test[3],test[4],test[5],test[6]])
