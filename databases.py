from tkinter import *
import sqlite3

root = Tk()
root.title("Databases...")
root.iconbitmap('images/codemy.ico')
root.geometry('400x600')


# Update record
def update():
    editor = Tk()
    editor.title("Update record...")
    editor.iconbitmap('images/codemy.ico')
    editor.geometry('400x600')

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("""UPDATE addresses SET 
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
        WHERE oid = :oid""",
              {
                'first': f_name_editor.get(),
                'last': l_name_editor.get(),
                'address': address_editor.get(),
                'city': city_editor.get(),
                'state': state_editor.get(),
                'zipcode': zipcode_editor.get(),
                'oid': record_id
              }
             )

    conn.commit()
    conn.close()

    editor.destroy()


# Edit record
def edit():
    global editor

    editor = Tk()
    editor.title("Edit record...")
    editor.iconbitmap('images/codemy.ico')
    editor.geometry('400x250')

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()

    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # Create Text fields
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    # Loop through results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # Create Text field labels
    f_name_label_editor = Label(editor, text="First Name")
    f_name_label_editor.grid(row=0, column=0, pady=(10, 0))

    l_name_label_editor = Label(editor, text="LastName")
    l_name_label_editor.grid(row=1, column=0)

    address_label_editor = Label(editor, text="Address")
    address_label_editor.grid(row=2, column=0)

    city_label_editor = Label(editor, text="City")
    city_label_editor.grid(row=3, column=0)

    state_label_editor = Label(editor, text="State")
    state_label_editor.grid(row=4, column=0)

    zipcode_label_editor = Label(editor, text="Zip Code")
    zipcode_label_editor.grid(row=5, column=0)

    edit_button_editor = Button(editor, text='Save edited record', command=update)
    edit_button_editor.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

    conn.commit()
    conn.close()


# Delete a record
def delete():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute('DELETE FROM addresses WHERE oid = ' + delete_box.get())

    conn.commit()
    conn.close()


# Create submit function
def submit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses values (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()
              }
              )

    conn.commit()
    conn.close()

    # Clear inputs
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# Create query function
def query():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print_records = ""

    for record in records:
        print_records += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t ' + str(record[6]) + '\n'

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

    conn.commit()
    conn.close()


# Create or connect to DB
conn = sqlite3.connect('address_book.db')
# Create a cursor
c = conn.cursor()
# Create table
''' commented out as its built
c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )
""")
'''
# Create Text fields
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)


# Create Text field labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))

l_name_label = Label(root, text="LastName")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zip Code")
zipcode_label.grid(row=5, column=0)

delete_label = Label(root, text="ID No:")
delete_label.grid(row=9, column=0, pady=5)

# Create submit button
submit_button = Button(root, text='Add to database', command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create query button
query_button = Button(root, text='Show records', command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create delete button
delete_button = Button(root, text='Delete record', command=delete)
delete_button.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

# Create edit button
edit_button = Button(root, text='Edit record', command=edit)
edit_button.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

# Commit and close DB
conn.commit()
conn.close()

root.mainloop()
