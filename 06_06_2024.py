file = open('article.txt','r',encoding='utf-8')
def read_last(lines, file):
    print(file.readlines(lines))
read_last(60,file)

file = open('homework19.txt','r')
def fprint_docs(directory):
    print(directory.read())
fprint_docs(file)

file=open('article.txt','r',encoding='utf=8')
def longest_words(file):
    fileread=file.read()
    filereadsplit=fileread.split()
    print(max(filereadsplit,key=len))
longest_words(file)
