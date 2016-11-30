from LinkedStack import LinkedStack

x = LinkedStack()

x.push(10)
x.push(25)
x.push(55)


for i in range(x.size - 1, -1, -1):

    print '|', x.data[i].get_element(), '|' ,
    #next object

    if x.data[i].get_next() == None:
        print '--> None'
    else:
        print  x.data[i].get_next().get_element(), '-|---->  ',

