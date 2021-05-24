import tkinter
import  tkinter as tk
from tkinter import Menu, Scrollbar, StringVar, ttk,font,filedialog,messagebox,colorchooser
import os
from tkinter.constants import FALSE, INSERT, TRUE


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

#variables related to file --------------------
url= ''
#variable finish------------------------------
#new functionality------------------------------------
def new_file_func(event=None):
    global url
    url=''
    text_editor.delete(1.0,'end')
    main_win.title(os.path.basename(url).split('.')[0])
    
file_menu.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N',command=new_file_func)    #tk.LEFT for assigning new icon left of label, accelerator for shortcutkey
#new functionality finish------------------------------------

#open functionality-----------------------------------------
def open_file_func(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=url, title='Select File', filetypes=(('Text File','*.txt'),('Other File','*.*')))
    try:
        with open(url,'r') as f:
            text_editor.delete(1.0,'end')
            text_editor.insert(1.0,f.read())
    except FileNotFoundError:
        return
    except:
        return
    main_win.title(os.path.basename(url).split('.')[0])

file_menu.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O',command=open_file_func)    #tk.LEFT for assigning new icon left of label, accelerator for shortcutkey

#save functionality------------------------------------------------
def save_file_func(event=None):
    global url
    text_content = str(text_editor.get(1.0,'end'))
    try:
        if url:
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(text_content)
                
        else:
            file= filedialog.asksaveasfile(mode='w',initialdir=url,title='Save File',defaultextension='.txt',filetypes=(('Text File','*.txt'),('Other File,''*.*')))
            file.write(text_content)
            url= file.name
            main_win.title(os.path.basename(url).split('.')[0])
            url.close()
    except FileNotFoundError:
        pass
    except:
        pass

    
file_menu.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S',command=save_file_func)    #tk.LEFT for assigning new icon left of label, accelerator for shortcutkey

#save functionality finish---------------------------------------------

#save_as functionality ------------------------------------------------
def save_as_file_func(event=None):
    global url
    text_content = str(text_editor.get(1.0,'end'))
    try:
        file = filedialog.asksaveasfile(mode='w', initialdir=url, title='Save As',defaultextension='.txt',filetype=(('Text File','*.txt'),('Other File','*.*')))
        file.write(text_content)
        url= file.name
        main_win.title(os.path.basename(url).split('.')[0])
    except FileNotFoundError:
        pass
    except:
        pass

file_menu.add_command(label='Save As',image=save_as_icon,compound=tk.LEFT,accelerator='Ctrl+z',command=save_as_file_func)    #tk.LEFT for assigning new icon left of label, accelerator for shortcutkey

#save_as functionality finish-----------------------------------------------

#exit functionality --------------------------------------------------------
def exit_file_func(event=None):
    global url
    global text_change
    if text_change:
        option_selected = messagebox.askyesnocancel(title='Warning',message='Do you want to save ?!')
        if option_selected==True:
            save_file_func()
            main_win.destroy()
        elif option_selected==False:
            main_win.destroy()
        else:
            pass

file_menu.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+Q',command=exit_file_func)    #tk.LEFT for assigning new icon left of label, accelerator for shortcutkey

#exit functionality finish-------------------------------------------------

#-------------edit menu-------------------------------------------
##------------icons import and naming for edit
#  menu --------------
copy_icon= tk.PhotoImage(file='icons/copy.png')
cut_icon= tk.PhotoImage(file='icons/cut.png')
paste_icon= tk.PhotoImage(file='icons/paste.png')
clear_all_icon= tk.PhotoImage(file='icons/clear_all.png')
find_icon= tk.PhotoImage(file='icons/find.png')


edit_menu = tk.Menu(main_menu,tearoff=False)
#--------find menu functionality -------------------------------

def find_replace_text_func(event=None):

    def find_text_func(event=None):
        text_to_be_find = str(find_text_entry.get()).lower()
        editors_text = str(text_editor.get(1.0,'end')).lower().split('\n')
        len_finding = len(text_to_be_find)
    
        text_editor.tag_remove('match',1.0,'end')
        text_editor.tag_config("match",background='yellow', foreground='magenta')
        
        
        for j,line in enumerate(editors_text):
            len_editor_text= len(line)
            i=0
            while i<=(len_editor_text-len_finding):
                if(text_to_be_find[0]==line[i]):
                    if(text_to_be_find==line[i:i+len_finding]):
                        text_editor.tag_add('match',f'{j+1}.{i}',f'{j+1}.{i+len_finding}')
                        i+=len_finding
                    else:
                        i+=1
                else:
                    i+=1
        


    def replace_text_func(event=None):
        text_to_be_find = str(find_text_entry.get()).lower()
        text_to_place = str(replace_text_entry.get())
        editors_text = str(text_editor.get(1.0,'end')).lower().split('\n')
        len_finding = len(text_to_be_find)
        len_replacing = len(text_to_place)
    
        text_editor.tag_remove('match',1.0,'end')
        text_editor.tag_remove('replace',1.0,'end')

        text_editor.tag_config("replace",background='orange', foreground='blue')
        
        
        for j,line in enumerate(editors_text):
            len_editor_text= len(line)
            i=0
            while i<=(len_editor_text-len_finding):
                if(text_to_be_find[0]==line[i]):
                    if(text_to_be_find==line[i:i+len_finding]):
                        text_editor.delete(f'{j+1}.{i}',f'{j+1}.{i+len_finding}')
                        text_editor.insert(f'{j+1}.{i}',text_to_place)
                        text_editor.tag_add('replace',f'{j+1}.{i}',f'{j+1}.{i+len_replacing}')
                        i+=len_finding
                    else:
                        i+=1
                else:
                    i+=1


    popup_dialogue = tk.Toplevel()
    popup_dialogue.geometry('300x200+100+50')
    popup_dialogue.title('Find and Replace')
    popup_dialogue.resizable(False,False)

    #fram inside popup dialogue
    frame_in_popup = ttk.Label(popup_dialogue)
    frame_in_popup.pack(pady=50)

    #label for find and replace inside frame frame_in_popup
    find_text_label = ttk.Label(frame_in_popup,text='Enter Word:')
    find_text_label.grid(row=0,column=0,padx=4,pady=4)
    replace_text_label= ttk.Label(frame_in_popup,text='Replace With:')
    replace_text_label.grid(row=1,column=0,padx=4,pady=4)

    #entry box for find and replace inside frmae frame_in_popup
    find_text_entry = ttk.Entry(frame_in_popup,width=30)
    find_text_entry.grid(row=0,column=1,padx=4,pady=4)
    find_text_entry.focus_set()
    replace_text_entry = ttk.Entry(frame_in_popup,width=30)
    replace_text_entry.grid(row=1,column=1,padx=4,pady=4)

    #submit button for find replace-------------
    find_text_btn= ttk.Button(frame_in_popup,text='Find',command=find_text_func)
    find_text_btn.grid(row=2,column=0,padx=8,pady=8)
    replace_text_btn= ttk.Button(frame_in_popup,text='Replace',command=replace_text_func)
    replace_text_btn.grid(row=2,column=1,padx=0,pady=8)

    popup_dialogue.mainloop()
    
  
edit_menu.add_command(label='Find',image= find_icon,compound=tk.LEFT,accelerator='Ctrl+F',command=find_replace_text_func)

##-----------------------find menu finish----------------------------------------------------


##-------------copy, cut, paste, clear_all all menu at a place ------------------------------
edit_menu.add_command(label='Copy',image= copy_icon,compound=tk.LEFT,accelerator='Ctrl+C',command=lambda:text_editor.event_generate('<Control c>'))
edit_menu.add_command(label='Cut',image= cut_icon,compound=tk.LEFT,accelerator='Ctrl+X',command=lambda:text_editor.event_generate('<Control x>'))
edit_menu.add_command(label='Paste',image= paste_icon,compound=tk.LEFT,accelerator='Ctrl+V',command=lambda:text_editor.event_generate('<Control v>'))
edit_menu.add_command(label='Clear All',image= clear_all_icon,compound=tk.LEFT,accelerator='Ctrl+Shift+d',command=lambda:text_editor.delete(1.0,'end'))

## --------------copy, cut , paste , clear_all all menu finish--------------------------------

###----------------edit menu finish-----------------------------------------------------------



#--------------view menu------------------------------------------
##-----------icon import and naming for view menu----------------
tool_bar_icon=tk.PhotoImage(file='icons/tool_bar.png')
status_bar_icon=tk.PhotoImage(file='icons/status_bar.png')


view_menu = tk.Menu(main_menu, tearoff=False)

show_toolbar= tk.BooleanVar()
show_toolbar.set(True)
show_statusbar= tk.BooleanVar()
show_statusbar.set(True)

def hide_toolbar_func(event=None):
    global show_toolbar
    if show_toolbar:
        toolbar.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        toolbar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill= tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar=True



def hide_statusbar_func():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar=True


view_menu.add_checkbutton(label='Tool Bar',onvalue=True,offvalue=False,variable=show_toolbar,image=tool_bar_icon,compound=tk.LEFT,command=hide_toolbar_func)
view_menu.add_checkbutton(label='Status Bar',onvalue=True,offvalue=False,variable=show_statusbar,image=status_bar_icon,compound=tk.LEFT,command=hide_statusbar_func)


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
    'Light Plus':('#020202','#F4F6F6'),
    'Dark':('#f3f3f3','#566573'),
    'Red':('#001111','#EC7063'),
    'Monokai':('#000000','#FAD7A0'),
    'Night Blue':('#111111','#2E86C1')
}

#----------change theme functionality--------------------------------
def change_theme_func():
    theme_selected = color_theme_var.get()
    color_tuple = color_theme_dict.get(theme_selected)
    fg_color,bg_color = color_tuple
    text_editor.config(fg=fg_color,background=bg_color)
    

color_theme_var = tk.StringVar()
for count,i in enumerate(color_theme_dict):
    color_theme_menu.add_radiobutton(label=i,image=color_theme_icons[count],compound=tk.LEFT, variable=color_theme_var,command=change_theme_func)


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

def change_font_color():
    asked_font_color = colorchooser.askcolor()      #this method returns chosen color by user in rgb and hex value at index 0and 1
    text_editor.configure(fg=asked_font_color[1]) 

font_color_btn.configure(command=change_font_color) 


###---------font align left button--------------------
font_align_left_icon = tk.PhotoImage(file='icons/align_left.png')
font_align_left_btn = ttk.Button(toolbar,image=font_align_left_icon)
font_align_left_btn.grid(row=0,column=6,padx=5)


def change_font_align_left():
    text_content = text_editor.get(1.0,'end-1c')   #with get all text written in editor and store in variable
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,'end')
    text_editor.insert(tk.INSERT,text_content,'left')
font_align_left_btn.configure(command=change_font_align_left)


###-----------font align center button------------------------------
font_align_center_icon = tk.PhotoImage(file='icons/align_center.png')
font_align_center_btn = ttk.Button(toolbar,image=font_align_center_icon)
font_align_center_btn.grid(row=0,column=7,padx=5)


def change_font_align_center():
    text_content = text_editor.get(1.0,'end-1c')   #with get all text written in editor and store in variable
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,'end')
    text_editor.insert(tk.INSERT,text_content,'center')
font_align_center_btn.configure(command=change_font_align_center)

###-----------font align right button----------------------------------
font_align_right_icon = tk.PhotoImage(file='icons/align_right.png')
font_align_right_btn = ttk.Button(toolbar,image=font_align_right_icon)
font_align_right_btn.grid(row=0,column=8,padx=5)



def change_font_align_right():
    text_content = text_editor.get(1.0,'end-1c')   #with get all text written in editor and store in variable
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,'end')
    text_editor.insert(tk.INSERT,text_content,'right')
font_align_right_btn.configure(command=change_font_align_right)

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


# # #for making everything highlighted into normal 
# # def tag_removal(event=None):
# #     if text_editor.edit_modified():
# #         text_editor.tag_delete('match',1.0,'end')
# #     text_editor.edit_modified(False)

# # text_editor.bind('<<Modified>>',tag_removal)

#-------------------text + toolbar finish ----------------------------------------------------------

##------------------status bar ---------------------------------------------------
status_bar = ttk.Label(main_win, text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_change = False
def change_count(main_win):
    global text_change
    if text_editor.edit_modified():
        text_change=True
        text = text_editor.get(1.0,'end-1c')
        words = len(text.split())
        character = len(text)
        status_bar.config(text=f' words : {words}, characters : {character} ')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>',change_count)


##-----------------status bar finish-------------------------------------------

def refresh_text(event=None):
    text_editor.tag_remove('match',1.0,'end')
    text_editor.tag_remove('replace',1.0,'end')
    



main_win.config(menu= main_menu)

#shortcut allotment ------------------------------
main_win.bind("<Control-f>",find_replace_text_func)
main_win.bind("<Control-o>",open_file_func)
main_win.bind("<Control-n>",new_file_func)
main_win.bind("<Control-s>",save_file_func)
main_win.bind("<Control-z>",save_as_file_func)
main_win.bind("<Control-r>",refresh_text)
main_win.bind("<Control-Shift-d>",lambda:text_editor.delete(1.0,'end'))

# main_win.bind("<Control-f>",find_replace_text_func)

main_win.mainloop()