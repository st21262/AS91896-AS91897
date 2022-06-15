"""Julie's Party Hire
This program is to keep track of how many items Julie has out currently.

Julie runs a party hire store and has a range of items for hire. She needs to keep a
track of items that are currently out
She needs to keep the following details

Customer full name
Receipt number
The item that is hired
How many of the item the customer has hired
To ensure good data collection the following are required
Customer full name required
Receipt number only
The item that is hired required
How many of the item the customer has hired between 1 and 500
When an item is returned she needs to be able to delete it, so it no longer shows.
"""

# import tkinter
import tkinter

item_hire_entry = ' '
full_name_entry = ' '
item_amount_entry = ' '
item_hire_message = ' '
full_name_message = ' '
item_amount_message = ' '
full_name = ' '
item_hire = ' '
item_amount = ' '
full_name_label = ' '
item_amount_label = ' '
item_hire_label = ' '
clear_button = ' '
check_button = ' '
enter_button = ' '


# minimum and maximum number of items hired
MIN_ITEM_HIRE = 1
MAX_ITEM_HIRE = 500

# include a subroutine to close the window
def quit():
     root.destroy()

# include a subroutine to check the valid of input for
# full name, item for hire, and item amount
def checkValidity():
    allValid = True

    # make sure full name isn't empty
    if full_name_entry.get() == 0:

        #entry field must be red
        full_name_entry.configure(background='#FFC0C0',
                                 highlightbackground='#FF8080',
                                 highlightcolor='#FF8080',
                                 highlightthickness=2)

        # have an error message set up
        full_name_message.configure(text='Required')

        #set allValid to False
        allValid = False

        # reset color so entry field is back to white
    else:
        full_name_entry.configure(background='#FFFFFF',
                                  highlightbackground=None,
                                  highlightcolor=None,
                                  highlightthickness=0)

        full_name_entry.Message.configure(text='')

    # make sure item hired isnt empty
    if item_hire_entry.get() == 0:
        #entry field must be red
        item_hire_entry.configure(background='#FFC0C0',
                                  highlightbackground='#FF8080',
                                  highlightcolor='FF8080',
                                  highlightthickness=2)

        # display error message
        item_hire_message.configure(text='Item hired must not be empty')

        # set allValid to False
        allValid = False

        # resets colour of item hired entry field and removed the error
    else:
        item_hire_entry.configure(background='#FFFFFF',
                                 highlightbackground=None,
                                 highlightcolor=None,
                                 highlightthickness=0)

        item_hire_message.configure(text='')

        # make sure that the input for item amount is an integer
        if item_amount.get().isdigit() == False:

            #make item amount entry field red
            item_amount_entry.configure(background='#FFC0C0',
                                     highlightbackground='#FF8080',
                                     highlightcolor='#FF8080',
                                     highlightthickness=2)

            #display error message
            item_amount_message.configure(text='must be a number between {} and {} (inclusive)'
                                                   .format(str(MIN_ITEM_HIRE),str(MAX_ITEM_HIRE)))

            # set allValid to False
            allValid = False

        # check if item amount is more than 500
        elif int(item_amount_entry.get()) > 500:
            # make item amount entry field red
            item_amount_entry.configure(background='#FFC0C0',
                                 highlightbackground='#FF8080',
                                 highlightcolor='#FF8080',
                                 highlightthickness=2)

def enter():
    pass    # test
def clear():
    pass    # test

def main():

    global main_window, root
    global full_name, item_hire, item_amount, receipt_id, check, enter, clear, all_items_list

    main_window = tkinter.Tk()

    root = tkinter.Tk()

    # create main frame for buttons and entry fields
    main_frame = tkinter.Frame(root)

    # create gap between main_frame and print_frame
    main_frame.pack(pady=10)

    # create empty list to store what items for each group
    all_items_list = []

    # create labels and entry fields for user to input info
    full_name_label = tkinter.Label(main_frame, text='Full name')
    full_name_label.grid(row=1, column=0)

    full_name_entry = tkinter.Entry(main_frame)
    full_name_entry.grid(row=1, column=1)

    item_hire_label = tkinter.Label(main_frame, text='Item for hire')
    item_hire_label.grid(row=2, column=0)

    item_hire_entry = tkinter.Entry(main_frame)
    item_hire_entry.grid(row=2, column=1)

    item_amount_label = tkinter.Label(main_frame, text='Item amount')
    item_amount_label.grid(row=3, column=0)

    item_amount_entry = tkinter.Entry(main_frame)
    item_amount_entry.grid(row=3, column=1)

    # create error labels to display error messages
    full_name_message = tkinter.Label(main_frame)
    full_name_message.grid(row=1, column=2)

    item_hire_message = tkinter.Label(main_frame)
    item_hire_message.grid(row=2, column=2)

    item_amount_message = tkinter.Label(main_frame)
    item_amount_message.grid(row=3, column=2)

    # create the buttons
    clear_button = tkinter.Button(main_frame, text='Clear',command=clear)
    clear_button.grid(row=5, column=0)

    enter_button = tkinter.Button(main_frame, text='Enter', command=enter)
    enter_button.grid(row=5, column=1)

    check_button = tkinter.Button(main_frame, text='Check', command=checkValidity)
    check_button.grid(row=7, column=1)



    main_window.mainloop()
    root.mainloop()

main()








