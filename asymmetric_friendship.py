import sys
import MapReduce

mr=MapReduce.MapReduce()

def mapper(record):
    personA = record[0]
    personB=record[1]
    mr.emit_intermediate(personA,personB)

def reducer(personA,list_of_friends):
    
    for friend in list_of_friends:
        if friend not in mr.intermediate.keys() or personA not in mr.intermediate[friend]:
            mr.emit((personA,friend))
            mr.emit((friend,personA))
       
def main():
    data = sys.argv[1]
    inputw = open(data)
    mr.execute(inputw,mapper,reducer)

if __name__=='__main__':
     main()


