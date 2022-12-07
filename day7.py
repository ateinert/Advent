inputfile = "day7.txt"

class directory:
    def __init__(self,parent = None,name = "/",size = 0):
        self.setParent(parent)
        self.setName(name)
        self.size = 0
    def addSize(self,size):
        print("Set: ",self.getName(), self.getSize(), " + ",size, " = ", self.getSize() + size)
        self.size += size
        if self.parent:
            self.parent.addSize(size)
        else:
            print("EOU\n")
    def setName(self, name):
        self.name = name
    def setParent(self, parent):
        self.parent = parent
    def getName(self):
        return self.name
    def getParent(self):
        return self.parent
    def getSize(self):
        return self.size

directories = []

def main():
    filestream = open(inputfile).read()

    i = 0
    token = filestream[i]
    current_dir = None
    while i < len(filestream):
        token = filestream[i]
        if token == "$":
            # It's a command
            i += 2
            token = filestream[i]
            command = ""
            while token != "\n":
                command += token
                i += 1
                token = filestream[i]
            #print(command)
            i += 1
            token = filestream[i]
            command_bd = command.split(" ")
            if "cd" in command_bd:
                # update directory
                if command_bd[1] == "..":
                    current_dir = current_dir.getParent()
                else:
                    if current_dir:
                        current_dir = directory(parent = current_dir,name = command_bd[1], size = 0)
                    else: 
                        current_dir = directory(name = command_bd[1], size = 0)
                    directories.append(current_dir)
            elif "ls" in command_bd:
                # update directory size
                while token != "$":
                    line = ""
                    while token != "\n":
                        line += token
                        i += 1
                        if i < len(filestream):
                            token = filestream[i]
                        else:
                            token = "\n"
                    i += 1
                    if i < len(filestream):
                        token = filestream[i]
                    else:
                        token = "$"
                    line_bd = line.split(" ")
                    if line_bd[0] != "dir":
                        print(line)
                        size = int(line_bd[0])
                        current_dir.addSize(size)
                    #print (line)

    total = 0
    total_used = directories[0].getSize()
    remaining = 70000000 - total_used
    delete_size = 9999999999999999999
    for i in directories:
        print(i.getName(), i.getSize())
        if i.getSize() <= 100000:
            total += i.getSize()
        if i.getSize() >= (30000000 - remaining) and i.getSize() < delete_size:
            delete_size = i.getSize()
    print("\nTotal used: ", total_used)
    print ("Part 1: ", total)
    print ("Part 2: ", delete_size)

main()