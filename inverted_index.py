import MapReduce
import sys

mr=MapReduce.MapReduce()

def mapper(record):
    key = record[0]
    value=record[1]
    token = value.split()
    for word in token:
        mr.emit_intermediate(word,key)
        

def reducer(key,terms):
    terms = list(set(terms))
    mr.emit((key,terms))

def main():
    data= sys.argv[1]
    inputw = open(data)
    mr.execute(inputw,mapper,reducer)

if __name__=='__main__':
     main()
        

