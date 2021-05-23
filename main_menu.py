import tkinter
import  tkinter as tk
from tkinter import Menu, ttk,font,filedialog,messagebox,colorchooser
import os


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
##------------icons import and naming for edit menu --------------
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







main_win.config(menu= main_menu)
main_win.mainloop()