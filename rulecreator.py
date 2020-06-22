import sys
import cv2
import pickle
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import rulecreator_support
from tkinter.filedialog import askopenfilename, asksaveasfilename 

actions = []

def save_actions():
    f = asksaveasfilename(defaultextension=".pr")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    print(f)
    with open(f, 'wb') as file:
        pickle.dump(actions, file, protocol=pickle.HIGHEST_PROTOCOL)

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    rulecreator_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    rulecreator_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def delete_from_tree(self):
        for item in self.ActionTree.selection():
            id = self.ActionTree.item(item,"text")
            for curr, action in enumerate(actions, start=0):
                if action['id'] == id:
                    print(action["id"] == id)
                    actions.pop(curr)
            self.ActionTree.delete(item)
            print(actions)

    def open_file(self, click_pos='left'): 
        action_key = 'image_right_click' if click_pos == 'right' else 'image_left_click'
        file = askopenfilename(filetypes =[('Image Files', ['*.png', '*.jpg', '*.jpeg'])]) 
        if file is not None:   
            actions.append({
                'id' : self.id,
                'action' : action_key,
                'value' : cv2.imread(file, 0),
                'rgb_image' : cv2.imread(file)
            })      
            self.ActionTree.insert("",'end',text=self.id,values=(action_key, file))
            self.id += 1
            print(actions) 
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        self.id = 1
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("700x580+507+189")
        top.minsize(124, 1)
        top.maxsize(1924, 1061)
        top.resizable(0, 0)
        top.title("Patchio-Rule creator")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.style.configure('Treeview',  font="TkDefaultFont")
        self.ActionTree = ScrolledTreeView(top)
        self.ActionTree.place(relx=0.017, rely=0.022, relheight=0.588
                , relwidth=0.967)
        self.ActionTree.configure(columns=["rule","Action"])
        # build_treeview_support starting.
        self.ActionTree.heading("#0",text="Id")
        self.ActionTree.heading("#0",anchor="center")
        self.ActionTree.column("#0",width="30")
        self.ActionTree.column("#0",minwidth="20")
        self.ActionTree.column("#0",stretch="1")
        self.ActionTree.column("#0",anchor="w")
        self.ActionTree.heading("rule",text="Rule")
        self.ActionTree.heading("rule",anchor="center")
        self.ActionTree.column("rule",width="180")
        self.ActionTree.column("rule",minwidth="20")
        self.ActionTree.column("rule",stretch="1")
        self.ActionTree.column("rule",anchor="w")
        self.ActionTree.heading("Action",text="Action")
        self.ActionTree.heading("Action",anchor="center")
        self.ActionTree.column("Action",width="281")
        self.ActionTree.column("Action",minwidth="20")
        self.ActionTree.column("Action",stretch="1")
        self.ActionTree.column("Action",anchor="w")

        self.btn_add_keyboard = tk.Button(top,command=lambda:self.get_text_input(self.txt_keyboard_action, 'keyboard'))
        self.btn_add_keyboard.place(relx=0.429, rely=0.667, height=41, width=47)
        self.btn_add_keyboard.configure(activebackground="#ececec")
        self.btn_add_keyboard.configure(activeforeground="#000000")
        self.btn_add_keyboard.configure(background="#d9d9d9")
        self.btn_add_keyboard.configure(cursor="fleur")
        self.btn_add_keyboard.configure(disabledforeground="#a3a3a3")
        self.btn_add_keyboard.configure(foreground="#000000")
        self.btn_add_keyboard.configure(highlightbackground="#d9d9d9")
        self.btn_add_keyboard.configure(highlightcolor="black")
        self.btn_add_keyboard.configure(pady="0")
        self.btn_add_keyboard.configure(text='''Add''')

        self.txt_keyboard_action = tk.Text(top)
        self.txt_keyboard_action.place(relx=0.029, rely=0.667,height=42, relwidth=0.377)
        self.txt_keyboard_action.configure(background="white")
        self.txt_keyboard_action.configure(font="TkFixedFont")
        self.txt_keyboard_action.configure(foreground="#000000")
        self.txt_keyboard_action.configure(highlightbackground="#d9d9d9")
        self.txt_keyboard_action.configure(highlightcolor="black")
        self.txt_keyboard_action.configure(insertbackground="black")
        self.txt_keyboard_action.configure(selectbackground="#c4c4c4")
        self.txt_keyboard_action.configure(selectforeground="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=-0.014, rely=0.617, height=23, width=149)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Keyboard action''')

        self.tn_add_image_right_click = tk.Button(top, command=lambda:self.open_file('right'))
        self.tn_add_image_right_click.place(relx=0.529, rely=0.717, height=31
                , width=168)
        self.tn_add_image_right_click.configure(activebackground="#ececec")
        self.tn_add_image_right_click.configure(activeforeground="#000000")
        self.tn_add_image_right_click.configure(background="#d9d9d9")
        self.tn_add_image_right_click.configure(disabledforeground="#a3a3a3")
        self.tn_add_image_right_click.configure(foreground="#000000")
        self.tn_add_image_right_click.configure(highlightbackground="#d9d9d9")
        self.tn_add_image_right_click.configure(highlightcolor="black")
        self.tn_add_image_right_click.configure(pady="0")
        self.tn_add_image_right_click.configure(text='''Find image and right click''')

        self.btn_add_image_left_click = tk.Button(top, command=lambda:self.open_file('left'))
        self.btn_add_image_left_click.place(relx=0.529, rely=0.65, height=31
                , width=168)
        self.btn_add_image_left_click.configure(activebackground="#ececec")
        self.btn_add_image_left_click.configure(activeforeground="#000000")
        self.btn_add_image_left_click.configure(background="#d9d9d9")
        self.btn_add_image_left_click.configure(disabledforeground="#a3a3a3")
        self.btn_add_image_left_click.configure(foreground="#000000")
        self.btn_add_image_left_click.configure(highlightbackground="#d9d9d9")
        self.btn_add_image_left_click.configure(highlightcolor="black")
        self.btn_add_image_left_click.configure(pady="0")
        self.btn_add_image_left_click.configure(text='''Find image and left click''')

        self.btn_save = tk.Button(top, command=lambda:save_actions())
        self.btn_save.place(relx=0.786, rely=0.65, height=31, width=130)
        self.btn_save.configure(activebackground="#ececec")
        self.btn_save.configure(activeforeground="#000000")
        self.btn_save.configure(background="#d9d9d9")
        self.btn_save.configure(cursor="fleur")
        self.btn_save.configure(disabledforeground="#a3a3a3")
        self.btn_save.configure(foreground="#000000")
        self.btn_save.configure(highlightbackground="#d9d9d9")
        self.btn_save.configure(highlightcolor="black")
        self.btn_save.configure(pady="0")
        self.btn_save.configure(text='''Save''')

        self.btn_delete = tk.Button(top, command=lambda:self.delete_from_tree())
        self.btn_delete.place(relx=0.786, rely=0.717, height=31, width=130)
        self.btn_delete.configure(activebackground="#ececec")
        self.btn_delete.configure(activeforeground="#000000")
        self.btn_delete.configure(background="#d9d9d9")
        self.btn_delete.configure(disabledforeground="#a3a3a3")
        self.btn_delete.configure(foreground="#000000")
        self.btn_delete.configure(highlightbackground="#d9d9d9")
        self.btn_delete.configure(highlightcolor="black")
        self.btn_delete.configure(pady="0")
        self.btn_delete.configure(text='''Delete Action''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.029, rely=0.759, height=24, width=70)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Command''')

        self.txt_command = tk.Text(top)
        self.txt_command.place(relx=0.029, rely=0.793, relheight=0.05
                , relwidth=0.377)
        self.txt_command.configure(background="white")
        self.txt_command.configure(font="TkTextFont")
        self.txt_command.configure(foreground="black")
        self.txt_command.configure(highlightbackground="#d9d9d9")
        self.txt_command.configure(highlightcolor="black")
        self.txt_command.configure(insertbackground="black")
        self.txt_command.configure(selectbackground="#c4c4c4")
        self.txt_command.configure(selectforeground="black")
        self.txt_command.configure(wrap="word")

        self.btn_add_command = tk.Button(top,command=lambda:self.get_text_input(self.txt_command, 'command'))
        self.btn_add_command.place(relx=0.429, rely=0.793, height=31, width=102)
        self.btn_add_command.configure(activebackground="#ececec")
        self.btn_add_command.configure(activeforeground="#000000")
        self.btn_add_command.configure(background="#d9d9d9")
        self.btn_add_command.configure(disabledforeground="#a3a3a3")
        self.btn_add_command.configure(foreground="#000000")
        self.btn_add_command.configure(highlightbackground="#d9d9d9")
        self.btn_add_command.configure(highlightcolor="black")
        self.btn_add_command.configure(pady="0")
        self.btn_add_command.configure(text='''Add command''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.029, rely=0.845, height=24, width=98)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(cursor="fleur")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Wait action(s)''')

        self.txt_wait = tk.Text(top)
        self.txt_wait.place(relx=0.029, rely=0.879, relheight=0.05, relwidth=0.163)
        self.txt_wait.configure(background="white")
        self.txt_wait.configure(font="TkTextFont")
        self.txt_wait.configure(foreground="black")
        self.txt_wait.configure(highlightbackground="#d9d9d9")
        self.txt_wait.configure(highlightcolor="black")
        self.txt_wait.configure(insertbackground="black")
        self.txt_wait.configure(selectbackground="#c4c4c4")
        self.txt_wait.configure(selectforeground="black")
        self.txt_wait.configure(wrap="word")

        self.btn_add_wait_action = tk.Button(top,command=lambda:self.get_text_input(self.txt_wait, 'wait'))
        self.btn_add_wait_action.place(relx=0.2, rely=0.879, height=31, width=37)

        self.btn_add_wait_action.configure(activebackground="#ececec")
        self.btn_add_wait_action.configure(activeforeground="#000000")
        self.btn_add_wait_action.configure(background="#d9d9d9")
        self.btn_add_wait_action.configure(disabledforeground="#a3a3a3")
        self.btn_add_wait_action.configure(foreground="#000000")
        self.btn_add_wait_action.configure(highlightbackground="#d9d9d9")
        self.btn_add_wait_action.configure(highlightcolor="black")
        self.btn_add_wait_action.configure(pady="0")
        self.btn_add_wait_action.configure(text='''Add''')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.786, rely=0.966, height=24, width=147)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Patchio V.1.0 By IO18-2''')

    def get_text_input(self, component, action_key):
        result = component.get(1.0, tk.END+"-1c")        
        actions.append({
            'id' : self.id,
            'action' : action_key,
            'value' : result
        })      
        self.ActionTree.insert("",'end',text=self.id,values=(action_key, result))
        component.delete(1.0, tk.END+"-1c")
        self.id += 1
    @staticmethod
    def popup1(event, *args, **kwargs):
        Popupmenu1 = tk.Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.configure(activeborderwidth="1")
        Popupmenu1.configure(activeforeground="black")
        Popupmenu1.configure(background="#d9d9d9")
        Popupmenu1.configure(borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3")
        Popupmenu1.configure(font="{Segoe UI} 11")
        Popupmenu1.configure(foreground="black")
        Popupmenu1.post(event.x_root, event.y_root)

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





