class dna_tools ():
    def __init__(self,file_name) :
        self.file_name = file_name
        self.dict = {}
        f_reader = open (self.file_name)
        for line in f_reader:
            line = line.strip("\n")
            if ">" in line:
                header = line
                self.dict[header] = ""
            else:
                self.dict[header] = ""
        f_reader.close
    
    def count_records(self):
        number_of_records = len(self.dict)
        print(number_of_records)
    