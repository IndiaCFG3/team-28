import tkinter as tk 
import webbrowser

def callback(url):
    webbrowser.open_new(url)
 
  
root = tk.Tk() 
  
# specify size of window. 
root.geometry("600x300") 
subject_grades = [36,67,80]
subject = ["Mathematics","Science","Social Science"]
#finding the minimun grades
index = subject_grades.index(min(subject_grades))

# Create text widget and specify size. 
T = tk.Text(root, height = 30, width = 69) 
  
# Create label 
l = tk.Label(root, text = "Feedback") 
l.config(font =("Courier", 29)) 
  
Fact = "Grades were not upto to the mark for "+  subject[index]  +". Here are the Resources to progress further."

# Create button for next text. 
link1 = tk.Label(root, text="Link", fg="blue", cursor="hand2",)
link1.bind("<Button-1>", lambda e: callback("http://www.algebra4children.com/eigth-grade-math-worksheets.html"))
 

l.pack()
link1.pack()  
T.pack() 
  
# Insert The Fact. 
T.insert(tk.END, Fact) 
  
tk.mainloop() 