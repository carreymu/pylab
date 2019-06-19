if __name__ == "__main__":
    items = [0, 1, 2, 3, 4, 5, 6]
    print("inititem is ", items)
    a = slice(2,4)
    print("slice result:",a)
    #[2,4)
    print(items[2:4])
    print(items[a])
    items[a] = [10,11]
    print("item is ", items)
    del items[a]
    print("after del item[a]", items)

    print("========================")
    s = slice(5, 50 ,2)
    print("s is ", s)
    print("s.start is ",s.start)
    print("s.stop is ", s.stop)
    print("s.step is ", s.step)
    print("========================")
    hel = 'HelloWorld12'
    print("hel is ", hel)
    hela = s.indices(len(hel))
    print("hela is ", hela)
    for i in range(*s.indices(len(hel))):
        print("hel[%d] is %s" %(i,hel[i]))

