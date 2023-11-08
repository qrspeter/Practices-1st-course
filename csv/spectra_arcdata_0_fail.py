import pdb
spectra = []
with open('WingsMPA_633ex_1mmslit.arc_data', 'r', encoding='cp1251') as fin:
    for line in fin:
        if len(line) == 0:
            break
        if (line[0] != '#') and (line != '\n'):
            l_line = line.split('\t')
            l1 = []
            pdb.set_trace()
            l1.append(l_line[0])  #.strip()
            l1.append(l_line[1])  #.strip()
          #  point = [float for x in line.split('\t')]
            
            spectra.append(l1)



print(spectra)
