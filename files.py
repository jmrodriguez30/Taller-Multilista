class Files:
    @staticmethod
    def read_file(path):
        with open(path, "r", encoding="utf-8") as file:
            line1 = file.readline()  # Reads the first line
            print(line1.strip())
