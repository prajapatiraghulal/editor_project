import tkinter
import  tkinter as tk
from tkinter import Menu, Scrollbar, StringVar, ttk,font,filedialog,messagebox,colorchooser
import os
from tkinter.constants import FALSE, TRUE


main_win = tkinter.Tk()         #main software screen window
main_win.geometry('1200x800')
main_win.title('Smart Editor')



#----------------main_monu body------------------



main_menu = tk.Menu()   #if something misbehaves just remove arg in this line

#----------file menu-------------------
##------------icons import and naming for file menu --------------
new_icon= tk.PhotoImage(file='icons/new.png')
open_icon= tk.PhotoImage(file='icons/open.png')
save_icon= tk.PhotoImage(file='icons/save.png')
save_as_icon= tk.PhotoImage(file='icons/save_as.png')
exit_icon= tk.PhotoImage(file='icons/exit.png')



file_menu = tk.Menu(main_menu, tearoff=False)
file_menu.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N')    #tk.LEFT for assigning new icon left of label, accelerator for shortcutkey
file_menu.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O')    #tk.LEFT for assigning new icon left of label, accelerator for shortcutkey
file_menu.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S')    #tk.LEFT for assigning new icon left of label, accelerator for shortcutkey
file_menu.add_command(label='Save As',image=save_as_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+S')    #tk.LEFT for assigning new icon left of label, accelerator for shortcutkey
file_menu.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+Q')    #tk.LEFT for assigning new icon left of label, accelerator for shortcutkey

#-------------edit menu-------------------------------------------
##------------icons import and naming for edit
#  menu --------------
copy_icon= tk.PhotoImage(file='icons/copy.png')
cut_icon= tk.PhotoImage(file='icons/cut.png')
paste_icon= tk.PhotoImage(file='icons/paste.png')
clear_all_icon= tk.PhotoImage(file='icons/clear_all.png')
find_icon= tk.PhotoImage(file='icons/find.png')


edit_menu = tk.Menu(main_menu,tearoff=False)
edit_menu.add_command(label='Find',image= find_icon,compound=tk.LEFT,accelerator='Ctrl+F')
edit_menu.add_command(label='Copy',image= copy_icon,compound=tk.LEFT,accelerator='Ctrl+C')
edit_menu.add_command(label='Cut',image= cut_icon,compound=tk.LEFT,accelerator='Ctrl+X')
edit_menu.add_command(label='Paste',image= paste_icon,compound=tk.LEFT,accelerator='Ctrl+V')
edit_menu.add_command(label='Clear All',image= clear_all_icon,compound=tk.LEFT,accelerator='Ctrl+Shift+d')

#--------------view menu------------------------------------------
##-----------icon import and naming for view menu----------------
tool_bar_icon=tk.PhotoImage(file='icons/tool_bar.png')
status_bar_icon=tk.PhotoImage(file='icons/status_bar.png')


view_menu = tk.Menu(main_menu, tearoff=False)
view_menu.add_checkbutton(label='Tool Bar',image=tool_bar_icon,compound=tk.LEFT)
view_menu.add_checkbutton(label='Status Bar',image=status_bar_icon,compound=tk.LEFT)


#---------------color theme menu--------------------------------------
##--------------icon import and naming for color theme menu-----------
light_default_icon=tk.PhotoImage(file='icons/light_default.png')
light_plus_icon=tk.PhotoImage(file='icons/light_plus.png')
dark_icon=tk.PhotoImage(file='icons/dark.png')
red_icon=tk.PhotoImage(file='icons/red.png')
monokai_icon=tk.PhotoImage(file='icons/monokai.png')
night_blue_icon=tk.PhotoImage(file='icons/night_blue.png')


color_theme_menu = tk.Menu(main_menu, tearoff=False)

#below two data structure should be in same order or putting element 
color_theme_icons=(light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)
color_theme_dict={
    'Light Default':('#000000','#ffffff'),
    'Light Plus':('#020202','#fdfdfd'),
    'Dark':('#f3f3f3','#040404'),
    'Red':('#001111','#fc0111'),
    'Monokai':('#022f11','#cccccc'),
    'Night Blue':('#ff0809','#0f1fff')
}


color_theme_var = tk.StringVar()
for count,i in enumerate(color_theme_dict):
    color_theme_menu.add_radiobutton(label=i,image=color_theme_icons[count],compound=tk.LEFT, variable=color_theme_var)


#cascade drop down option while clicking on menu option 
main_menu.add_cascade(label='File',menu=file_menu)
main_menu.add_cascade(label='Edit',menu=edit_menu)
main_menu.add_cascade(label='View',menu=view_menu)
main_menu.add_cascade(label='Color Theme',menu=color_theme_menu)

#------------------main menu created --------------------


####----------------####----toolbar -------####--------------------------------------------------
toolbar = ttk.Label(main_win)
toolbar.pack(side=tk.TOP,fill=tk.X)



###------------font seslection combobox -------------------
current_font_family= 'Arial'
font_availabe = font.families()    #this is will give tuple of available fonts in tkinter 
font_family_selected = tk.StringVar()
font_combobox= ttk.Combobox(toolbar,width=30,textvariable=font_family_selected, state='readonly')
font_combobox['values']= font_availabe
font_combobox.grid(row=0,column=0,padx=5)
font_combobox.current(font_availabe.index('Arial'))

def change_font_family(main_win):
    global current_font_family
    current_font_family=font_family_selected.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_combobox.bind('<<ComboboxSelected>>',change_font_family)

###-----------font size combobox ----------------------------

current_font_size = 12
font_size_available = tuple(range(8,80,2))
font_size_selected = tk.IntVar()
font_size_combobox = ttk.Combobox(toolbar, width=15,textvariable=font_size_selected, state='readonly')
font_size_combobox['values']= font_size_available
font_size_combobox.current(font_size_available.index(current_font_size))
font_size_combobox.grid(row=0,column=1,padx=5)

def change_font_size(main_win):
    global current_font_size
    current_font_size= font_size_selected.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_size_combobox.bind('<<ComboboxSelected>>',change_font_size)


###-----------font bold button------------------------------
font_bold_icon = tk.PhotoImage(file='icons/bold.png')

font_bold_btn = ttk.Button(toolbar, image=font_bold_icon)
font_bold_btn.grid(row=0,column=2,padx=5)

def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] =='normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

font_bold_btn.configure(command=change_bold)


###----------font italic button--------------------
font_italic_icon = tk.PhotoImage(file='icons/italic.png')
font_italic_btn= ttk.Button(toolbar,image=font_italic_icon)
font_italic_btn.grid(row=0,column=3,padx=5)

def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='italic':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
    elif text_property.actual()['slant']=='roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))

font_italic_btn.configure(command=change_italic)




###---------font underline button--------------------
font_underline_icon = tk.PhotoImage(file='icons/underline.png')
font_underline_btn = ttk.Button(toolbar, image=font_underline_icon)
font_underline_btn.grid(row=0,column=4,padx=5)

def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']==TRUE:
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
    elif text_property.actual()['underline']==FALSE:
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))

font_underline_btn.configure(command=change_underline)



###---------font color button--------------------------
font_color_icon = tk.PhotoImage(file='icons/font_color.png')
font_color_btn = ttk.Button(toolbar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)

###---------font align left button--------------------
font_align_left_icon = tk.PhotoImage(file='icons/align_left.png')
font_align_left_btn = ttk.Button(toolbar,image=font_align_left_icon)
font_align_left_btn.grid(row=0,column=6,padx=5)

###-----------font align center button------------------------------
font_align_center_icon = tk.PhotoImage(file='icons/align_center.png')
font_align_center_btn = ttk.Button(toolbar,image=font_align_center_icon)
font_align_center_btn.grid(row=0,column=7,padx=5)
###-----------font align right button----------------------------------
font_align_right_icon = tk.PhotoImage(file='icons/align_right.png')
font_align_right_btn = ttk.Button(toolbar,image=font_align_right_icon)
font_align_right_btn.grid(row=0,column=8,padx=5)

###################----------------toolbar finish---------------------#########################3

#--------------------------------------text editor+ scrollbar -----------------------------------------#

text_editor = tk.Text(main_win)
text_editor.config(wrap='word',relief=tk.FLAT)
scrollbar= tk.Scrollbar(main_win)
text_editor.focus_set()
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)

scrollbar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scrollbar.set)


#-------------------text + toolbar finish ----------------------------------------------------------

##------------------status bar ---------------------------------------------------
status_bar = ttk.Label(main_win, text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

##-----------------status bar finish-------------------------------------------





main_win.config(menu= main_menu)
main_win.mainloop()