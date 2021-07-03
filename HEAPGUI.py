from tkinter import *
from heaps import Minheap
from heaps import MaxHeap



def setMax():
    global _type
    _type = 'max'


def setMin():
    global _type
    _type = 'min'
    



def drawItems(heap):
    k = 0
    line_y = 60
    space = cv.winfo_width()/2 -20
    new_line_x = space - 60
    line_reduce = 80
    spacing = 40
    line_x = space
    line_start = line_x

    rowCounter = 0
    oval_size = 20

    locs = []

    for i in range(heap.size):
        cv.create_oval(line_x-oval_size,line_y-oval_size,line_x+oval_size,line_y+oval_size,fill='red')
        cv.create_text(line_x,line_y,text=str(heap.heap[i]),font=('david',15),fill='white')
        locs.append((line_x,line_y+10))

        rowCounter +=1
        if (rowCounter >= 2**k):
            k+=1
            line_start -= line_reduce
            line_reduce *= 1.12
            line_x = line_start
            line_y += 60
            rowCounter = 0
            spacing *= 1.2
        line_x += spacing

    for i,l in enumerate(locs):
        left = 2*i + 1
        right = 2*i + 2
        if left <= heap.size - 1:
            cv.create_line(l,locs[left],fill='green')
        
        if right <= heap.size - 1:
            cv.create_line(l,locs[right],fill='green')






def removemin():
    cv.delete('all')

    global globalHeap
    global _type


    globalHeap.getTop()

    drawItems(globalHeap)

# functions go here
# loooooooooooooooool
def add_numbers():
    l = ent.get().split(',')
    res  = []
    for c in l:
        res.append(int(c))

    global globalHeap
    global _type
    if _type == 'min':
        globalHeap = Minheap(res)
    
    else:
        globalHeap = MaxHeap(res)

    # print(globalHeap.heap)

    drawItems(globalHeap)




    

    


    # python magic
    




HEIGHT = 600
WIDTH = 1000



_type = None
globalHeap = None




# ok step 1: we need a window
window = Tk() 
window.title('heap visual') #this sets a title using a string
# loooool
window.geometry(f'{WIDTH}x{HEIGHT}') #this is for the size (resolution) , takes str
#u get used to it, took m e a while too but now i know them by heart
cv = Canvas(window,bg = 'dark gray',width=WIDTH,height=HEIGHT)
cv.pack()

addnumButton = Button(cv,text='add numbers',font=('times new roman',17),command=add_numbers)
addnumButton.place(relx=0.8,rely=0.90)


removeMin = Button(cv,text=f'Remove Top',font=('times new roman',17),command=removemin)
removeMin.place(relx=0.6,rely=0.9)



# yarin are u ready for python magic????????????
# this is called annonymous function


# L0L zohar
MIN = Radiobutton(cv,text='Minimum heap',value=1,command=setMin)
MAX = Radiobutton(cv,text='Maximum heap',value=2,command=setMax)


MIN.place(relx=0.2,rely=0.8)
MAX.place(relx=0.4,rely=0.8)


ent = Entry(cv,width=50,font=('david',14))
ent.place(relx=0.1,rely=0.9)

# step 2: run the window loop (in frames)
window.mainloop()



