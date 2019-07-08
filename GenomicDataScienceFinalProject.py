class dna_tool_sets ():

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
        record_max_length = [item for item in length_dict if length_dict[item] == max_length]
        # identifier of sequences with min length        
        record_min_length = [item for item in length_dict if length_dict[item] == min_length]
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
        pairs = {"A": "T", "C": "G", "G": "C", "T": "A"}
        c_dna = [pairs[s] for s in dna]
        return "".join(c_dna)[::-1]

    def orf_identifier (self):
        orf = {}
        for header, dna_seq in self.dict.items(): # generate orf for the whole file
            pos = self.find_pos(dna_seq)
            orf[header] = pos
        # find header for question 7
        id_key = [key for key in orf if "gi|142022655|gb|EQ086233.1|129" in key]
        idx = id_key[0]  
        # generate list of frames for questions 4 to 7
        frame1, frame2, all_frames, id_frames = [], [], [], []
        for key, dict_value in orf.items():
            frame1 += dict_value["frame1"]
            frame2 += dict_value["frame2"]
            frames = dict_value["frame1"] + dict_value["frame2"] + dict_value["frame3"]
            all_frames += frames
            if key == idx:
                id_frames = dict_value["frame1"] + dict_value["frame2"] + dict_value["frame3"]
            
        #Q4: What is the length of the longest ORF appearing in reading
        #frame 2 of any of the sequences?
        frame2_max_length = max(frame2, key = lambda x: x[1])
        print "Q4: The length of longest ORF in frame2: %d\n"%frame2_max_length[1]
        #Q5: What is the starting position of the longest ORF in reading frame 1 
        #in any of the sequences? 
        
        frame1_max_length_pos = max(frame1, key = lambda x: x[1])
        print "Q5: The start position of longest ORF in frame1: %d\n"%frame1_max_length_pos[0]
        #Q6: What is the length of the longest ORF appearing in any sequence and 
        #in any forward reading frame?
        max_length = max(all_frames, key = lambda x: x[1])
        print "Q6: The longest ORF of all frames and sequences: %d\n"%max_length[1]
        #Q7: What is the length of the longest forward ORF that appears in the 
        #sequence with the identifier gi|142022655|gb|EQ086233.1|129?

        max_length_id = max(id_frames, key = lambda x: x[1])
        print "Q7: The length of longest ORF for ", idx, "is: %d \n" %max_length_id[1]
        
        # uncomment the return code to return the whole orf information 
        #including starting position and length of each frame for each sequence
        
        #return orf

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

if __name__ == "__main__":
    
    file_name = "dna.example.fasta"
    dna_tools = dna_tool_sets (file_name)
    # Q1: How many records are in the multi-FASTA file?
    dna_tools.count_records()
    
    # Q2: What is the length of the longest sequence in the file?
    # Q3: What is the length of the shortest sequence in the file?
    dna_tools.check_length()
    
    #Q4: What is the length of the longest ORF appearing in reading
    #frame 2 of any of the sequences?
    #Q5: What is the starting position of the longest ORF in reading frame 1 
    #in any of the sequences? 
    #Q6: What is the length of the longest ORF appearing in any sequence and 
    #in any forward reading frame?
    #Q7: What is the length of the longest forward ORF that appears in the 
    #sequence with the identifier gi|142022655|gb|EQ086233.1|129?
    dna_tools.orf_identifier()
    
    # Q8:Find the most frequently occurring repeat of length 7 in all 
    # sequences. How many times does it occur in all?
    # Q10:Which one of the following repeats of length 7 has a maximum 
    #number of occurrences?
    dna_tools.repeats_identifier(7)
    
    # Q9:Find all repeats of length 10 in the input file. Let's use Max to 
    #specify the number of copies of the most frequent repeat of length 10. 
    #How many different 10-base sequences occur Max times?
    dna_tools.repeats_identifier(10)