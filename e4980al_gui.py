#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Dec 15, 2017 07:58:04 PM
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import e4980al_gui_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    e4980al_gui_support.set_Tk_var()
    top = E4980AL_controller (root)
    e4980al_gui_support.init(root, top)
    root.mainloop()

w = None
def create_E4980AL_controller(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    e4980al_gui_support.set_Tk_var()
    top = E4980AL_controller (w)
    e4980al_gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_E4980AL_controller():
    global w
    w.destroy()
    w = None


class E4980AL_controller:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x424+657+205")
        top.title("E4980AL controller")
        top.configure(background="#d9d9d9")



        self.start_btn = Button(top)
        self.start_btn.place(relx=0.77, rely=0.05, height=43, width=116)
        self.start_btn.configure(activebackground="#d9d9d9")
        self.start_btn.configure(activeforeground="#000000")
        self.start_btn.configure(background="#d9d9d9")
        self.start_btn.configure(command=e4980al_gui_support.start_single_measure)
        self.start_btn.configure(disabledforeground="#a3a3a3")
        self.start_btn.configure(foreground="#000000")
        self.start_btn.configure(highlightbackground="#d9d9d9")
        self.start_btn.configure(highlightcolor="black")
        self.start_btn.configure(pady="0")
        self.start_btn.configure(text='''Start measure''')
        self.start_btn.configure(width=116)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.05, rely=0.24, height=26, width=56)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''voltage''')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.05, rely=0.14, height=26, width=76)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''frerquency''')

        self.meas_combo1 = ttk.Combobox(top)
        self.meas_combo1.place(relx=0.18, rely=0.05, relheight=0.06
                , relwidth=0.14)
        self.value_list = ['Cs','Cp','Ls','Lp','R-X',]
        self.meas_combo1.configure(values=self.value_list)
        READONLY = 'readonly'
        self.meas_combo1.configure(state=READONLY)
        self.meas_combo1.configure(textvariable=e4980al_gui_support.meas1)
        self.meas_combo1.configure(width=87)
        self.meas_combo1.configure(takefocus="")

        self.Label3 = Label(top)
        self.Label3.place(relx=0.05, rely=0.05, height=26, width=62)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''measure''')

        self.result_text = Text(top)
        self.result_text.place(relx=0.67, rely=0.17, relheight=0.17
                , relwidth=0.29)
        self.result_text.configure(background="white")
        self.result_text.configure(font="TkTextFont")
        self.result_text.configure(foreground="black")
        self.result_text.configure(highlightbackground="#d9d9d9")
        self.result_text.configure(highlightcolor="black")
        self.result_text.configure(insertbackground="black")
        self.result_text.configure(selectbackground="#c4c4c4")
        self.result_text.configure(selectforeground="black")
        self.result_text.configure(width=174)
        self.result_text.configure(wrap=WORD)

        self.meas_combo2 = ttk.Combobox(top)
        self.meas_combo2.place(relx=0.38, rely=0.05, relheight=0.06
                , relwidth=0.14)
        self.value_list = ['R','D','Q','G',]
        self.meas_combo2.configure(values=self.value_list)
        READONLY = 'readonly'
        self.meas_combo2.configure(state=READONLY)
        self.meas_combo2.configure(textvariable=e4980al_gui_support.meas2)
        self.meas_combo2.configure(width=87)
        self.meas_combo2.configure(takefocus="")

        self.req_entry = Spinbox(top, from_=20.0, to=1000000.0)
        self.req_entry.place(relx=0.18, rely=0.14, relheight=0.06, relwidth=0.16)

        self.req_entry.configure(activebackground="#f9f9f9")
        self.req_entry.configure(background="white")
        self.req_entry.configure(buttonbackground="#d9d9d9")
        self.req_entry.configure(disabledforeground="#a3a3a3")
        self.req_entry.configure(foreground="black")
        self.req_entry.configure(from_="20.0")
        self.req_entry.configure(highlightbackground="black")
        self.req_entry.configure(highlightcolor="black")
        self.req_entry.configure(insertbackground="black")
        self.req_entry.configure(justify=RIGHT)
        self.req_entry.configure(selectbackground="#c4c4c4")
        self.req_entry.configure(selectforeground="black")
        self.req_entry.configure(takefocus="0")
        self.req_entry.configure(textvariable=e4980al_gui_support.freq)
        self.req_entry.configure(to="1000000.0")
        self.req_entry.configure(width=96)

        self.voltage_entry = Spinbox(top, from_=0.0, to=2.0)
        self.voltage_entry.place(relx=0.18, rely=0.24, relheight=0.06
                , relwidth=0.16)
        self.voltage_entry.configure(activebackground="#f9f9f9")
        self.voltage_entry.configure(background="white")
        self.voltage_entry.configure(buttonbackground="#d9d9d9")
        self.voltage_entry.configure(disabledforeground="#a3a3a3")
        self.voltage_entry.configure(foreground="black")
        self.voltage_entry.configure(highlightbackground="black")
        self.voltage_entry.configure(highlightcolor="black")
        self.voltage_entry.configure(increment="0.1")
        self.voltage_entry.configure(insertbackground="black")
        self.voltage_entry.configure(justify=RIGHT)
        self.voltage_entry.configure(selectbackground="#c4c4c4")
        self.voltage_entry.configure(selectforeground="black")
        self.voltage_entry.configure(takefocus="0")
        self.voltage_entry.configure(textvariable=e4980al_gui_support.voltage)
        self.voltage_entry.configure(to="2.0")
        self.voltage_entry.configure(width=96)

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.file = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.file,
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="File")
        self.file.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                accelerator="Ctrl +Q",
                background="#d9d9d9",
                command=e4980al_gui_support.command_quit,
                font="TkMenuFont",
                foreground="#000000",
                label="Quit")
        self.menubar.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                accelerator="Ctrl + S",
                background="#d9d9d9",
                command=e4980al_gui_support.command_save,
                font="TkMenuFont",
                foreground="#000000",
                label="Save")


        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.02, rely=0.38, relheight=0.6
                , relwidth=0.97)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''List mode''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(width=580)

        self.start_list_meas_btn = Button(self.Labelframe1)
        self.start_list_meas_btn.place(relx=0.38, rely=0.59, height=43
                , width=113)
        self.start_list_meas_btn.configure(activebackground="#d9d9d9")
        self.start_list_meas_btn.configure(activeforeground="#000000")
        self.start_list_meas_btn.configure(background="#d9d9d9")
        self.start_list_meas_btn.configure(command=e4980al_gui_support.start_list_measure)
        self.start_list_meas_btn.configure(disabledforeground="#a3a3a3")
        self.start_list_meas_btn.configure(foreground="#000000")
        self.start_list_meas_btn.configure(highlightbackground="#d9d9d9")
        self.start_list_meas_btn.configure(highlightcolor="black")
        self.start_list_meas_btn.configure(pady="0")
        self.start_list_meas_btn.configure(takefocus="0")
        self.start_list_meas_btn.configure(text='''Start measure''')
        self.start_list_meas_btn.configure(width=113)

        self.list_from_entry = Spinbox(self.Labelframe1, from_=20.0, to=1000000.0)
        self.list_from_entry.place(relx=0.12, rely=0.16, relheight=0.09
                , relwidth=0.15)
        self.list_from_entry.configure(activebackground="#f9f9f9")
        self.list_from_entry.configure(background="white")
        self.list_from_entry.configure(buttonbackground="#d9d9d9")
        self.list_from_entry.configure(disabledforeground="#a3a3a3")
        self.list_from_entry.configure(foreground="black")
        self.list_from_entry.configure(from_="20.0")
        self.list_from_entry.configure(highlightbackground="black")
        self.list_from_entry.configure(highlightcolor="black")
        self.list_from_entry.configure(insertbackground="black")
        self.list_from_entry.configure(justify=RIGHT)
        self.list_from_entry.configure(selectbackground="#c4c4c4")
        self.list_from_entry.configure(selectforeground="black")
        self.list_from_entry.configure(takefocus="0")
        self.list_from_entry.configure(textvariable=e4980al_gui_support.list_sweep_from)
        self.list_from_entry.configure(to="1000000.0")
        self.list_from_entry.configure(width=86)

        self.list_to_entry = Spinbox(self.Labelframe1, from_=20.0, to=1000000.0)
        self.list_to_entry.place(relx=0.36, rely=0.16, relheight=0.09
                , relwidth=0.17)
        self.list_to_entry.configure(activebackground="#f9f9f9")
        self.list_to_entry.configure(background="white")
        self.list_to_entry.configure(buttonbackground="#d9d9d9")
        self.list_to_entry.configure(disabledforeground="#a3a3a3")
        self.list_to_entry.configure(foreground="black")
        self.list_to_entry.configure(from_="20.0")
        self.list_to_entry.configure(highlightbackground="black")
        self.list_to_entry.configure(highlightcolor="black")
        self.list_to_entry.configure(insertbackground="black")
        self.list_to_entry.configure(justify=RIGHT)
        self.list_to_entry.configure(selectbackground="#c4c4c4")
        self.list_to_entry.configure(selectforeground="black")
        self.list_to_entry.configure(takefocus="0")
        self.list_to_entry.configure(textvariable=e4980al_gui_support.list_sweep_to)
        self.list_to_entry.configure(to="1000000.0")
        self.list_to_entry.configure(width=96)

        self.Label4 = Label(self.Labelframe1)
        self.Label4.place(relx=0.03, rely=0.16, height=26, width=40)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''From''')

        self.Label5 = Label(self.Labelframe1)
        self.Label5.place(relx=0.31, rely=0.16, height=26, width=23)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''To''')

        self.list_gen_combo = ttk.Combobox(self.Labelframe1)
        self.list_gen_combo.place(relx=0.59, rely=0.16, relheight=0.1
                , relwidth=0.27)
        self.value_list = ['logarithmic','linear','manual',]
        self.list_gen_combo.configure(values=self.value_list)
        self.list_gen_combo.configure(textvariable=e4980al_gui_support.list_gen_mode)
        self.list_gen_combo.configure(width=157)
        self.list_gen_combo.configure(takefocus="")

        self.list_numpoints_entry = Spinbox(self.Labelframe1, from_=1.0, to=201.0)
        self.list_numpoints_entry.place(relx=0.21, rely=0.31, relheight=0.09
                , relwidth=0.1)
        self.list_numpoints_entry.configure(activebackground="#f9f9f9")
        self.list_numpoints_entry.configure(background="white")
        self.list_numpoints_entry.configure(buttonbackground="#d9d9d9")
        self.list_numpoints_entry.configure(disabledforeground="#a3a3a3")
        self.list_numpoints_entry.configure(foreground="black")
        self.list_numpoints_entry.configure(from_="1.0")
        self.list_numpoints_entry.configure(highlightbackground="black")
        self.list_numpoints_entry.configure(highlightcolor="black")
        self.list_numpoints_entry.configure(insertbackground="black")
        self.list_numpoints_entry.configure(justify=RIGHT)
        self.list_numpoints_entry.configure(selectbackground="#c4c4c4")
        self.list_numpoints_entry.configure(selectforeground="black")
        self.list_numpoints_entry.configure(takefocus="0")
        self.list_numpoints_entry.configure(textvariable=e4980al_gui_support.num_of_points)
        self.list_numpoints_entry.configure(to="201.0")
        self.list_numpoints_entry.configure(width=56)

        self.Label6 = Label(self.Labelframe1)
        self.Label6.place(relx=0.05, rely=0.31, height=26, width=78)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''# of points''')

        self.list_sweep_progress = ttk.Progressbar(self.Labelframe1)
        self.list_sweep_progress.place(relx=0.05, rely=0.82, relwidth=0.88
                , relheight=0.0, height=22)
        self.list_sweep_progress.configure(length="510")
        self.list_sweep_progress.configure(variable=e4980al_gui_support.list_progressbar_var)

        self.list_gen_combo.current(0)
        self.meas_combo1.current(0)
        self.meas_combo2.current(0)
        e4980al_gui_support.voltage.set(1.0)
        e4980al_gui_support.freq.set(100000)
        e4980al_gui_support.list_sweep_from.set(20)
        e4980al_gui_support.list_sweep_to.set(1000000)
        e4980al_gui_support.num_of_points.set(201)

if __name__ == '__main__':
    vp_start_gui()


