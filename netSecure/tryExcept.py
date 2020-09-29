for x in range(1, 10):
    try:
        f = open("%s.log" % x, "r")
        data = f.read()
        f.close()
        print(x)
    except:
        continue