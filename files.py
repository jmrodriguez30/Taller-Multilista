class Files():
    def read_file(path):
        with open (path,"r") as file:
            line1 = file.readline() # Reads the first line
            print(line1.strip())