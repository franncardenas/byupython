import re
import string 
import tkinter as tk
from tkinter import *
from finalproject import Students
from tkinter import ttk 
from tkinter import messagebox

class window(Frame):

    students = Students()

    def __init__(self, master=None):
        super().__init__(master, width=680, height=260)
        self.master = master 
        self.pack()
        self.create_widgets()
        self.fill_data()
        self.enable_box("disabled")
        self.enable_button("normal")
        self.enable_savebutton("disabled")

    def num_charac_InText(self, input_string):
        # Using regex, look for a number in the string
        invalidcharacters= set(string.punctuation)
        if (re.search("[0-9]",input_string)) or any(char in invalidcharacters for char in input_string):
            return False
        # if no number is found, return False
        return True
    
    def check_empty(self, input_string) :
        if input_string == None:
            return 1     #your function where you want to jump
        return 2
    
    def enable_box(self,state):
        #allow them to write in the boxes
        self.boxFirstName.configure(state=state)
        self.boxLastName.configure(state=state)
        self.boxCountryBirth.configure(state=state)
        self.boxAge.configure(state=state)

    def enable_button(self,estado):
        #allow them to press the buttons 'new student' and 'delete student'.
        self.new_button.configure(state=estado)                
        self.delete_button.configure(state=estado)

    def enable_savebutton(self,estado):
        #enable them to press the 'save' and 'cancel' buttons
        self.save_button.configure(state=estado)                
        self.cancel_button.configure(state=estado)

    def clean_box(self):
        #Clean text boxes
        self.boxFirstName.delete(0, END)
        self.boxLastName.delete(0, END)
        self.boxCountryBirth.delete(0, END)
        self.boxAge.delete(0, END)

    def clean_grid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)

    def fill_data(self):
        data = self.students.query_allstudents()        
        for row in data:            
            self.grid.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4]))

    def new_button(self):
        self.enable_box("normal")
        self.enable_button("disabled")
        self.enable_savebutton("normal")
        self.clean_box()
        self.boxFirstName.focus()
        

    def delete_button(self):
        selected = self.grid.focus()                               
        key = self.grid.item(selected,'text')        
        if key == '':
            messagebox.showwarning("Delete", 'You must select an element.')            
        else:                           
            r = messagebox.askquestion("Delete", "Do you want to delete the selected record?")            
            if r == messagebox.YES:
                n = self.students.delete_student(key)
                if n == 1:
                    messagebox.showinfo("Delete", 'Item successfully removed.')
                    self.clean_grid()
                    self.fill_data()
                else:
                    messagebox.showwarning("Delete", 'It was not possible to eliminate the element.')

    def save_button(self):
        check1 = self.check_empty(self.boxFirstName.get())
        check2 = self.check_empty(self.boxLastName.get())
        check3 = self.check_empty(self.boxFirstName.get())
        check4 = self.check_empty(self.boxAge.get())
        if check1==2 or check2==2 or check3==2 or check4==2:
            box1 = self.num_charac_InText(self.boxFirstName.get())
            box2 = self.num_charac_InText(self.boxLastName.get())
            box3 = self.num_charac_InText(self.boxCountryBirth.get())

            if box1 == True and box2==True and box3==True :
                self.students.insert_student(self.boxFirstName.get(),self.boxLastName.get(),self.boxCountryBirth.get(),self.boxAge.get())
                self.clean_grid()
                self.fill_data()  
                self.enable_savebutton("disabled")      
                self.enable_button("normal")
                self.clean_box()
                self.enable_box("disabled")
            else:
                messagebox.showinfo("Save", 'Invalid data, try again')
                self.clean_box()
                self.enable_box("normal")
                self.enable_button("disabled")
        else : 
            messagebox.showinfo("Save", 'Empty Data, try again')
            self.clean_box()
            self.enable_box("normal")
            self.enable_button("disabled")


    def cancel_button(self):
        r = messagebox.askquestion("Calcel", "Are you sure you want to cancel the current operation?")
        if r == messagebox.YES:
            self.clean_box() 
            self.enable_savebutton("disabled")      
            self.enable_button("normal")
            self.enable_box("disabled")

    def create_widgets(self):

        #Create Frame 1
        frame = Frame(self, bg="#bfdaff")
        frame.place(x=0, y=0, width=100,height=259)
        self.new_button=Button(frame,text="New Student", command=self.new_button, bg="green", fg="white")
        self.new_button.place(x=5,y=60,width=85, height=40 )
        self.delete_button=Button(frame,text="Delete Student", command=self.delete_button, bg="red", fg="white")
        self.delete_button.place(x=5,y=110,width=85, height=40 )

        #Create Frame 2
        frame2 = Frame(self,bg="#d3dde3" )
        frame2.place(x=95,y=0,width=150, height=270)
        #Create label First Name
        lbl1 = Label(frame2,text="First Name : ")
        lbl1.place(x=10,y=5)      
        #Create an Entry (text box)
        self.boxFirstName=Entry(frame2)
        self.boxFirstName.place(x=10,y=25,width=130, height=20)
        #Create label Last Name
        lbl2 = Label(frame2,text="Last Name : ")
        lbl2.place(x=10,y=55)      
        #Create an Entry (text box)
        self.boxLastName=Entry(frame2)
        self.boxLastName.place(x=10,y=75,width=130, height=20)
        #Create label Country of Birth
        lbl3 = Label(frame2,text="Country of Birth : ")
        lbl3.place(x=10,y=105)      
        #Create an Entry (text box)
        self.boxCountryBirth=Entry(frame2)
        self.boxCountryBirth.place(x=10,y=125,width=130, height=20)
        #Create label Last Name
        lbl4 = Label(frame2,text="Age (1-99): ")
        lbl4.place(x=10,y=155)      
        #Create an Entry (text box)
        self.boxAge=IntEntry(frame2,lower_bound=1, upper_bound=99)
        self.boxAge.place(x=10,y=175,width=130, height=20)

        #Add save and cancel button
        self.save_button=Button(frame2,text="Save", command=self.save_button, bg="green", fg="white")
        self.save_button.place(x=10,y=210,width=60, height=30)
        self.cancel_button=Button(frame2,text="Cancel", command=self.cancel_button, bg="red", fg="white")
        self.cancel_button.place(x=80,y=210,width=60, height=30)

        #Add view of database 
        self.grid = ttk.Treeview(self, columns=("col1","col2","col3","col4"))
        #Add columns 
        self.grid.column("#0",width=35)
        self.grid.column("col1",width=70, anchor=CENTER)
        self.grid.column("col2",width=90, anchor=CENTER)
        self.grid.column("col3",width=90, anchor=CENTER)
        self.grid.column("col4",width=90, anchor=CENTER) 
        #Add names columns
        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="First Name", anchor=CENTER)
        self.grid.heading("col2", text="Last Name", anchor=CENTER)
        self.grid.heading("col3", text="Country of Birth", anchor=CENTER)
        self.grid.heading("col4", text="Age", anchor=CENTER)
        self.grid.place(x=247,y=0,width=420, height=259)


class _NumberEntry(Entry):
    _ERROR_STYLE = {"bg":"pink", "fg":"black"}


    def __init__(self, parent, datatype, dataname,
            lower_bound, upper_bound, default, kwargs):
        super().__init__(parent)

        assert type(self) != _NumberEntry, \
            "can't create a _NumberEntry object; " \
            "only children classes of _NumberEntry can be instantiated"
        assert isinstance(lower_bound, datatype), \
            f"lower_bound must be " + dataname
        assert isinstance(upper_bound, datatype), \
            f"upper_bound must be " + dataname
        assert lower_bound < upper_bound, \
            "lower_bound must be less than upper_bound"

        self.__datatype = datatype
        self.__dataname = dataname
        self.__lower_bound = lower_bound
        self.__upper_bound = upper_bound

        if default is not None:
            assert isinstance(default, datatype), \
                f"default must be " + dataname
            assert self._in_bounds(default), \
                "default must be between lower_bound and upper_bound"
            self.delete(0, tk.END)
            self.insert(0, str(default))

        self.__set_tk_args(kwargs)
        self.bind("<FocusIn>", _NumberEntry.__select_all)


    def __set_tk_args(self, kwargs):
        """Set the arguments that are used by tkinter."""
        if "justify" not in kwargs:
            kwargs["justify"] = "left"
        if "width" not in kwargs:
            kwargs["width"] = \
                max(len(str(self.__lower_bound)), len(str(self.__upper_bound)))
        kwargs["validate"] = "focusin"
        kwargs["validatecommand"] = \
                (self.register(self.__validate_all), "%V", "%s", "%P")
        self.config(**kwargs)
        self._original_style = {"bg":self["bg"], "fg":self["fg"]}


    # Each time a _NumberEntry gets the keyboard focus,
    # select all the text in that entry.
    @staticmethod
    def __select_all(event):
        """Select all the characters in the entry."""
        entry = event.widget
        entry.select_range(0, tk.END)
        entry.icursor(tk.END)


    @staticmethod
    def _contains_space(text):
        has_space = False
        for ch in text:
            has_space = ch.isspace()
            if has_space:
                break
        return has_space


    def __validate_all(self, reason, current_text, text_if_allowed):
        valid = False
        if reason == "key":
            valid = self._validate_key(current_text, text_if_allowed)
        elif reason == "focusin":
            valid = self.__focus_in(current_text)
        elif reason == "focusout":
            valid = self.__focus_out(current_text)
        return valid


    def __focus_in(self, current_text):
        self.config({"validate": "all"})
        return self.__validate_focus(current_text)

    def __focus_out(self, current_text):
        self.config({"validate": "focusin"})
        return self.__validate_focus(current_text)

    def __validate_focus(self, current_text):
        valid = False
        try:
            n = self._convert(current_text)
            valid = self._in_bounds(n)
        except ValueError:
            pass
        style = self._original_style if valid else _NumberEntry._ERROR_STYLE
        self.config(style)
        return valid


    def _in_bounds(self, n):
        return self.__lower_bound <= n <= self.__upper_bound


    def set(self, n):
        """Display a number for the user to see."""
        assert isinstance(n, self.__datatype), \
            "n must be " + self.__dataname
        assert self._in_bounds(n), \
            f"n must be between {self.__lower_bound} and {self.__upper_bound}"
        self.delete(0, tk.END)
        self.insert(0, str(n))


    def get(self):
        """Return the number that the user entered."""
        n = self._convert(super().get())
        if not self._in_bounds(n):
            raise ValueError("number must be between"
                f" {self.__lower_bound} and {self.__upper_bound}")
        return n


    def clear(self):
        self.config({"validate": "focusin"})
        self.config(self._original_style)
        self.delete(0, tk.END)


class IntEntry(_NumberEntry):
    """An Entry widget that accepts only integers between
    an optional lower bound and an optional upper bound.
    """
    def __init__(self, parent, *, lower_bound=-2**63,
            upper_bound=2**63 - 1, default=None, **kwargs):
        super().__init__(parent, int, "an integer",
                lower_bound, upper_bound, default, kwargs)

        self.__lower_entry = lower_bound if lower_bound <= 1 else 1
        self.__upper_entry = upper_bound if upper_bound >= -1 else -1
        self.__allow_negative = (lower_bound < 0)


    def _validate_key(self, current_text, text_if_allowed):
        allowed = valid = False
        try:
            if not _NumberEntry._contains_space(text_if_allowed):
                n = int(text_if_allowed)
                allowed = self.__lower_entry <= n <= self.__upper_entry
                # If text_if_allowed is allowed, we must allow it, and
                # we must check only text_if_allowed for validity.
                if allowed:
                    valid = self._in_bounds(n)
        except ValueError:
            allowed = (len(text_if_allowed) == 0 or
                    (self.__allow_negative and text_if_allowed == "-"))

        # If text_if_allowed is not allowed, we must not allow
        # it, and we must check only current_text for validity.
        if not allowed:
            try:
                n = int(current_text)
                valid = self._in_bounds(n)
            except ValueError:
                pass

        style = self._original_style if valid else _NumberEntry._ERROR_STYLE
        self.config(style)
        return allowed


    @staticmethod
    def _convert(text): return int(text)