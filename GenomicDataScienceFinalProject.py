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
    
    def check_length(self):
        length_dict = {}
        for key,value in self.dict.items():
            length_dict[key] = len(value)
        
        lengths = length_dict.values()
        max_length = max(lengths)
        min_length = min(lengths)
        record_max_length = [item for item in length if length_dict[item] == max_length]
        record_min_length = [item for item in length if length_dict[item] == min_length]
        print(record_max_length)
        print(record_min_length)
    
    def find_pos(self,dna):
        