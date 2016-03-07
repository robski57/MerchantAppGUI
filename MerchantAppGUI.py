import sqlite3

from tkinter import *

database_filename = "merchant_db"

class MerchantGUI(Frame):

    def __init__(self):

        Frame.__init__(self)
        self.master.title("Merchant App")

        self.master.minsize(300, 200)
        self.pack()

        self._merchantItem = Label(self, text="Hat 19, Sweater 25, Jacket 50")
        self._merchantItem.pack()

        self._merchantVar = StringVar()
        self._merchantEntry = Entry(self, textvariablr=self._merchantItemVar, width=50)
        self._merchantEntry.pack()

       # self._enterItem = Label(self, text="Enter Item")
       # self._enterItem.pack

       # self._enterItem = StringVar()
       # self._enterItem = Entry(self,textvariable=self._enterItemVar, width=50)
       # self._enterItem.pack()

        self._enterAmount = Label(self, text="Enter Amount")
        self._enterAmount.pack

        self._enterAmount = StringVar()
        self._enterAmount = Entry(self,textvariable=self._enterAmountVar, width=50)
        self._enterAmount.pack()

        self._enterPrice = Label(self, text="Enter Price")
        self._enterPrice.pack

        self._enterPrice = StringVar()
        self._enterPrice = Entry(self,textvariable=self._enterPriceVar, width=50)
        self._enterPrice.pack()

        self._totalButton = Button(self, text="Total", command=self._total)
        self._totalButton.pack()

        self._resultVar = StringVar()
        self._resultLabel = Label(self, text=" \n ", textvariable=self._resultVar)
        self._resultLabel.pack()

        self._quitButton = Button(self, text="Quit", command=self._quit)
        self._quitButton.pack()

def _auth(self, enterItem, enterAmount, enterPrice):

    print("Attempting to total enterAmout: %s \nenterPrice: %s" % (enterAmount, enterPrice))

    db = sqlite3.connect(database_filename)
    db.row_factory = sqlite3.Row
    cursor = db.cursor()

    sql_statement = '''SELECT merchantItem FROM enterAmount WHERE'''

    print('About to execute the following SQL statement: \n' + sql_statement)

    cursor.execute(sql_statement)   # Execute the SQL statement we created

#    result = None  # Assume login fails, unless DB returns a row for this user

        # This loop won't run if no results are returned.
    for row in cursor:
            result = row['item']  # Extract name from first row
            break

            db.close()
            return result

def _quit(self):

        exit(0)

def _login(self):
          enterItem = self._enterItemVar.get()
          enterAmount = self._enterAmountVar.get()
          enterPrice = self._enterPriceVar.get()
          #result = self._auth(enterAmount, enterPrice)


#if result is None:
 #           display_result = "Enter Amount or Enter Price incorrect"
#else:
#            display_result = "Welcome, " + result

#self._resultVar.set(display_result)

def setup_database():

    db = sqlite3.connect('database_filename')
    cursor = db.cursor()

    # Delete any existing data
    cursor.execute('DROP TABLE IF EXISTS users')

    db.commit()

    # Create a database table with columns for user's name (name), user id (user),  and password (password)
    cursor.execute('CREATE TABLE IF NOT EXISTS merchantItem (Item text, Price text, Amount text) ')

    # Add some sample data. Note that the admin is the first entry in the table, as is often the case
    cursor.execute('''INSERT INTO merchantItem VALUES ( 'Hat', '19', '') ''')
    cursor.execute('''INSERT INTO merchantItem VALUES ( 'Shirt', '25', '') ''')
    cursor.execute('''INSERT INTO merchantItem VALUES ( 'Shoes', '50', '') ''')
    cursor.execute('''INSERT INTO merchantItem VALUES ( 'Jacket', '60', '' ) ''')

    # commit saves changes
    db.commit()

    # and then close the connection to the database.
    db.close()


def start_gui():

    MerchantGUI().mainloop()


def quit():

    sys.exit()


def main():
    setup_database()
    start_gui()


main()          

    
