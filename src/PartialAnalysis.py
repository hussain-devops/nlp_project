from src import *
from src import helpInfo

menu = Menu()



class PartialAnalysis():
    input2=''
    def getInput(self):
        print ('You are inside Partial Analysis class')
        menu.ShowPartialAnalysis()
        self.input2 = menu.getInput()
        return self.input2

    def validateInput(self,input2):
        if self.input2 == 'q':
            print 'Exit From Frame Work'
            exit()
        elif self.input2 == '1': 
            print ('Entered Input '+ self.input2) 
        elif self.input2 == '2':
            print ('Entered Input '+ self.input2)
        elif self.input2 == '3':
            print ('Entered Input '+ self.input2)
        elif self.input2 == '4':
            print ('Entered Input '+ self.input2)
        elif self.input2 == 'h':
            print ('Entered Input '+ self.input2)
            print helpInfo.help2
        else:
            print ('Please Enter Choice within the range')



# class PartialAnalysisMenu():
#     def
# partialAnalysis = PartialAnalysis()
# partialAnalysis.validateInput(input2)