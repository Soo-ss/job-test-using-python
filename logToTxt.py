for x in range(1, 10):
    print("in progress...")
    f = open("%d.log" % (x), "r")

    for line in f.readlines():
        line = line.split(" ")
        ip = line[0]

        line = " ".join(line[1:])

        # 덮어쓰기가 아니고 추가로 씀("a")
        wf = open("result\\%s.txt" % (ip), "a")
        wf.write(line)
        wf.close()

    f.close()
print("done!!")
