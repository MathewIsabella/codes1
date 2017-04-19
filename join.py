import sys
import MapReduce
import itertools

mr=MapReduce.MapReduce()

def mapper(record):
    key = record[1]
    mr.emit_intermediate(key,record)


def reducer(key,list_of_values):
    order_ID = list_of_values[0]
    LineItem = list_of_values[1:]

    for line  in LineItem:
        mr.emit(order_ID +line)


def main():
    data = sys.argv[1]
    inputw=open(data)
    mr.execute(inputw,mapper,reducer)

if __name__=='__main__':
     main()

