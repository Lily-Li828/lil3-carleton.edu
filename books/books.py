import sys
import csv

def search_title(string):
  with open('books.csv', newline='') as k:
    reader = csv.reader(k)
    for row in reader:
      title = row[0]
      if(string in title.lower()):
        print(title)


def search_year(startY, endY):
  with open('books.csv', newline='') as k:
    reader = csv.reader(k)
    for row in reader:
      year = int(row[1])
      if(year>= startY and year <= endY):
        print(row[0])


def search_author(string):
 with open('books.csv', newline='') as k:
    reader = csv.reader(k)
    namelist = []
    for row in reader:
      author = row[2]
      if(string in author.lower() and author not in namelist):
        print('\033[1m'+author+'\033[0m')
        namelist.append(author)
        with open('books.csv', newline='') as j:
          readerr = csv.reader(j)
          for row in readerr:
            if(row[2]==author):
              print('\033[95m'+row[0]+'\033[0m')
          print('')
     
      

  
try:
  if (sys.argv[1] == 'st' or sys.argv[1] == 'search-title'  ):
    try:
      string = sys.argv[2]
      print('\033[4m'+"Below are book titles containing "+string+'\033[0m')
      search_title(string)
    except:
      print("Please enter the string you would like to search")

  elif(sys.argv[1] == 'sy' or sys.argv[1] == 'search-year'):
    try:
      startY = int(sys.argv[2]) 
      endY = int(sys.argv[3]) 
      print('\033[4m'+"Below are books publish between ",startY ,"and " ,endY,'\033[0m')
      search_year(startY, endY)
    except:
      print("Please enter the range of publishing years you would like to search, in formate [start year] [end year] ")

  elif(sys.argv[1] == 'sa' or sys.argv[1] == 'search-author'):
    try:
      string = sys.argv[2]
      print("Below are authors with names containing "+string)
      print("publications of the author are in purple ")
      print('')
      search_author(string)
    except:
      print("Please enter the string which you would like the authors' name to contain")




except:
  print("Please enter an operation, such as st(search books according to title), sy(search according to year), and sa(search according to author)")






