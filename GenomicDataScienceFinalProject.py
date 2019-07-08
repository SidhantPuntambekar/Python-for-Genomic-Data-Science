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
             else:
                 while len(start_pos) != 0:
                     start = min(start_pos)
                     try:
                        end = min([stop for stop in stop_pos if stop > start])
                     except ValueError:
                        break
                    s_pos = len("".join(frame[:start])) + 1
                     pos.append((s_pos, (end - start + 1)*3))
                     start_pos.remove(start) 
            pos_dict["frame%d"%(i+1)] = pos 
            
        return pos_dict

    def reverse_complement(dna):
        pairs = {"A":"T":"C":"G", "G":"C":"T":"A"}
        c_dna = [pairs[s] for s in dna]
        return "".join(c_dna)[::-1]

    def orf_identifier (self):
        orf = {}
        for header, dna_seq in self.dict.items(): 
            pos = self.find_pos(dna_seq)
            orf[header] = pos
        
        id_key = [key for key in orf if "gi|142022655|gb|EQ086233.1|129" in key]
        idx = id_key[0]  
        
        frame1, frame2, all_frames, id_frames = [], [], [], []
        for key, dict_value in orf.items():
            frame1 += dict_value["frame1"]
            frame2 += dict_value["frame2"]
            frames = dict_value["frame1"] + dict_value["frame2"] + dict_value["frame3"]
            all_frames += frames
            if key == idx:
                id_frames = dict_value["frame1"] + dict_value["frame2"] + dict_value["frame3"]    
        frame2_max_length = max(frame2, key = lambda x: x[1])
        print(frame2_max_length[1])
        frame1_max_length_pos = max(frame1, key = lambda x: x[1])
        print(frame1_max_length_pos)
        max_length = max(all_frames, key = lambda x: x[1])
        print(max_length)
        max_length_id = max(id_frames, key = lambda x: x[1])
        print(max_length_id)

    def find_repeats(self, dna, n):
        repeats_set = {}
        for header, dna_seq in self.dict.items():
            repeats = self.find_repeats(dna_seq, n)
            repeats_set[header] = repeats
        combined_repeats = {}
        for dict_value in repeats_set.values():
            for key in dict_value:
                if key not in combined_repeats:
                    combined_repeats[key] = dict_value[key]
                else:
                    combined_repeats[key] = combined_repeats.get(key) \
                                            + dict_value[key]
        if n == 7:
            most_freq_7 = max (combined_repeats.values())
            print("Q8: The most frequently repeats occur: %d times \n"%most_freq_7)
            most_freq_7_seq = [key for key in combined_repeats if \
                       combined_repeats[key] == max(combined_repeats.values())]
            print ("Q10: The following repeats occured most frequently: \n", most_freq_7_seq)
        if n == 10:
            count_most_freq_10 = len([value for value in combined_repeats.values()\
                             if value == max(combined_repeats.values())])
            print "Q9: The number of different 10-base sequences occur max times: %d \n"\
                  %count_most_freq_10