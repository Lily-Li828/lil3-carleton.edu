#Assignment 2: Lily Li  Yiwen Luo
import sys
import csv

#function which print out titles of books according to strings it contains.

def search_title(string,reader):
    for row in reader:
      title = row[0]
      if(string in title.lower()):
        print(title)


#function which print out titles of books according to year of publication.
def search_year(startY, endY,reader):
    for row in reader:
      year = int(row[1])
      if(year>= startY and year <= endY):
        print(row[0])


#function which print out authors' names and books according to string in their name

def search_author(string, reader):
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
     
      
#implementation of different functions according to users' input

def main():
  reader = csv.reader(open('books.csv'))  
  try:
    if (sys.argv[1] == 'st' or sys.argv[1] == 'title'  ):
      try:
        string = sys.argv[2]
        print('\033[4m'+"Below are book titles containing "+string+'\033[0m')
        search_title(string,reader)
      except:
        print("Please enter the string you would like to search")

    elif(sys.argv[1] == 'sy' or sys.argv[1] == 'year'):
      try:
        startY = int(sys.argv[2]) 
        endY = int(sys.argv[3]) 
        print('\033[4m'+"Below are books publish between ",startY ,"and " ,endY,'\033[0m')
        search_year(startY, endY,reader)
      except:
        print("Please enter the range of publishing years you would like to search, in formate [start year] [end year] ")
 
    elif(sys.argv[1] == 'sa' or sys.argv[1] == 'author'):
      try:
        string = sys.argv[2]
        print("Below are authors with names containing "+string)
        print("publications of the author are in purple ")
        print('')
        search_author(string,reader)
      except:
        print("Please enter the string which you would like the authors' name to contain")


