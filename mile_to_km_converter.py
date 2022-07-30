from tkinter import *
window = Tk()
window.minsize(width=400,height=300)
window.config(pady=20,padx=20)
window.title("MILE TO KM CONVERTER")
text_input1 = Label(text="Miles",font=("Arial",18,"bold"))
text_input1.grid(column=3,row=0)
text_input2 = Label(text="is equal to",font=("Arial",18,"bold"))
text_input2.grid(column =0,row=2)
text_input3 = Label(text="Km",font=("Arial",18,"bold"))
text_input3.grid(column=3,row=2)

#Miles
miles_input = Entry(width=10,font=("Arial",14,"bold"))

miles_input.focus()
miles_input.grid(column=2,row=0)

#KM
km_output = Label(text="0",font=("Arial",14,"bold"))
km_output.grid(column=2,row=2)

#calculate button
def miles_to_km():
    miles = miles_input.get()
    km = 1.60934 *int(miles)
    km_output.config(text=km)
button = Button(text="Calculate",command=miles_to_km)
button.grid(column=2,row=3)

window.mainloop()