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
        start_code = "ATG"
        stop_codes = ["TAA", "TAG", "TGA"]
        pos_dict = {}
        for i in range(3):
            pos = []
            if i == 0 :
                frame = [dna[j:j+3] for j in range(i, len(dna), 3)]
            else:
                frame = [dna[:i]] + [dna[j:j+3] for j in range(i, len(dna), 3)]
            start_pos = []
            stop_pos = []
            try:
                index_start_pos = [m for m, y in enumerate(frame) if \
                                  y == start_code]
                start_pos += index_start_pos
            except ValueError:
                pos.append((-1, 0))
                continue

            for stop_code in stop_codes:
                try:
                    index_stop_code = [n for n, x in enumerate(frame) if \
                                       x == stop_code and n > min(start_pos)]
                    stop_pos += index_stop_code
                except ValueError:
                    continue
            if len(stop_pos) == 0:
                pos.append((-1, 0))