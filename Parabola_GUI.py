from tkinter import *
root = Tk()
root.title("Data Extraction")
import sys
import os
import glob


#Class used for the beta decay code
class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.configure(bg='#21314D')

        self.create_widgets()
        self.grid()


        self.chemSymVar = StringVar()
        self.A = StringVar()
        self.T = StringVar()
        

    def create_widgets(self):
        title = Frame(self)
        decay = Frame(self)
        out = Frame(self)
        title.pack(side = TOP)
        decay.pack(side = BOTTOM)
        out.pack(side = BOTTOM)

        title.configure(bg='#21314D')
        decay.configure(bg='#21314D')
        out.configure(bg='#21314D')


        decayLabel = Label(decay, text = "Evaluated Beta Decay Information",font=("Helvetica",13,"bold"),bg='#21314D',fg='#92A2BD')
        decayLabel.grid(columnspan = 4,row = 0)

        ALabel = Label(decay, text = "Mass (ex. 60)",bg='#21314D',fg='#92A2BD',font=11)
        ALabel.grid(row = 1, column = 1, sticky = W)

        TLabel = Label(decay, text = "Temperature (K)", bg = '#21314D', fg = '#92A2BD', font = 11)
        TLabel.grid(row = 1, column = 2 , sticky = W)

        #Here I will set up all of the entry boxes for nucStruc
        #Same format

        self.AEntry = Entry(decay)
        self.AEntry.grid(row = 2, column = 1, sticky = W)
        self.TEntry = Entry(decay)
        self.TEntry.grid(row = 2, column = 2, sticky = W)



        #Setting up the submit buttons
        decaySubmit = Button(decay, text = "Submit", command = self.sendNucData,bg='#92A2BD',fg='#21314D',highlightbackground="#21314D",font=11)
        decaySubmit.grid(row = 5, column = 0)

        fullScreenSubmit = Button(decay, text = "Full Screen", command = self.fullScreenButton,bg='#92A2BD',fg='#21314D',highlightbackground="#21314D",font=11)
        fullScreenSubmit.grid(row = 5, column = 1)

        newChoiceSubmit = Button(decay, text = "Program Selection", command = self.newChoiceButton,bg='#92A2BD',fg='#21314D',highlightbackground="#21314D",font=11)
        newChoiceSubmit.grid(row = 5, column = 2)

        exitButtonSubmit = Button(decay, text = "Exit", command = self.exitButton,bg='#92A2BD',fg='#21314D',highlightbackground="#21314D",font=11)
        exitButtonSubmit.grid(row=5,column=3)


        #Setting up the graph output box including the calling of the most
        #recent graph to the GUI
        self.outGraph = Canvas(out,width = 700, height = 500)
        self.outGraph.grid(row = 0, column = 0, sticky = W+E+N+S)

        os.chdir("Output/gnuPlot")
        work_path = os.getcwd()
        if os.listdir(work_path) == []:
            print("Directory Empty")
        else:
            self.directory=os.getcwd()
            self.newest = max(glob.iglob(self.directory+"/*"),key=os.path.getctime)
            self.newest = self.newest.replace(os.getcwd()+"/","")
            if self.newest[-4:] != ".gif":
                try:
                    self.newest = "nuclearChart.gif"
                    self.photo = PhotoImage(file=self.newest)
                    self.outGraph.create_image(0,0,image=self.photo, anchor = "nw")
                except:
                    print("No Image to Display")
            elif os.listdir(work_path) == ["Ignore.txt"]:
                print("Directory Empty")
            else:
                try:
                    self.photo = PhotoImage(file=self.newest)
                    self.outGraph.create_image(0,0,image=self.photo, anchor = "nw")
                except:
                    print("No Image to Display")
        os.chdir("..")
        os.chdir("..")

        self.pictureSpot = Canvas(title,width = 620, height = 90)
        self.pictureSpot.grid(row = 0, column = 0) 
        self.photo2 = PhotoImage(file = "eilonglogo.gif")
        self.pictureSpot.create_image(0,0,image = self.photo2, anchor = "nw")
            

    #Defining the functions that make the submit buttons do things. 
    def sendNucData(self):
        """Send user input to nuclear structure sorting function"""
        self.A = self.AEntry.get()
        self.T = self.TEntry.get()
        root.destroy()#closes window

    def exitButton(self):
        self.exitcount = 1
        print("Thanks!")
        root.destroy()
        sys.exit()

    def fullScreenButton(self):
        os.chdir("Output/gnuPlot")
        directory = os.getcwd()
        newest = max(glob.iglob(directory+"/*"),key=os.path.getctime)
        newest = newest.replace(os.getcwd()+"/","")
        os.system("okular --presentation "+newest+" &")
        os.chdir("..")
        os.chdir("..")

    def newChoiceButton(self):
        self.chemSymVar = "Zn"
        self.A = 10
        self.spinVar = "0+"
        self.exitcount = 1
        root.destroy()
        os.system("python3 USE_THIS.py")
        sys.exit()

app = Application(root)
root.protocol("WM_DELETE_WINDOW",app.exitButton)
root.mainloop()

#Need to define a class for the variables output by the gui (the user inputs), to be used in the other scripts

class parabolaoutputs:
#These are the Nuclear Structure (ENSDF inputs) variables
    periodicTable=open("ElementList.txt",'r')
    Z = periodicTable.readline()
    Z = Z.strip()
    A=app.A
    J=""
    T=app.T

    ##These if statements either kill the program or input preset values if the
    ##user leaves a section blank.
    if A == '':
        print("YOU SUCK, FIGURE IT OUT")
        sys.exit()
    if T == '':
        T = 0

