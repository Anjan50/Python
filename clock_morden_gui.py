from threading import *
from tkinter import *
from datetime import datetime
from time import strftime

root = Tk(className="clock")
root.maxsize(height=350, width=600)
root.minsize(height=350, width=600)
root.geometry('600x400')

bgColor = '#262626'
fgColor = 'white'

root.config(bg=bgColor)

running = False
hours, minutes, seconds = 0, 0, 0

global back
back = 0


def default_home():
    f2 = Frame(root, width=600, height=350, bg=bgColor)
    f2.place(x=0, y=45)

    time_lable = Label(root, text='\nCLOCK', font=(20), fg=fgColor, bg=bgColor)
    time_lable.place(x=270, y=60)

    date_today = datetime.today().strftime('%A')
    date_today_3 = date_today.upper()
    date = date_today_3[:3]

    def get_time():

        if (format == 1):
            time = strftime('%H : %M : %S')  #I H
        else:
            time = strftime('%I : %M : %S')  #I H

        if (back == 1):
            time = strftime('%I : %M : %S')  #I H

        time_text.config(text=time)
        time_text.after(1000, get_time)

    time_text = Label(root,
                      font=("century gothic", 30),
                      fg=fgColor,
                      bg=bgColor)
    time_text.place(x=258, y=170)  #x258

    date_text = Label(root,
                      text=date + " | ",
                      fg=fgColor,
                      bg=bgColor,
                      font=("century gothic", 28))
    date_text.place(x=138, y=171)  #x138

    tod = Label(text='DAY', font=("century gothic", 8), fg=fgColor, bg=bgColor)
    tod.place(x=165, y=214)

    hour = Label(text='Hour',
                 font=("century gothic", 8),
                 fg=fgColor,
                 bg=bgColor)
    hour.place(x=270, y=214)

    min = Label(text='MIN', font=("century gothic", 8), fg=fgColor, bg=bgColor)
    min.place(x=346, y=214)

    sec = Label(text='SEC', font=("century gothic", 8), fg=fgColor, bg=bgColor)
    sec.place(x=423, y=214)
    get_time()


def home():
    f1.destroy()
    f2 = Frame(root, width=600, height=350, bg=bgColor)
    f2.place(x=0, y=45)

    time_lable = Label(root, text='\nCLOCK', font=(20), fg=fgColor, bg=bgColor)
    time_lable.place(x=275, y=60)

    date_today = datetime.today().strftime('%A')
    date_today_3 = date_today.upper()
    date = date_today_3[:3]

    def get_time():

        if (format == 1):
            time = strftime('%H : %M : %S')  #I H
        else:
            time = strftime('%I : %M : %S')  #I H

        if (back == 1):
            time = strftime('%I : %M : %S')  #I H

        time_text.config(text=time)
        time_text.after(1000, get_time)

    time_text = Label(root,
                      font=("century gothic", 30),
                      fg=fgColor,
                      bg=bgColor)
    time_text.place(x=258, y=170)  #x258

    date_text = Label(root,
                      text=date + " | ",
                      fg=fgColor,
                      bg=bgColor,
                      font=("century gothic", 28))
    date_text.place(x=138, y=171)  #x138

    tod = Label(text='DAY', font=("century gothic", 8), fg=fgColor, bg=bgColor)
    tod.place(x=165, y=214)
    hour = Label(text='Hour',
                 font=("century gothic", 8),
                 fg=fgColor,
                 bg=bgColor)
    hour.place(x=270, y=214)
    min = Label(text='MIN', font=("century gothic", 8), fg=fgColor, bg=bgColor)
    min.place(x=346, y=214)
    sec = Label(text='SEC', font=("century gothic", 8), fg=fgColor, bg=bgColor)
    sec.place(x=423, y=214)
    get_time()


def stopwatch():

    f1.destroy()
    f2 = Canvas(root, width=600, height=350, bg=bgColor, highlightthickness=0)
    f2.place(x=0, y=45)

    l2 = Label(root, text='\nSTOPWATCH', font=(20), fg=fgColor, bg=bgColor)
    l2.place(x=245, y=65)

    def start():
        global running
        if not running:
            update()
            running = True

        start_button.destroy()

        def pause():
            global running
            if running:
                stopwatch_label.after_cancel(update_time)
                running = False

            if not running:
                pause_button.destroy()

            start_button = Button(f2, text='start', width=6, command=start)
            start_button.place(x=245, y=170)

        global pause_button
        pause_button = Button(f2, text='pause', width=6, command=pause)
        pause_button.place(x=245, y=170)

    def reset():
        global running
        if running:
            stopwatch_label.after_cancel(update_time)
            running = False
        global hours, minutes, seconds
        hours, minutes, seconds = 0, 0, 0
        stopwatch_label.config(text='00:00:00')

    def update():
        global hours, minutes, seconds
        seconds += 1
        if seconds == 60:
            minutes += 1
            seconds = 0
        if minutes == 60:
            hours += 1
            minutes = 0
        hours_string = f'{hours}' if hours > 9 else f'0{hours}'
        minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
        seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
        stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' +
                               seconds_string)

        global update_time
        update_time = stopwatch_label.after(1000, update)

    stopwatch_label = Label(text='00:00:00',
                            font=("century gothic", 30),
                            fg=fgColor,
                            bg=bgColor)
    stopwatch_label.place(x=230, y=145)

    start_button = Button(f2, text='start', width=6, command=start)
    start_button.place(x=245, y=170)
    reset_button = Button(f2, text='reset', width=6, command=reset)
    reset_button.place(x=323, y=170)


def exit():
    quit()


def toggle_win():

    global f1
    f1 = Frame(root, width=160, height=350, bg='#12c4c0')
    f1.place(x=0, y=0)

    #buttons
    def bttn(x, y, text, bcolor, fcolor, cmd):

        def on_entera(e):
            myButton1['background'] = bcolor  #ffcc66
            myButton1['foreground'] = bgColor  #000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground'] = bgColor

        myButton1 = Button(f1,
                           text=text,
                           width=23,
                           height=2,
                           fg=bgColor,
                           border=0,
                           bg=fcolor,
                           activeforeground=bgColor,
                           activebackground=bcolor,
                           command=cmd)

        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x, y=y)

    bttn(0, 80, 'C L O C K', '#0f9d9a', '#12c4c0', home)
    bttn(0, 117, 'S T O P W A T C H', '#0f9d9a', '#12c4c0', stopwatch)
    bttn(0, 317, 'E X I T ', '#0f9d9a', '#12c4c0', exit)

    def dele():
        f1.destroy()
        b2 = Button(root,
                    text='=',
                    font=("century gothic", 12),
                    border=0,
                    command=toggle_win,
                    bg='#12c4c0',
                    activebackground='#12c4c0')
        b2.place(x=5, y=10)

    Button(f1,
           text='x',
           font=("century gothic", 12),
           border=0,
           command=dele,
           bg='#12c4c0',
           activebackground='#12c4c0').place(x=5, y=10)


default_home()

global b2
b2 = Button(root,
            text='=',
            font=("century gothic", 12),
            border=0,
            command=toggle_win,
            bg='#12c4c0',
            activebackground='#12c4c0').place(x=5, y=10)

root.mainloop()
