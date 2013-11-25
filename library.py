# Library by Zachary Lucas
from collections import namedtuple
Library = namedtuple("Library","title author status")
#Array of library objects:
m = []

print("Welcome to your library!")
while(1):
    goBack = False
    # Get input:
    var = raw_input("> ")
    splitIn = var.partition(" ")
    if (var == "quit"):
        exit("Bye!")
    elif (splitIn[0] == "add"):
        splitAgain = splitIn[2].partition("\"")
        titleTuple = splitAgain[2].partition("\"")
        title = titleTuple[0]
        splitAgain = titleTuple[2].partition("\"")
        authorTuple = splitAgain[2].partition("\"")
        author = authorTuple[0]
        # To check if a title has been added:
        for i in m:
            if (i.title == title):
                print("Sorry, you can't add the same title twice!")
                goBack = True
        if (goBack == True):
            continue
        print("Added " + title + " by "+author+" to the list")
        m.append(Library(title,author,"unread"))
    elif (splitIn[0] == "read"):
        splitAgain = splitIn[2].partition("\"")
        titleTuple = splitAgain[2].partition("\"")
        title = titleTuple[0]
        #Goes through library, replacing an unread version of a book with a read version
        for i,j in enumerate(m):
            if (j.title == title):
                tempTitle = j.title
                tempAuthor = j.author
                del m[i]
                m.append(Library(tempTitle,tempAuthor,"read"))
        print("You've read "+title+"!")
    elif (splitIn[0] == "show"):
        show = splitIn[2]
        if (show == "all"):
            for i in m:
                print("\""+i.title+"\" by "+i.author+" ("+i.status+")")
            continue
        allBy = show.partition(" ")
        allBy1 = allBy[2].partition(" ")
        if (allBy1[0] == "by" and allBy[0] == "all"):
            # Go through library, show all by specified author
            allBy2 = allBy1[2].partition("\"")
            allBy3 = allBy2[2].partition("\"")
            for i in m:
                if(i.author == allBy3[0]):
                    print("\""+i.title+"\" by "+i.author+" ("+i.status+")")
            continue
        elif (show == "unread"):
            # Go through library, get all unread books
            for i in m:
                if (i.status == "unread"):
                    print("\""+i.title+"\" by "+i.author+" ("+i.status+")")
            continue
        unreadBy = show.partition(" ")
        unreadBy1 = unreadBy[2].partition(" ")
        if (unreadBy1[0] == "by"):
            unreadBy2 = unreadBy1[2].partition("\"")
            unreadBy3 = unreadBy2[2].partition("\"")
            # Go through, get all unread books by specified author
            for i in m:
                if (i.author == unreadBy3[0] and i.status == "unread"):
                    print("\""+i.title+"\" by "+i.author+" ("+i.status+")")
    else:
        print("Unrecognized Command.")

