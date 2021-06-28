import random
import datetime


def checkemptystring():
    valid = False
    while not valid:
        text = input('Type here: ')
        if str(text).strip() == '':
            print('Entry can\'t be empty please try again')
        else:
            return text


def checkifnumber():
    valid = False
    while not valid:
        num = input('Type here: ')
        try:
            int(num)
            valid = True
            return num
        except:
            print('Please enter a number')


def checkifyear():
    valid = False
    while not valid:
        year = input('Type here:')
        try:
            if 0 <= int(year) <= 2021:
                valid = True
                return year
            else:
                print('Please enter a year between 0 and 2021')
        except:
            print('please enter a valid year between 0 and 2021')


def checkifdate():
    valid = False
    while not valid:
        date = input('Please enter a date (yyyy-mm-dd)')
        try:
            year, month, day = date.split('-')
            if 0 <= int(year) <= 2021 and 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                datetime.date(int(year), int(month), int(day))
                valid = True
                return date
            else:
                continue
        except:
            print('please enter an appropriate date (yyyy-mm-dd) ')


class Books:
    def __init__(self):
        self.bookID = random.randint(1, 1000000)
        self.title = ''
        self.author = ''
        self.year = ''
        self.publisher = ''
        self.copiesavailable = 0
        self.publicationdate = ''

    def settitle(self):
        print('please enter the title')
        self.title = checkemptystring()

    def setauthor(self):
        print('please enter the author')
        self.author = checkemptystring()

    def setyear(self):
        print('please enter the year')
        self.year = checkifyear()

    def setpublisher(self):
        print('please enter the publisher')
        self.publisher = checkemptystring()

    def setcopies(self):
        print('please enter the number of copies')
        self.copiesavailable = checkifnumber()

    def setpubdate(self):
        print('please enter the publication date')
        self.publicationdate = checkifdate()

    def returntitle(self):
        return self.title

    def returnauthor(self):
        return self.author

    def returnyear(self):
        return self.year

    def returnpublisher(self):
        return self.publisher

    def returncopies(self):
        return self.copiesavailable

    def returnpubdate(self):
        return self.publicationdate

    def bookdetails(self):
        print(f'title: {self.returntitle()} \n'
              f'author: {self.returnauthor()} \n'
              f'year: {self.returnyear()}  \n'
              f'publisher: {self.returnpublisher()} \n'
              f'publication date: {self.returnpubdate()} \n'
              f'copies available: {self.returncopies()}')


class BookList:
    def __init__(self):
        self.booklist = {}

    def storebook(self, book):
        self.booklist[book.title] = {'title': book.title,
                                     'author': book.author,
                                     'publisher': book.publisher,
                                     'pubdate': book.publicationdate,
                                     'bookobj': book}

    def findbook(self):
        print('What book are you looking for?')
        book = checkemptystring()
        b = [key for key in self.booklist for i in ['title', 'author', 'publisher', 'pubdate'] if
             self.booklist[key][i] == book]

        return b

    def bookdetails(self, book):
        self.booklist[book]['bookobj'].bookdetails()

    def removebook(self, title):
        try:
            del self.booklist[title]
        except:
            print('There is no book with that title please try again')

    def numberofbooks(self):
        return len(self.booklist)

    def updatebookdetails(self):
        pass


class Users:
    def __init__(self):
        self.username = ''
        self.firstname = ''
        self.surname = ''
        self.housenumber = ''
        self.street = ''
        self.postcode = ''
        self.email = ''
        self.dob = ''

    def setusername(self):
        print('please enter the username')
        self.username = checkemptystring()

    def setfirstname(self):
        print('please enter the first name')
        self.firstname = checkemptystring()

    def setsurname(self):
        print('please enter the surname')
        self.surname = checkemptystring()

    def sethousenumber(self):
        print('please enter the house number')
        self.housenumber = checkifnumber()

    def setstreet(self):
        print('please enter the street name')
        self.street = checkemptystring()

    def setpostcode(self):
        print('please enter the post code')
        self.postcode = checkemptystring()

    def setemail(self):
        print('please enter the email')
        self.email = checkemptystring()

    def setdob(self):
        print('please enter the date of birth')
        self.dob = checkifdate()

    def returnusername(self):
        return self.username

    def returnfirstname(self):
        return self.firstname

    def returnsurname(self):
        return self.surname

    def returnhousenumber(self):
        return self.housenumber

    def returnstreet(self):
        return self.street

    def returnpostcode(self):
        return self.postcode

    def returnemail(self):
        return self.email

    def returndob(self):
        return self.dob

    def returnuserdetails(self):
        print(f'Username: {self.username} \n'
              f'FirstName: {self.firstname} \n'
              f'Surname: {self.surname} \n'
              f'House Number: {self.housenumber} \n'
              f'Street Name: {self.street} \n'
              f'Postcode: {self.postcode} \n'
              f'Email: {self.email} \n'
              f'dob: {self.dob}')


class UserList:
    def __init__(self):
        self.userlist = {}

    def adduser(self, user):
        self.userlist[user.username] = {'firstname': user.firstname,
                                        'username': user.username,
                                        'object': user}

    def numberofusers(self):
        len(self.userlist)

    def userdetails(self, username):
        self.userlist[username]['object'].returnuserdetails()

    def finduser(self):
        username = checkemptystring()
        users = [key for key in self.userlist for x in ['username', 'firstname'] if self.userlist[key][x] == username]
        if len(users) == 0:
            print('no users exist with this name')
        else:
            return users

    def deluser(self, username):
        del self.userlist[username]


class Loans:
    def __init__(self):
        self.loanlist = {}

    def borrowbook(self, username, booktitle):
        if username in self.loanlist.keys():
            self.loanlist[username].append(booktitle)
        else:
            self.loanlist[username] = [booktitle]

    def returnbook(self, username, booktitle):
        if username not in self.loanlist.keys():
            print('user has no books to return')
        if username in self.loanlist.keys():
            try:
                self.loanlist[username].remove(booktitle)
            except:
                print('user hasn\'nt borrowed this book')
        else:
            print('user has no books to return')

    def returnuserbooksborrowed(self, username):
        len(self.loanlist[username])

    def userwhoborrowed(self, booktitle):
        return [key for key in self.loanlist for i in self.loanlist[key] if booktitle in i]


def librarysystem():
    '''function to house the process of the library system'''
    booklist = BookList()
    userlist = UserList()
    loans = Loans()
    while True:
        print('Welcome to our library system \n'
              'please choose from the options below: \n'
              '1.) Add Book \n'
              '2.) Add User \n'
              '3.) Find a book \n'
              '4.) Find a user \n'
              '5.) Update a books details \n'
              '6.) Update a users details \n'
              '7.) Borrow a book \n'
              '8.) Return a book \n'
              '9.) Remove a book from the system \n'
              '10.) remove a user from the system '
              )
        menuinput = input('Please choose your option(1-8): ')
        if menuinput == '1':
            '''menu input branch for creating a new user'''
            book = Books()
            book.settitle()
            book.setyear()
            book.setauthor()
            book.setpubdate()
            book.setcopies()
            book.setpublisher()
            booklist.storebook(book)
            continue
        elif menuinput == '2':
            '''menu input branch for creating a new user'''
            user = Users()
            user.setusername()
            user.setfirstname()
            user.setsurname()
            user.setemail()
            user.setdob()
            user.sethousenumber()
            user.setstreet()
            user.setpostcode()
            userlist.adduser(user)
            continue
        elif menuinput == '3':
            '''menu input branch for searching for a book'''
            fb = booklist.findbook()
            try:
                for i in fb:
                    print('-----------------------------------------')
                    booklist.bookdetails(i)
                    print('-----------------------------------------')
            except:
                continue
        elif menuinput == '4':
            '''menu input branch for searching for a user'''
            fu = userlist.finduser()
            try:
                for i in fu:
                    print('-----------------------------------------')
                    userlist.userdetails(i)
                    print('-----------------------------------------')
            except:
                continue
        elif menuinput == '5':
            '''menu input branch for updating a books details'''
            pass
        elif menuinput == '6':
            '''menu input branch for updating a users details'''
            pass
        elif menuinput == '7':
            '''menu input branch for borrowing a book'''
            print('please enter the username of the person borrowing the book:')
            un = userlist.finduser()
            print('Which book would you like to borrow?')
            book = booklist.findbook()
            loans.borrowbook(un, book)
        elif menuinput == '8':
            '''menu input branch for returning a book'''
            print('please enter the username of the person borrowing the book:')
            un = userlist.finduser()
            print('Which book would you like to borrow?')
            book = booklist.findbook()
            loans.returnbook(un, book)
        elif menuinput == '9':
            '''menu input branch for removing a book'''
            pass
        elif menuinput == '10':
            '''menu input branch for removing a user'''
            while True:
                print('please enter the user you would like to remove')
                utr = userlist.finduser()
                try:
                    if len(utr) > 1:
                        print('warning the details you entered refer to multiple users:')
                        for i in utr:
                            print(userlist.userdetails(i))
                        imu = input('what would you like to do?: \n'
                                    '1.) delete all matching users \n'
                                    '2.) delete user on username \n'
                                    '3.) nothing')

                        if imu == '1':
                            for i in utr:
                                userlist.deluser(i)
                                print(f'user {i} deleted')
                        elif imu =='2':
                            continue
                        elif imu == '3':
                            break
                    else:
                        userlist.deluser(utr[0])
                        print(f'user {utr[0]} has been deleted')
                except:
                    break

        else:
            print('that option isn\'t available please try again')


'librarysystem()'
