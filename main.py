from tkinter import *
from tkinter import messagebox
from timeit import default_timer as timer
import random

root = Tk()
root.geometry("500x500")
root.configure(bg="#233d4d")

window = Tk()
window.geometry("550x500")
window.configure(bg="#233d4d")
window.withdraw()

hs_file = open('highscore.txt', 'r+')
x = 0


def game():
    global x
    if x == 0:
        root.withdraw()
        x = x+1
    window.deiconify()

    def check_result():
        j = error = 0
        answer = entry.get("1.0", 'end-1c')
        end = timer()
        time_taken = end-start
        # len diff
        if len(words[word]) > len(answer):
            error = len(words[word])-len(answer)
            for i in answer:  # take shorter sentence
                if i == words[word][j]:
                    pass
                else:
                    error += 1
                j += 1
        elif len(words[word]) < len(answer):
            error = len(answer)-len(words[word])
            for i in words[word]:
                if i == answer[j]:
                    pass
                else:
                    error += 1
                j += 1
        wpm = len(answer)/5
        wpm = wpm - error
        wpm = int(wpm/(time_taken/60))
        hs_file.seek(0)
        line = int(hs_file.readline())
        if wpm > line:
            hs_file.seek(0)
            hs_file.write(str(wpm))
            result = "Amazing! Your new highscore is: "+str(wpm)+" WPM"
            messagebox.showinfo("Score", result)
            finish()
        else:
            result = "Your score is: "+str(wpm)+" WPM\nBetter luck next time!"
            messagebox.showinfo("Score", result)

    def finish():
        hs_file.close()
        window.destroy()
        root.destroy()

    words = ["bright sun is blinding me", "different colour would suit me better", "as busy as could be at this moment", "please inform us of your decision", "do not delay this process anymore", "I would do anything to possess such a necklace", "weary traveler relaxes in a rundown pub", "running from danger is completely natural", "even a narrow road can lead to something magnificent", "ruthless pirates have rulled this sea for decades", "what language is your favourite?", "this is too spooky even for me"]
    word = random.randint(0, (len(words)-1))

    x2 = Label(window, text=words[word], bg="black", fg="white", height=7, width=47, font="times 15", wraplength=500)
    x2.place(x=15, y=10)

    x3 = Button(window, text="Submit!", font="times 20", bg="#ffc300", command=check_result)
    x3.place(x=220, y=350)
    window.bind('Enter', lambda event: check_result)

    entry = Text(window)
    entry.place(x=50, y=180, height=150, width=450)

    b2 = Button(window, text="Done", font="times 13", bg='#a1c181', width=12, command=finish)
    b2.place(x=155, y=420)

    b3 = Button(window, text="Another One!", font="times 13", bg='#a1c181', width=12, command=game)
    b3.place(x=265, y=420)

    start = timer()


x1 = Label(root, text="Let's test your typing speed!", bg="#233d4d", fg="white", font="times 20")
x1.place(x=100, y=50)

b1 = Button(root, text="Go!", width=12, bg='#a1c181', font="times 20", command=game)
b1.place(x=150, y=120)

hs_text = Label(root, text="Highscore:", width=12, fg='#fff', bg='#233d4d', font="times 35")
hs_text.place(x=90, y=240)

hs = int(hs_file.readline())
hs_val = Label(root, text=str(hs) + " WPM", width=12, fg='#79bcb8', bg='#233d4d', font="times 30")
hs_val.place(x=110, y=320)

root.mainloop()
window.mainloop()
