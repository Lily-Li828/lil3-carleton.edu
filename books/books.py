#Assignment 2: Lily Li  Yiwen Luo
import sys
import csv

#function which print out titles of books according to strings it contains.


def search_title(string,reader):
  for row in reader:
    title = row[0]
    if(string.lower() in title.lower()):
      print(title)


#function which print out titles of books according to year of publication.
def search_year(startYear, endYear,reader):
  if(startYear>endYear):
    print("Please enter search years in correct format: \n [starting year] [ending year]")
  else:
    for row in reader:
      year = int(row[1])
      if(year>= startYear and year <= endYear):
        print(row[0])


#function which print out authors' names and books according to string in their name

def search_author(string,reader):
  namelist = []
  for row in reader:
    author = row[2]
    if(string.lower() in author.lower() and author not in namelist):
      print('\033[1m'+author+'\033[0m')
      namelist.append(author)
      with open('books.csv', newline='') as j:
        reader2 = csv.reader(j)
        for row in reader2:
          if(row[2]==author):
            print('\033[94m'+row[0]+'\033[0m')
        print('')

# prints out syntax dictionary
def help_menu():
  helpMenu= open(r"usage.txt","r")
  for row in helpMenu:
    print(row)
  helpMenu.close()
     
      
#implementation of different functions according to users' input

def main():
  reader = csv.reader(open('books.csv'))
  try:
    if(sys.argv[1] == 'h' or sys.argv[1] == 'help'  ):
      help_menu()      
    elif (sys.argv[1] == 'st' or sys.argv[1] == 'title'  ):
      try:
        string = sys.argv[2]
        print('\033[4m'+"Below are book titles containing "+string+'\033[0m')
        search_title(string,reader)
      except:
        print("Please enter the string you would like to search")

    elif(sys.argv[1] == 'sy' or sys.argv[1] == 'year'):
      try:
        startYear = int(sys.argv[2]) 
        endYear = int(sys.argv[3]) 
        print('\033[4m'+"Below are books publish between ",startYear ,"and " ,endYear,'\033[0m')
        search_year(startYear, endYear,reader)
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




  except:
    print("Please enter an operation, such as st(search books according to title), sy(search according to year), and sa(search according to author)")

main()







