######################
# Import libraries
######################

from altair.vegalite.v4.schema.channels import Color
import pandas as pd
import streamlit as st
import altair as alt
import time

from streamlit.proto.Markdown_pb2 import Markdown
#from PIL import Image

######################
# Page Title
######################

#image = Image.open('dna-logo.jpg')

#st.image(image, use_column_width=True)

st.sidebar.header("WELCOME👋 TO DNA DEPICTION WEB APP")

rad = st.sidebar.radio(
    "Hii select from⬇️", ["ABOUT ME", "THE DNA TEST", "TEST CASES"])

if rad == "ABOUT ME":
    st.write("""
    # DNA Depiction Web App using Nucleo Celltide Count
    ___
    ### About The Project:
    Every Human DNA Consists of Nucleotide Cells Composition. The Four basic Nucleotides that are available in the DNA are 
    - Adenine - A
    - Thymene - T
    - Guyanine - G
    - Cytosine - S
    

    ![image](https://raw.githubusercontent.com/Gouthique/Data/main/Streamlit/Pictures/DNA.jpg)
    
    - 📌 This app Analyses counts the nucleotide composition of query DNA! 
    - 📌 The important application of this app is in Crime Investigation.
    ___
    
    ## ✨Developed By✨:
    - ### Name:- V. MANI CHANDANA 
    - ### Rollno:- 18671A1954 
    - ### Branch:- Department Of _Electronics and Computer Engineering_
    - ### College:- J.B Institute Of Engineering & Technology
    ___

    """)


######################
# Input Text Box
######################

if rad == "THE DNA TEST":
    #st.sidebar.header('Enter DNA sequence')
    st.header('Enter The Evidence DNA sequence')

    sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

    #sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
    sequence = st.text_area("Sequence input", sequence_input, height=250)
    sequence = sequence.upper()
    sequence = sequence.splitlines()
    sequence = sequence[1:]  # Skips the sequence name (first line)
    sequence = ''.join(sequence)  # Concatenates list to string

    st.write("""
    ___
    """)

    # Prints the input DNA sequence
    st.header('INPUT (Evidence DNA Query)')
    sequence

    # DNA nucleotide count
    st.header('OUTPUT (DNA Nucleotide Count)')

    # 1. Print dictionary
    st.subheader('1. Print dictionary')

    def DNA_nucleotide_count(seq):
        d = dict([
            ('A', seq.count('A')),
            ('T', seq.count('T')),
            ('G', seq.count('G')),
            ('C', seq.count('C'))
        ])
        return d

    X = DNA_nucleotide_count(sequence)

    #X_label = list(X)
    #X_values = list(X.values())

    X

    # 2. Analysing The DNA Sequence
    st.subheader('2. Analysing The Evidence DNA Sequence')
    st.warning('There are  ' + str(X['A']) + ' adenine (A)')
    st.error('There are  ' + str(X['T']) + ' thymine (T)')
    st.success('There are  ' + str(X['G']) + ' guanine (G)')
    st.info('There are  ' + str(X['C']) + ' cytosine (C)')

    Vic_A = int(str(X['A']))
    Vic_T = int(str(X['T']))
    Vic_G = int(str(X['G']))
    Vic_C = int(str(X['C']))

    # 3. Display The DataFrame
    st.subheader('3. Display The DataFrame')
    df = pd.DataFrame.from_dict(X, orient='index')
    df = df.rename({0: 'count'}, axis='columns')
    df.reset_index(inplace=True)
    df = df.rename(columns={'index': 'nucleotide'})
    st.write(df)

    # 4. Visualization of The DNA NCC
    st.subheader('4. Visualization of The DNA NCC')
    p = alt.Chart(df).mark_bar().encode(
        x='nucleotide',
        y='count'
    )
    p = p.properties(
        width=alt.Step(80)  # controls width of bar.
    )
    st.write(p)
    st.subheader('5. The match Counts For Investigation of Suspects are:')

    st.write(' adenine (A) = ' + str(X['A']))
    st.write(' thymine (T) = ' + str(X['T']))
    st.write(' guanine (G) = ' + str(X['G']))
    st.write(' cytosine (C) = ' + str(X['C']))
    '''
    ### Note: If the Supect Has the Same Count of As The Above match Count then he is the Culprit⚠️
    '''

    # _______________________________________________________________________________________________
    # _______________________________________________________________________________________________
    # _______________________________________________________________________________________________
    # _______________________________________________________________________________________________
    st.write("""___""")
    st.header('Enter The Suspect DNA sequence')

    sequence_input_SUS = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
    #sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
    sequence2 = st.text_area("Sequence input2", sequence_input_SUS, height=250)
    sequence2 = sequence2.upper()
    sequence2 = sequence2.splitlines()
    sequence2 = sequence2[1:]  # Skips the sequence name (first line)
    sequence2 = ''.join(sequence2)  # Concatenates list to string

    st.write("""
    ***
    """)
    st.write("""
    ___
    """)
    # Prints the input DNA sequence
    st.header('INPUT (Suspect #1 DNA Query)')
    sequence2

    # DNA nucleotide count
    st.header('OUTPUT (DNA Nucleotide Count)')

    # 1. Print dictionary
    st.subheader('1. Print dictionary')

    def DNA_nucleotide_count(seq2):
        d = dict([
            ('A', seq2.count('A')),
            ('T', seq2.count('T')),
            ('G', seq2.count('G')),
            ('C', seq2.count('C'))
        ])
        return d

    Y = DNA_nucleotide_count(sequence2)

    #X_label = list(X)
    #X_values = list(X.values())

    Y

    # 2. Analysing The DNA Sequence
    st.subheader('2. Analysing The Suspect #1 DNA Sequence')
    st.error('There are  ' + str(Y['A']) + ' adenine (A)')
    st.warning('There are  ' + str(Y['T']) + ' thymine (T)')
    st.success('There are  ' + str(Y['G']) + ' guanine (G)')
    st.info('There are  ' + str(Y['C']) + ' cytosine (C)')

    Sus_A = int(str(Y['A']))
    Sus_T = int(str(Y['T']))
    Sus_G = int(str(Y['G']))
    Sus_C = int(str(Y['C']))

    # 3. Display The DataFrame
    st.subheader('3. Display The DataFrame')
    df = pd.DataFrame.from_dict(Y, orient='index')
    df = df.rename({0: 'count'}, axis='columns')
    df.reset_index(inplace=True)
    df = df.rename(columns={'index': 'nucleotide'})
    st.write(df)

    # 4. Visualization of The DNA NCC
    st.subheader('4. Visualization of The DNA NCC')
    p = alt.Chart(df).mark_bar().encode(
        x='nucleotide',
        y='count'
    )
    p = p.properties(
        width=alt.Step(80)  # controls width of bar.
    )
    st.write(p)
    st.subheader('5. The match Counts For Investigation of Suspects are:')

    st.write(' adenine (A) = ' + str(Y['A']))
    st.write(' thymine (T) = ' + str(Y['T']))
    st.write(' guanine (G) = ' + str(Y['G']))
    st.write(' cytosine (C) = ' + str(Y['C']))

    st.write(""" ``` """)

    result = st.button("CLICK HERE TO GET THE TEST RESULTS")

    if result:
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.05)
            progress.progress(i+1)
        if ((Vic_A == Sus_A) and (Vic_C == Sus_C) and (Vic_G == Sus_G) and (Vic_T == Sus_T)):
            st.error(
                "The Evidence DNA Match count perfectly matches to Suspect #1's DNA Count So \n\n ⚠️ SUSPECT #1 IS THE CULPRIT ⚠️")
        else:
            st.success(
                "The Evidence DNA Match count doest not matches to Suspect #1's DNA Count So \n\n 😇 SUSPECT #1 IS INNOCENT 😇")

if rad == "TEST CASES":
    st.write(
        """
        # Test Case:1 - 1000 Sequence
        ### Evidence - 1000 Sequence
        ```
        tcgagaatagattgtcgagccgcaaggcccggcagaaagcattaatagctcgctgccacc
        aaagtgtggggctagacgctaaagggccgcacctcagattaccacaaaatttggaataat
        tacggattaaataggtagaccggcgtccccgggcccctgcgctgtatcttatggttcctc
        tcaacacgagatttaccggtttcaagcccggccgacataagtgagggctgggacaggaga
        ccatcgcttaagattcgataacatgaggcaaatgcccgtgtgagcgtgaatgggctcgct
        cggcacctgctcccaacccacgaaagacttgcggcatgcattgccttttgacacactcgt
        ccagtacgttctacctggcatagtgtgatatctcaacagctgggtattcccgactcatag
        ctagcacaggaccgggtccgacacgtcggtcttctcagacgtgacgagtgcagcttgact
        aggggaccgcgaccggggtcctcatctccgacgcctgtcagaaccgatgcatgtagccct
        catccgcagaacatcgcattggctacgctgctatcactgcgattggagctagtttgaggg
        aagacatcccggccattccatcttccctcgaaccaggagctccgcagcagctcacaaaag
        gcgacgcccattccttcatctgaggtaatagtgcctgcgtggacccaaatgtgactatga
        ccaatgggtcttgcagcatggaacccctgttgggccccctaagtggaagtttacgagagg
        cgacgatagtcgcgatcgcaaatagccctagtagtacactcaattccactcggtcgtgcc
        gttggaatcctctagagaccaggtctcgacagtagggaggtgtgactgaatcctggctgt
        tgaacaagttttggcggagacatgacccacagatgacaacgactgtaccgatctggaagc
        aacgcgggaaacgatccaagtttcgaaatggcgtgcgccc
        ```
        ### Suspect - 1000 Sequence
        ```
        acctgctttgaactgaggacggtcctgcgaagactctcacagggcttgtcatggcaactc
        ggagtggggctcttatacgaggtgcgtctagccatctaaagctataatgtttactagatc
        tatccggtattatagcggcgtaagcttaatgcgcaaactagtcctctggatttcacatat
        agatcaaggctctgatcagataatctaaaaagtgagcgaacctcacaacagcgtacgaca
        tggttcagtgactctctaccgtttcacacgcctgataagccactgttgctccccctcggt
        tgttatgagtactggtactcattggtttcatgaggtccactaacgacttgattttacgat
        gcgcgagttggtttgggagggtcgctccacctgctccttgatttcctgaagctactgaat
        accgggcaagcaacaaaatggggaggaagctttcctggtagggcgcctggtatcattctc
        tttaaggtgcattggctagctatgtgcggagactgactcagtctgaaccatatgtccggg
        tggtgggggagaccacgccagtcacccataagtgtctatagtgcatcaaaacgccgaata
        ggtggattactgtatcgatcgcgatgcgcatcgaacaaggtcctccggtttcgttttaaa
        aggtcagccgcttaattccacccgactcaacgagtgtccgtgctcgaacacgtataataa
        catttttatcaccgggcaacgctggccagtacccatgagtaaacgtgcaatcatattagt
        tacctaccctctatctttctcgcctcgcagaaacatggggttaaaagacccactgtcacc
        cccacgtggctatttctcgtcccacactagtccaatatgcactctcaggggtgatccgaa
        tgcgctttctcaataacagaaatatagaaagggtcacttgcaacctactagacaaggtgt
        aggccactttgttacctgtgccggggtcctcaactaccac
    """)
    st.write(
        """
        # Test Case:2 - 5000 Sequence
        ### Evidence - 5000 Sequence
        ```
        tgttcagcacacacagggatggctgatgtcgaaaagatgacttacctgacgaactgagcc
        aatttatcttattttcagagaatcccctggagtgatatatgtcaacgatgatacaatttg
        aaacacggatgtagcgacgccgggtcaatcgatgtcgccaaagacctggtccgtgcgaaa
        gatcacggacccgctctgccacgatacgaccgccctgagcgtattcatgtcctatacgat
        cacattactgttatctgtaggtcctttcagaggcatgcaaaaccggtagtaaaacgggcc
        cgagtgatactagtacagcgaattgacgggaagtatccagaatgcgaagatcattgaggt
        cgctcagctcttcgccgccagcttacaacttcgtagcgttttcaacgcagcccaagcagt
        cctggtgcctaggacgttgatcttactccgtgacgccctcactttgagggtaaatcaaac
        catacaattcaatacgaccgccaacttacgtcacggttttgtagtttgggaacggggttg
        tgtcaagcctcggagccgaacgtcctgaatccctatcgcgcaacgcacgcatgatagtgc
        atggtccgtaattaggattataagttccacttgtatgcaacgcgcaaccgggaaggtagc
        gtgggaattgggcccgacgcatttaggtgcgctcacaatcgacgtggctcctcgacgtag
        ttgttgcgggcttagtcttacgctacgggcctgccaggtccggattgccggcggtaagac
        gctccgcaccgaaccggggacagatcacttaaattaaacagaggacgtcgtttgtccgcc
        aatatcgacctgcgctaaatgaatagggagaagcacttaagtgcacaggacctgaggcgg
        acacatgtacgggaatggacagtctcgtaactgtgtcgaaagttctttaactggcgatgg
        ctactgcaggatcgacgccacctgtcctcgaagcaatgggtcggcccccagcttgttttt
        aatagtacacatccccacgtgccgttataggacacaagccacggcaaatgcgcggttgac
        ttacatggacctatttcgcactgatttggaccgaactacggcttgagccagttcttccag
        taagtgcacgtgatccctaggtaattcttacgccttaatccggtacgggtttagctaggc
        gctgcccttagcacccgagcattacagcgcggtgtcgcgactctataggcacatacggtg
        ccccgtagccccttcgacctagacaatcagctgtaatttttcgtcagactaaacgaacca
        atcccagtaggattcgttcctgcagtagagccacagaagtaagagtattcaggtttgagt
        tgtcatctgggcttctgcgcggacgaggggatccgcctcgtgatctacgaggtgcataca
        atataagcagagggctcgcgacttatctgttggattcagatattcggatgagcgaattct
        tgccgaagtgggacggctcagagagttacacagcccggtttactatttcagcagttaggt
        cacacgacatggtgttcgtgcgagtaaccacaggctagactgtgtcacctacactaagtt
        atttctagttattactccgatcactggcggtgccctttagacactcctgatcggacgtgc
        tgacatcattatagtctagtcgaacatctagatctctcccgaactgctaaatgtctacat
        tgcggttcgtcatgatcgttaaacagtagaatggaccacgccaccaccgcctcgtattac
        ttcgtattcccgttcttagctcctgataactcgaccagggattttgaggcgtcgccggct
        ttcggaattactcctacccaggtaaggagtttgaaggctgtcgggttatatgctctgtca
        atataacttttgcagagacagtcttcactaggcgctccaataactgctagccttctgctg
        gcaaaaacctcaatttgcaaggtcccgtggacagagagggcgaggtcgaagaacggtccc
        ctccatacgacattgcctatcaagaaacaggatcagcaatagcgctgtacgccatagtcg
        ctaaacacgggcatattctccttgccccagctgaggagcgtggtattacagatgtaccaa
        tctaataataaggcacgtatgtaatcgaagacaacagtttaccacatagcgctacttttg
        accagcagccatataaaccatctctttccatgcgcttagctcggaccgggacgcgatgag
        ccacaccgctcagatggtaagttgctctcggttttgcgagtgcccacagaaagtcctcgg
        gaaaccctggaccctgacttgtgcacttgcatacagaagatcaatgcgacctctacggct
        aaattcgttatgctcctacacctttatcacatcggcagactatcaaggtttccgcggtct
        cgccttcgtaacgcaaccttccgtaggaacaattactcgacgccggttgatccgcactgt
        aaaagagccccgctggaattgactcatcctcgtgtctcggttcggtaaagaggttgaaag
        ctgatttagcaatagaatacccacgaaggcattttatccggaggccgacatgtttggcca
        gtaaattaaatgtaccttgtcagggggctagatcggccacggtctagtaacgtgctttct
        acttcgcttcatagtcagactaaaacctcaggcgaattttacggcatgcaccagacaggc
        agtcgaacgcggttgaaacctcaccgcccatcgtgtaaaggcgcctgcgctttataacta
        attccgcagacgagattggcgggtctcgtcgttcgtggacattaggtgagttgggaggcc
        cggagggcttgaggccacttacttgggtgaatgagaaagtacgctaatcgacgtggttat
        gcaagtgcaattggcacctgtgcccccccccagcgatttacgctaaatttcgatcgtcga
        catcagtaacaccgctatgagcttaataggcgacaatatccttttaaattacacccgaga
        cctgccattttctgccacgaggtttgcgagttcgtatagtgcgagccaatgccacctatt
        gccgcggcataccttaagtttcattcgatggtctggtgcacctccccggaggattgttaa
        aaatgtaatcgaccaaggctattccggtctcatttactaggtgcccgtaatgcgatcagt
        ggctattatacagcggaacccaagggctccgatttgtaggtggaaagcctatttatctac
        tgccaggaggggtttgaccaggcatcacctcgaactcagaaacatcatctttcctgcctg
        agcgtgacacgagcagccttgacaactagtatgcggacttatctgttacaaacccaggaa
        gtaaatataagccctgctaatgtgtcttgtttacgctttgagctggtttcaccctgccgc
        cagtaactagtattctagaggactcttcagaaagcgactaaatcgctaacgtaaagatat
        aatctctctccgaagggcacagactctaggcgtcaaagctacttattctcaatacggtgt
        gctgatattggcagaagagctcgcactaacgaagctaaactcctgtccgatggagattac
        ctaaatttcgtatgactcacagaaactcacatagactagcggattccttgtagtcctgtt
        gctagccccgggcctgtctcgtcgttcgatcgtaactgttcctcttgccccgaacacgga
        ctgttggcaagaccggcgagaacttgtccgactttccacggaaactctgtgcgtactttt
        tgggctcaagcttaatagcagttgaagcacagtgccagtacgttttcattagcactatcc
        gatcttgttcagtcgaagttgaatggctaaggacacacccaaatgcaggatggcgatggg
        aagaagtctcttcgtatcgaaccatccccttagcccttgtgcggtcctattttccacacc
        agcctcagacacttcaacggtccagcatgtgcagcaaggacttctccgcgcttaggaacg
        ccgcgtggcgtccagtccaaacgctttcttggtccgatctcttggtgttaatacgcgacc
        gcctacgcgtcattaggcatagtgctacgcacggcacgcaatattggtcgtcgcgaccag
        gcggtcttgttatgttctaggcgatctcgctgagttcctgatgaggggtggtcccttcaa
        cgttcatacgtgccttgtctgaagggtgcagacgggagaatggcaaagagtatgggtaaa
        cttcacgctaccgcggggtgcaaaaatacaaagtttcgcccaatagatatgcacttccag
        gtacaccgatgaaactcggtaataaccccaaacgaatattcttatctgtcgaactagagc
        gtactcccggccccttagaaccaccgacataatgagaccaatttgcggctagtccttctc
        gaaacttggtttcgacggtttaatagagtactagggccggatcgcccgagcgtacggtga
        cactactggtcctgtaagaccgggtcccagttcgcgaaaacctctcggatacactagagt
        ttgagataatggatggcacgagtcgccctacgtcctgggttaagatactgacgagcaatc
        gcccatcgtccgtgctagcgtggctaatttgtgcccagtaacttacgacgcgaagtttgc
        ccgcccttcccaagggcccgacgggcggacgcagacacattgaaaaacctaggtccgctt
        cctactcggtatttgcggtcttgagggcccgagatcttcaagagggctatattcgttgga
        ctgctcacatagcaaccagcgccagcgttgactcgcctcgtgtagcttgttcaggcggac
        aatatgggtacaatttaggaacgatgtatttggtcgtctgataactttatatccaagggg
        cgggtagcgtcatgagctgg
        ```
        ### Suspect - 5000 Sequence
        ```
        tgttcagcacacacagggatggctgatgtcgaaaagatgacttacctgacgaactgagcc
        aatttatcttattttcagagaatcccctggagtgatatatgtcaacgatgatacaatttg
        aaacacggatgtagcgacgccgggtcaatcgatgtcgccaaagacctggtccgtgcgaaa
        gatcacggacccgctctgccacgatacgaccgccctgagcgtattcatgtcctatacgat
        cacattactgttatctgtaggtcctttcagaggcatgcaaaaccggtagtaaaacgggcc
        cgagtgatactagtacagcgaattgacgggaagtatccagaatgcgaagatcattgaggt
        cgctcagctcttcgccgccagcttacaacttcgtagcgttttcaacgcagcccaagcagt
        cctggtgcctaggacgttgatcttactccgtgacgccctcactttgagggtaaatcaaac
        catacaattcaatacgaccgccaacttacgtcacggttttgtagtttgggaacggggttg
        tgtcaagcctcggagccgaacgtcctgaatccctatcgcgcaacgcacgcatgatagtgc
        atggtccgtaattaggattataagttccacttgtatgcaacgcgcaaccgggaaggtagc
        gtgggaattgggcccgacgcatttaggtgcgctcacaatcgacgtggctcctcgacgtag
        ttgttgcgggcttagtcttacgctacgggcctgccaggtccggattgccggcggtaagac
        gctccgcaccgaaccggggacagatcacttaaattaaacagaggacgtcgtttgtccgcc
        aatatcgacctgcgctaaatgaatagggagaagcacttaagtgcacaggacctgaggcgg
        acacatgtacgggaatggacagtctcgtaactgtgtcgaaagttctttaactggcgatgg
        ctactgcaggatcgacgccacctgtcctcgaagcaatgggtcggcccccagcttgttttt
        aatagtacacatccccacgtgccgttataggacacaagccacggcaaatgcgcggttgac
        ttacatggacctatttcgcactgatttggaccgaactacggcttgagccagttcttccag
        taagtgcacgtgatccctaggtaattcttacgccttaatccggtacgggtttagctaggc
        gctgcccttagcacccgagcattacagcgcggtgtcgcgactctataggcacatacggtg
        ccccgtagccccttcgacctagacaatcagctgtaatttttcgtcagactaaacgaacca
        atcccagtaggattcgttcctgcagtagagccacagaagtaagagtattcaggtttgagt
        tgtcatctgggcttctgcgcggacgaggggatccgcctcgtgatctacgaggtgcataca
        atataagcagagggctcgcgacttatctgttggattcagatattcggatgagcgaattct
        tgccgaagtgggacggctcagagagttacacagcccggtttactatttcagcagttaggt
        cacacgacatggtgttcgtgcgagtaaccacaggctagactgtgtcacctacactaagtt
        atttctagttattactccgatcactggcggtgccctttagacactcctgatcggacgtgc
        tgacatcattatagtctagtcgaacatctagatctctcccgaactgctaaatgtctacat
        tgcggttcgtcatgatcgttaaacagtagaatggaccacgccaccaccgcctcgtattac
        ttcgtattcccgttcttagctcctgataactcgaccagggattttgaggcgtcgccggct
        ttcggaattactcctacccaggtaaggagtttgaaggctgtcgggttatatgctctgtca
        atataacttttgcagagacagtcttcactaggcgctccaataactgctagccttctgctg
        gcaaaaacctcaatttgcaaggtcccgtggacagagagggcgaggtcgaagaacggtccc
        ctccatacgacattgcctatcaagaaacaggatcagcaatagcgctgtacgccatagtcg
        ctaaacacgggcatattctccttgccccagctgaggagcgtggtattacagatgtaccaa
        tctaataataaggcacgtatgtaatcgaagacaacagtttaccacatagcgctacttttg
        accagcagccatataaaccatctctttccatgcgcttagctcggaccgggacgcgatgag
        ccacaccgctcagatggtaagttgctctcggttttgcgagtgcccacagaaagtcctcgg
        gaaaccctggaccctgacttgtgcacttgcatacagaagatcaatgcgacctctacggct
        aaattcgttatgctcctacacctttatcacatcggcagactatcaaggtttccgcggtct
        cgccttcgtaacgcaaccttccgtaggaacaattactcgacgccggttgatccgcactgt
        aaaagagccccgctggaattgactcatcctcgtgtctcggttcggtaaagaggttgaaag
        ctgatttagcaatagaatacccacgaaggcattttatccggaggccgacatgtttggcca
        gtaaattaaatgtaccttgtcagggggctagatcggccacggtctagtaacgtgctttct
        acttcgcttcatagtcagactaaaacctcaggcgaattttacggcatgcaccagacaggc
        agtcgaacgcggttgaaacctcaccgcccatcgtgtaaaggcgcctgcgctttataacta
        attccgcagacgagattggcgggtctcgtcgttcgtggacattaggtgagttgggaggcc
        cggagggcttgaggccacttacttgggtgaatgagaaagtacgctaatcgacgtggttat
        gcaagtgcaattggcacctgtgcccccccccagcgatttacgctaaatttcgatcgtcga
        catcagtaacaccgctatgagcttaataggcgacaatatccttttaaattacacccgaga
        cctgccattttctgccacgaggtttgcgagttcgtatagtgcgagccaatgccacctatt
        gccgcggcataccttaagtttcattcgatggtctggtgcacctccccggaggattgttaa
        aaatgtaatcgaccaaggctattccggtctcatttactaggtgcccgtaatgcgatcagt
        ggctattatacagcggaacccaagggctccgatttgtaggtggaaagcctatttatctac
        tgccaggaggggtttgaccaggcatcacctcgaactcagaaacatcatctttcctgcctg
        agcgtgacacgagcagccttgacaactagtatgcggacttatctgttacaaacccaggaa
        gtaaatataagccctgctaatgtgtcttgtttacgctttgagctggtttcaccctgccgc
        cagtaactagtattctagaggactcttcagaaagcgactaaatcgctaacgtaaagatat
        aatctctctccgaagggcacagactctaggcgtcaaagctacttattctcaatacggtgt
        gctgatattggcagaagagctcgcactaacgaagctaaactcctgtccgatggagattac
        ctaaatttcgtatgactcacagaaactcacatagactagcggattccttgtagtcctgtt
        gctagccccgggcctgtctcgtcgttcgatcgtaactgttcctcttgccccgaacacgga
        ctgttggcaagaccggcgagaacttgtccgactttccacggaaactctgtgcgtactttt
        tgggctcaagcttaatagcagttgaagcacagtgccagtacgttttcattagcactatcc
        gatcttgttcagtcgaagttgaatggctaaggacacacccaaatgcaggatggcgatggg
        aagaagtctcttcgtatcgaaccatccccttagcccttgtgcggtcctattttccacacc
        agcctcagacacttcaacggtccagcatgtgcagcaaggacttctccgcgcttaggaacg
        ccgcgtggcgtccagtccaaacgctttcttggtccgatctcttggtgttaatacgcgacc
        gcctacgcgtcattaggcatagtgctacgcacggcacgcaatattggtcgtcgcgaccag
        gcggtcttgttatgttctaggcgatctcgctgagttcctgatgaggggtggtcccttcaa
        cgttcatacgtgccttgtctgaagggtgcagacgggagaatggcaaagagtatgggtaaa
        cttcacgctaccgcggggtgcaaaaatacaaagtttcgcccaatagatatgcacttccag
        gtacaccgatgaaactcggtaataaccccaaacgaatattcttatctgtcgaactagagc
        gtactcccggccccttagaaccaccgacataatgagaccaatttgcggctagtccttctc
        gaaacttggtttcgacggtttaatagagtactagggccggatcgcccgagcgtacggtga
        cactactggtcctgtaagaccgggtcccagttcgcgaaaacctctcggatacactagagt
        ttgagataatggatggcacgagtcgccctacgtcctgggttaagatactgacgagcaatc
        gcccatcgtccgtgctagcgtggctaatttgtgcccagtaacttacgacgcgaagtttgc
        ccgcccttcccaagggcccgacgggcggacgcagacacattgaaaaacctaggtccgctt
        cctactcggtatttgcggtcttgagggcccgagatcttcaagagggctatattcgttgga
        ctgctcacatagcaaccagcgccagcgttgactcgcctcgtgtagcttgttcaggcggac
        aatatgggtacaatttaggaacgatgtatttggtcgtctgataactttatatccaagggg
        cgggtagcgtcatgagctgg
        """)
    st.write("""
        # Test Case:3 - 10000 Sequence
        ### Evidence: 10000 Sequence
        ```
        tgagtctcaaggtgaacacatcggcgtgataacaaggttgattcacaccgatcaagtagc ttagccagacgggtcactgtaccgccgtcgctgcgtgcaattcgtaaactggttacttct
        tagagtaccaaaaacccttcccagggccaacctatagttggtggagcggtagactatggagaggttgaaacctgtccctgtgataatctgagaggtccaggtccagacacctcatgcgat
        tttttagatacgtaacaagcgagtagctcctttatgtgtcggggtttctgatgtaatggccgagtataatgcgtcgcttacgtcgtatagaatacctgaataggtaacttaaagttgaca
        caccgatgttaataacagaaaccagcggcttccgccgaccctctattcttcctatttagctgccaagacaactgatagagggtcgatcctactcctcgactctatatatccacaagataa
        cgcacgttcgcgcatgattgtcttttaggggctacgggactttaaacggatgccgaacttggatgtgctgcggagtgactatcataggagaacaggttcgagcctagtacctcaacagtt
        atttggaatcccaatcccgccgttgtttcacgtcatcttgagaggtcgcggtgcctcagcaggcaaggttcacgtctccggagttgataatccgttgagtgcccacttacgaatattttg
        cgtttcaccctgatttctgggcaatgacccaatgagcaccgatactctagtggctgatgtactggagccaaaacggactagataaaacattttagggtggcaagcgtgttcgggttcttc
        caaccaccatagatcatcctaaaaacctagctgcagggttaagtcgtgctagcaaagtactcctaaaacgagtatccaggggctggataaagcacggtgggtcgcaccaataatccaaca
        tcaaggccaagacactctgtggaagtagtctccccagggcgcatcgcttcccttctactgcggactatgcacgctacagcagaggatcgacgaagtacaagccggtatgatactcagcat
        gttgccggtactgtcaaaactcgcctcaggatcactacagtgccttatgcacatgcggccgtcagtgaatggaggcctaggaagacggcaggtcgcaggcagcaatgagttttagccgta
        agtggccaagcaaccggactgttagtagtatagacatgattagcttgcccagcccaaggacgatatccgccgaggcggcttatataagcatgacttgtcttagcagcggatggtaatttg
        gctacttcctgaataaagcagatcagacgcgtcgcggccatgctgctcaggaaggtgatcgagcagctacggggcgcgccgtgcaatggcttctaacgggagtagggttgcacagacctc
        ctgtaatctaagctagacaattgttgtaaaggcgaaagccacgaacaccagctcaccaaatcggagccgcagtttctcgctagaatcgtacgggtccgacgaacgtaacgtgacccttat
        ttgccgccagcagagcgctcggctcgatccagtcgccagccctaaaaggtagttcgctgaacgtagaatcaggaatcgctcttcctgatttgaactaacttgagatctccacgccagtgc
        tcgagatcagttcatgagaattccatctattctgtgcttgcaatgactgctcgattacgtccataacactcttgcaggtacagcatccatccgatggctttaaaaatttggggcatctgc
        cttcaacttcctcaagggcgtgggccgcaataagtgctggctgcacacgactacacggtatgacacgagaccctcgttatgctaatcaatgtttcaagtttccactgatctccagctgac
        tgcacaccaatgccctaatacattatccaacttccgtctgtcaaagactctcaaccccacaacatccggagttatgcaaaccgatcccgtaccttcgccgtggcacacgacgatcatcac
        gcactatcggcgatatgcggcacaggatctagcagtttcggtcacctcttagaaactgagcggttgactacgccataataagtatgtctatctaggcgacgctggaacgccagccatcca
        actcctgccaagcggcgtttcgggagcaattatctttccgaaactgccgttcactagacctgactagcctacagccgattatgtttaggacagagaattagcgcgaccaccaccagcaag
        gacaacggctaccccctggtctgatacgggcaacctttgacatagatgatcatctccagagatgcggcagggtgtcaccacaaaatatatcctagagggtaggcgaacttagattgagcc
        gttcgtattgattgccaaaagtacctatttgatagggactttggcccaccgccaagcacaaagatctgtactcgctactcgatctatgtggagcgtatccgttagcagacatcgagccac
        aagtcagtgcgcgatgcgtcgcggacccaacgcgatctaaaagtctacaactaatccggcctaacgctactccaatacggacgtatcctaggggtaacagttatagcattccccttgcac
        ctggttactgcttgcttaaaaatcataagccaaactaatcatgttttatgcgcggctcacaagttagatagtaatcctcaagccgtttgttcggggttcctgacatctagaacgcgccaa
        ggcacgccaggagaagtattcgacgctcgaccaatggatgtgtcgtaaaacgctcttccgcgtgccacagaactgaatgacttgccacaagggcgtatatgtagtcacgtaatcagtcct
        tggctaggatattgccccatctactggatctggcacaatgcacattcagcgatttatctagatggtgtttcatccggggacagcagatagtagattgactcgacggtcattcgacagtgc
        ttcgggcggccacattcggacataaggcttctcacggcgtgacgataggctatcgatggccatgatcacaccacgtccattgcctcgcgggacgtaccaccgacaggcggttataagatc
        ccgtcctcccagaaggataccacaccgacggaggactttgttcaaggttagcggtaagatagttgaatcagacacagtagccgctaatgcccaacctgacggggtattcgtttctttccc
        cagtcgagtggtctaccccccgcctgcagacatgcataccatatgggcatcaggcaggtggaaatatgttccgacaccagggcactgcctactggggcgacattaccagagtagcgagat
        gataaaccagtgaaagtacgcacaaggtaatcgcaagtggggcttgaaaggacggcgtacggcattaccggggatgcgaagacatacttgagacacgttttgtgcatcggtacgggtagc
        cagatcctggttctgtctgggcgaataaggctatgataccccctataccacacaggagccatgttggcggaacgccacataagcctaccgcatgtgtcaccttcgaccaatctgttgcgc
        tggataggggttcgcagcgtcgtagtcatgtagctcggaagggtagaggtcacaaatactctccggcgcatggctgaagaccagatcctccaaactctaatcttcagaaaacatgtgtcg
        ttcgcagtcgcgtggagggccgttaaatcttctactaaagttccgtgagccatctaattacggaggacctttcgtggccgggcacgcgagacagccagggaagtcatcgtaacttgtagt
        tataattctaatccgaaaacaagttagcgtcatctggatgtaggagatgcgtccatggacacacgtttatatgcgattcctaccctttttgtagggtgaccattggtaaactcctgtggc
        ctggactcttgaaacctttaacccaccctcttgtagctcggtcaacaaagtaggcagactgcgtcctacaacgagtctaaaccggcaactggggatgcctgtcagattaaggtctccaca
        acgatatgagacagctcgccgaattaaggccacaaaacagtaatccctaggtactgctgagtgacagtagtcgcggtacccctgtggactacaaatcaactctgacgataaaatcacaat
        cgagcactaagacgatcgcaccggttgctggcgcctgtaaagtaagttcaacggttcccttacaataagttggtaacttatcgacgattcagtgatatagagcacatgattgatggctac
        atctgggaggaacaggtcgatcgctttgcctgagcgtcggcctgtcgcgtatcgatgtgacgtggtgtcagaggtgcggttgttgggctaataagtttactgcgatcccagttccctggt
        tgagtttgtataccttgtcgcccacccggagacaccgttaccgggttccgcacaccttgctcgctgtgttgagggttttgatcatatacgttcttgtccggttttgagcatataaagtca
        aatcttcaatgtgtattccacgcctcaagatagcgtgtgtggtcttggcagcttactatttacaacgcagactttatagtgaggatttgcctcacgtccggaaaaatagatgtgctcggg
        taggggctataggctttcagctcgggtcgacacaatgagcagcggaggaactgtatcacttgtgaatcatctaggcaccggcataacatcgatgcgatgcattgggtctagaatttaagc
        gtcatgcaacaagtgcactaatgtaaggttacgtgcagccgtcggcctcaactgggagtttctaggtaatatacggctagcccctttgctcaacatgggaacagttgtgtgaacaagacg
        ggaccgggattggatcaccaggcgggtgtgtttacattattgtggccataatactgactaggtgaccgccggagtatacttattgacaatgcgcaccacgcaggcgcggcgggtgtgaat
        cgtatccacagattcaaaagtcttcaatccacgtgactttgaggtaatagccgagggcgcttacgttcaagggcacctgagacttaacctgaagacgacaaacatcgcgctgcattctag
        actggtcacctccactccttaacctactgatagcccgggacagtgttaaatatcctgcgctctaatcgaacgagcctgaccatccctttaacgtccgaaattaccttcttcggctaatcc
        atcttatctctacccgttgtgacggtctctgaacgcttaatgttccactgattcagatgttgcggcattcgttctagcgaaagctgtgaccaggtgacccgaagcatcagcgggtgttta
        tatccgtcgagacaggacatttcctcatcttgtaacatcggtacaaaattgggacgcgttccggtcgctatattgaattgacaccagaatttggtgtaacgtttcttacggaggacaact
        aagtatatttgggtcagagtgccacacacagtttagtagagggaccgtgcaaaccagtacgctgtaaataaggttactttcattgcgtttctgcacgctcgcagtccacggtaaagaata
        cattatatgcggattgtcgactgggcgacgtcgtggttgaccattgtagcaatcgtgcctcttacgaatccagataccgaaattaacgcttctccgggttaccgggtcccgacggacact
        ttcagcccgtgaaatttcaatacttgcacaagacgcgtctcttaacggcatacctgctagggacgctgccgatattaaactaggttgaataaagatccggagttttccgctgcgggcgag
        ggagaatcgcccgttatttcgcgtctccgacgcttcagttcggacgatcagaccggcagtgggtgctgcgctctcgtgataattacccctaaagtgtgatgggacgttccttaccagtcc
        atgaaatgctagaacacactactcaacaatgtaggtgccgggtgaggctatgtcctttaccctcgtggggagacactagttgaaggcttgaagacaatttaggccggttcgcctaaactt
        ctgcatagagtggaccaattaagccggtcgcctcggggccctggatatcccaaatgccccgtcaccatgccataggttctcagcactcattcacggcggtttgtgcagacatcggaacgc
        agagaggattggacgggggtgtgcccccgattgctgagatcaggttaacaggtgcccggggacatgatacacgctatgattccaatttgcatctgatggttccaggccaaggacagcttg
        caatctatcggggtaatactatggtacccctatttccggagcaaaaatataaaaactctggccggatgcactgttagtgacttatgcaacccagtcctttacgtcctccgcgtacaggat
        atggagacagcagcgccatctcttgatagcgattctttgccccctcgctcagtgagtacccttagtaagtccatccggtgcggagggtgtccattgccactcgagagtggtcagggacat
        tcttgttgctaaccccttctggaaccagcgaccacccagagtaacggtcgtgatgctagaaaagtatacaagagttggggtccgactgatcctctgaccaagaggcccagaattcgagct
        ggtggaatataagccggcaatcggaagtaaccctcaggtccgccaaggctggcctaaataatagagcatacagcatatccctattgcctcaccggatagacactgcgctcttacttatat
        tcacactgaacgtccgcaaacaggacgcacaaaaaagactacagggcttattgtgcttctgtttatatacattcactgtaggccgtggagatttagatgaccccactatttttatatcta
        ggcctaaaaagggtgttgcggtatgtgaggtcgaacgaacccgcaaatagggctggcctcacaaggccgaactaagaagtagaagaccaagagttagggctagagttcgatgggttccgg
        cttagcagttgctgatagttatgataaaattggacgaattaagcccttaggttattactctcccgtctggcccaactccaccgtaagcaccttctttaacggtgtggcataccataataa
        gccccccttcacgtagtgtcatccgtcgtatttgccatagcgcgttgtcgcccttgttgaggagatactccggtgtgttggcaccccacccaaactaggaggttgggcctatgactcgtt
        ttgtgaaggctggacagatttacttctcacgccacgcgttgagaaatgccggtggcggcgttcgaccttgtcccaacctcctatcagaacaacccaagattcgttgattgctccccctgt
        caggttcctccctctattaagctaaatgccgagctgtttcgctatgtcatctcacaacgttgtggtcaactgtcaacattgtttatgacgaaatacgactggcgcactttctatgggtga
        cgtgaaatccctcatgagagatcgcacgtatgtttgttggggcacgggtaaccgatttcgatcgacgccgtacttacgtcagcgcgaccttagctcagcataacatggtgattcagggga
        tctcgaagcaagaggggggtgctatgatttctgctgattggttaataccattgttaaaattgctatgccgataccactggacgtaccgaacaaagatagttcgttgcagtatcttgccgt
        ctgaaccagatctaaccattcgctgcccagtcccgaatgcttcactcagcccaccgtctccggtgcgcctgctgtcctattgcatctgtcacttggcaagtcccgctagggttgtcgcaa
        ggcccagggaatctttcagcaacgggcctgtatttattatgtaatgggcaaggaccataccgccaacgttgtgttgggaaaacatcatttcgcctgaaatacttcaactcggtacagcaa
        tcccggtcttaaataactactaaacatgacaccatagtttttagttgtatgtgaatccgtgaaacttcaccattccgcattgcactaacatctagcgctctcacatattaaaataagtac
        acttctagaccgccagatccgggtcagggcgctgtttaaaatccgtgtacctttcacggcggatacgatagactcagatgagaggggggtcgtagtgagtcgattacaccggcagttgtg
        tcgcggtatcttggcactctgttaacgttaaggacgggcactgttcacttacgcgctccctacatttcagggcagtggcccgcgtagggataaatctggcccaggatattgcaacatgtt
        cccttcaacatacattttgcgtgtaaaccgttgcatccgcgatacaagaataggaggacctcgactccgggaggtatacacgctggtacttggttctcgcacaagaaatgcggtaatcgg
        cataagagtcgtagtaatatcgccggttcctctgtgtccttatatagacgctgagcgtactctaagcggtactacctccggttctctacaatttgtgaaatttcctcggacgcgattcgt
        attagtgaagagctccagcaaatgccgcgagtggatatcatcaacacggcgcatctgggtggacaccagtgccggatggtgagaattccactttatctcataggagacaataagaaatcg
        aggtaggcccctaagagtctcccttattgtggaatagaggcggccacacttcggaggtagagatttcgttggtcgtactagctggagagtcgggacagatagaaatcctgacctagagta
        taatggccaagtggcctgacgtgacgtgtgagtagttatgcaagcgcctttcttgcgatggtgctacggcgagcaggaggtagtagaggccggataggaacatactacattagtacactg
        gtgaccggcatgcgtagagtaaacggctaaacggcgggatgcatacactcattatggcaccatcgcacccgcagatgtgtatggaccgcgtcggcttccacagcgagacacggcggccat
        ggaatcttgagctcagcaaacacacagagagctatgaggatggttacgtcccctgagccatggagctaggtaacggcatcctcaagctgtagtcaggaggacccacagtcggatgatttc
        ccggactttatgttagcacctgcttaagttctccagcctctgatcgtgctcgacgacaaggatcgcttagataagcatgacccgacgggaacaatagcgatcctagtttcccgtcttgtc
        cgagtcatgaagctatcgtgtctaggatttatccgcaagcttcatgtgttcgtgaggtcaaagcacgtcccacacggcgctgaacttctgggatcgccacccaacccataactcgtcgtg
        tcccgccttgtcacagcggtaactacatagacagggagtagctatggttggacaacgagacgcgtggtacctagcacccccaactggaattggacatattaatgcctgagggcacaaagt
        ctccagaggtcctttctgttgtgccaacgggcgtcgagagtcttatgcgcatcatggttgttaactcagctagaaaaatcgcctgccgattcgagtaggtagtcagttgtgcaaaagcag
        gaccttggcagtcacggcggagaaagccaaccacgacggatagtagcgcggatgttgctagagccgcacggatgtaaaaaataagggagccgtcgtgtctgtctcaacgagaagacgcac
        gggctagaggttgggggccgatacactgaataaatccgtagttttgatggcaccgagacttacattaaccaacggggcgctgctgtgagtgtgaaatcccaaaatgagtccctgcggttg
        gcaacctcgacatcaatataatccgcggatttggggactt
        ```
        ### Suspect: 10000 Sequence
        ```
        cagcatttagggcgttagtgaggaagccaggtgtgtacacagaccacctgtacaatctgctcaactattgggctacattgggctatcgcatctttcgaaactacgcgtcccacctccgtg
        ttatactggtgttccccttgatacccccaactcttggtactgctctaagtagaaatgggaacaaccggaggaaaccaagttaaatccgagaacctttccaaaagtgcctcttaacgcaga
        aaggcaggaaacctacatcaggttctatcaaatagagctctggggttggcgacacgaaggaaggtccaagctctaggcccaacagccaagtctagtgagtcaggacgggcacgagcgaac
        cttcccttccggctagaaggcagtctgtaccatagagcctataatttatcgctactgactaattaaggtaaggtaagtaggcgcggatccatacaggctactccttcgatcttgcgatcg
        ggccaatcctggtgcagagaaaacactataccctcgtttgtcctgaacgcacgcactctccataagaattcggcctaagtcccgcgcgcttctctcaggcgttatcagcccattgtatgc
        tggagtactatcaacctacgaccgacgtcgcataagatgtgtccgtgccgtcctatttatccttgagccctggggaccgagcctcgccgaatgtctgggtagcgtggcggtctctaccgt
        ccacaccgacaccgtgaaaccatacagctgtagttaccgtttggtcactggcggtacccccgcctcgccactatgccgagcgcgacgagaacatcgaggttgccgccatcgatactcgta
        agggtctgaaatccacgctactccgctcaagcttggtgacattggtatcaagttcggaaggacgtaccgcctgttatccaagaactcagggcatagtggcctaattcgcctaacaatgag
        tgtatattcattctaggcttcagcgccgaaaagcgattgagtcactatttttcaaccaactcgatagccataatctacgttaccaatctaattctagtcgctagggatgcttgactatct
        agggcgaaatatcgcattacgataacaaccttaagcttagatttgcttctaaagtttattttgaccaacggtgtggtgatcgcatgttcccgagctgtttcgactaagatgatgagaacg
        ttagagcgttcctactataagctaaggtcctcttgaaattacgtatgactatgcggctagcgtttcgaagtgacttcgatacgagaacaagcctcgcaatgcatcataatagaagtttta
        tgagtacctacccgtaggacagcagatgacctttctgcgaacaggtcagtaagcgtggtaccgaggcagtctcgatcatttacggaacagatgggcacttcgccacgagtgcttgctgct
        tgatcggctttgacattaatcggcagtgtttacccccctttgacctttcataagcctaacgtcctgcaagggttcatctcaactggcagataagatccagtgtctacattcattcgcgtg
        acaatataacccatctgtgaacctatctatcctgatactccaacgatgtcgttcaagcgtttttccgaagacgcagttcgtttgggttcaaattgagctgcggggtgcggtaaaaaatcg
        ataggacctgccgcacaccccacaaataacagcaagtcgggttcgaaaagagttttccatgtcatagagggccatcgtcctaaccacaaggaatgagtctattgctgtacggtgaactat
        aagttgcgtgtcaacgggaagcctaatcccaactatacgcgctctaaaacaaatgaatgtaacactttaatgtgcatgtctcaacaacggcaatcttccgacagtgcgcttttggttcgt
        cttttaacgtaagtacaatttataccacaacgtaggtgcactggcaggcatttaagccgtcactcccaaaaatattatggtaattcggagcgtagcgcgccgtgctcacgcacaacttca
        gcttgaatcggcattatctattatcactccgcccctctctctgtgtggttactgaagggggtccctgtgccaatctccaacaaaccggtataggttactattctcctttctgcctagtgc
        gaaaacagggtacacgaggtaacataatttggcgcccatctttacgttgccgggccaattctcccaacgatgatatccgactgttcttcgacctctcgcgtggacagcgatttgaggatt
        cccttagtgactgccactcccctaactaacgccggtcggttgtaaccctacaggtctgtggaaccacgtttcctttggccccactgaagtcggctgtccgtgcacacatcgttgcgatgc
        ccccccttggtgaagcacaaacagcgcgcgggtacacacctcttcgtaggggaggtcctcactgggcaacaaatgataactctggccgcgtgggaccagtagtttctgaatttaaaaaag
        actgtgatacgatagtacaaaatctctgaggttgccaaagccctcgtttatgatgtcaacaaatagttgatgctattgggcgttcaggttatatctagttcacaccgtatataacctaac
        ttagctgctcatacccagccagtattgatgtgcaattggtcattttgtgactgccttgtttcttaatacgcagcgcaggcccgggttagtaacgctgtatggtacgagtgaaatccttgt
        gcaacaacctgcccacctttagtaacttatcgcagcttgtttaagggttaccaggattctcagtgccccagcaacccgtgtcactgagtcgtatgttgcgaaaaaagctggcgtaatcaa
        gttgcggctttcctaccacagtgttgtaggtagtccaaataataccatgataacaattcgaataggcctatggcacgaatctatacattacaattctttaatagaaaaattgtatcgtgc
        gcctttctcgcatttttgattcagccaagcatgcgccaacgcgtagacttgtaacccattggcacaggcaaacatgaacaaggagtttcacgtaatatccctactccctgtgggatgccg
        cacgcgaacctaatttccaaattcagaagacagaccataatggtgtggcgggacttcatttcttgaccgcaatagcgcaagcaccagcgaaccctgtagatgtccatcgccaacggcacg
        gcattggggcaaaccgtgttcaccataggggatctagtccttgcctcagtaccttcaaagctattggcggaaccccatcgccaacactctagcggggggtaaggcacgtgcacgcggtaa
        cggttcatatattcgcatggtgagaggagaaagccctcgccataactagagggcggatgtgcgttcgccgatgccatctcctagctcagtatgcgtgaacccatctcggttatgttgtcg
        cattatcttgcccgccggctgaatttaattcaagtggaggaagtcttaacatgtctagaaaaatgacgctcgatcttactggtcatttcgtgatctattctccgaggcgtcgcgagagtc
        ccaccccggtggaatgattgtaataataattaggccggtaggccgcaggccaattagccttctaacctatactttcgattctcacacagtctatcaccgaagcccagtcgttgcgcctaa
        gtttgcactcgaatcctcactttggtactctctcgaataacggcaccttcgcaggtttcgctcaaatctggcttcagcgctgtgccacagctgtgagtttctcatgtctgaaacggctta
        ccaatcggtagcctggggcacgactcactcagaaccgacgcagttccgctcaggggtcaaaagagcctgcgaatcagaatctgcagcaggacatctaacaacatggatttgtggcaacca
        tcgggccgactatggacccaggattggcccggcaagctctactagatagcgccgctacgccgatacggcggcctcactaccaattccgttttcaagttacctgttctacttctaagctag
        aacacctagaaagatcctctcctacgttgatagacctcacaagtagttcacctgcgtatctgggggttgctttgatgctatctatgaacgagagaattgttcgatgcctgagtcaactca
        gataccgttccgaccaacgccgagtcagttatctatcgtcagatggtttctcgccatcggcttattatcaagaaattgccggagctagtctctgttagtgtgtgaccacagatcaagtcc
        aggtctgaggccgtccctacctgtaaagaaactcaactacacgctttgttaaatacccaaagtcggcgttgtccagtcgcctgactgcgaatgggtcccgttagcgttttgggggccaag
        gtacgctagttggtacaccagtacaggatctgggaggagctgaccgtgcttagaaaacccccttcctccggaatctgtgtaatcttcccgatgagatgtctccgcgctataggtaactaa
        ataagaaagtgatagactctgttggaatcggaccattgcaatgagaagccgagtgactaatagaggatgcttatacttaaagacgcgggaccagcattgctcgctacggagctcccttgt
        gtgccaggggattttgcgtctagcgaccacacgtttaacccgtgttcataatatccgttaccataccgcgtacaagaatacgcattgtatctatgaaggacacgacaaaagtatagagtt
        cccggccgctacgcatgaggctggagcgtcctacctggttcatgcatcgcatcgtcaatagctaggaacattaggtaccacgaaaatttggcgccattgtaaagccatgtatgtacggcc
        ccggacccttcctggtttaggactcacacaatagcgccacgaatacgtttacttagatcatattagtccaagcaggcgatcaactattgccctacgctcacagaccgtagtcatatgttt
        cgtttcgggggacgaccgtcgcactaccagaattattcttcgcttcgtggtcaaagataaaaattaacctgggacaggatgtacggtaggaccataagcccactcaaaccagcacgaagg
        aacgcgaatggtttattgattcgtcccactaacgtacaatcagtatctttcccgcaaaaggaatagatgggggccctattgcgggcccgtgggaggtaatggacactttgaacggagtct
        ccacatgtatagaagcagcctggccaaaacagttaatagaccgcttactctaaggagacagcaaacgtcccaggctagcgtttggcggtcccactggtcttgatacggtggcctgttcca
        accgcgtgtcgacacgcctatttgctaacgttacctctatataacatatgtatatagtaggtgatgatagtgtagaacctgttccaagcagacgccaaaggtgaggacgggcccggccgc
        ggattcgattaatacaagggccaaaagctggcacaagaaacctaagagtaaaaaagcctggtttctcagagcaccgtacagtggtctcaggctcagtcgtcccttaacctgtagccaatt
        tgcccgttcaccgaagtcgtctcaaccgaggatttcatcgattgggaaccacatgggttcaagcagacgcgctcagtgctgcggctaaccgggacatacctacaggtccgctttcgcacg
        cacgaccctctcgtttttattgctcggtatctggaggagccttagtcacttggttgggttttgccgactctatcgacctggctttgtcaatacttcaaagtgatgcgcattgaagacacg
        ggcccaattattatcgtccaatttcgagcagagcactattgaacttaacgggcacgagtgaactggcggcgtgtagacgacagtgaggaagaagctcacttgtagacaggctcaagtagc
        tataagtcttccacctctggtgagacaatccacttacccggggcagtaagtaacattaatcttcgatacttgaatgttgatatctattctcatagtcccgctggcactaagaccccggcc
        gcattggtgggtcaagcattattttcttataataagaaatcgctaatgacataaacccgtcgcgtatgaaaaaacaatctcagattatatatggtacggccaaacgccgacggatgtaac
        atgtcatttctcgtactcttgctacgccgttcaaaccattgacagcctggacgcgtgcgaggcacctgcatagtacagtagacatcgtagatgcatgccgtgaatggacttatccctctc
        ggaccggtaccgacacatggagtgcgtcagtcacggggaggcctagtgcaaagcctgtccctctcagtcatctctcttctacggtcggcgaaatgtaattgccattctttgtcccgtcag
        gctctccggatgccagcagcggaacagcctattgacgtacaggagtagaatctcactacctcgacaggccactaaggcacgcgttatcctagagaactcctagctgatctcgtgcagcgt
        taggctaccaggctgggtgagcgtcctctgggacagccctcaaatcgaaggagcacagcggcctggcgtgcacgcccggcttcagatgactaatcaatatggaacgggaagagtctcatc
        acaagggatcgactctctactagcgcatgtaatagacgcaaagcctcgttcggaccaagggtataaaattacgtggcctgtttggaccaagcgacgagtctacgtaggcaacatcgcgga
        tgggtcctacgcccgaggacgggttgtagcaagattatagttgcgcatattacgctatgactaatttctcaaacttatttatcttcagaggttgtgttgccccccgacgtaaacggggat
        aacggtcgcggtatgctcttccattgtgcatgccgacaattctggaacaaacccgtatagacaaagtgggctggtacatggactgcgaatgttggcgtttcctaacaatgaggcattctg
        aaacaaccgcttataggccttggggcaattcggatctagattctgcacaccaacaatgttagcctgggtctagccgtgaggagtggataagccagcatgccgaactttatgctgttgtta
        tgttggcggccatctatatgcctttctcggagtgtgttacccgtaacaagggcagtaaggttctggaaatacgacttaaccccgtgctcaaaagtacacagttagcagtgcgttcggttg
        aaacgaccagtcctctaccctctcctgtaaaaagctggagagaaggcgaccggacgttccataagggtagatcggtatggacaaccctgctggctgtctccacatccaccattggcgcaa
        atcgcactttgtcatctgcctcacgcccgccgctccgttcattgctgtatgcccgatccgacggtcatcaagagggcctcaagtacgtactgatgggtaagatggccaaagatggcccaa
        actgcgcaatcattcgaacgggaactcggatgtacctaattccattaggcgaaatcttaccctttatacagattcgttatgtgtaccacaggccgtaagggtcgctagccgtaggaagcg
        tgtataagggcagaagaccgagagacgtccgtattatggcttttggtagcagacgggtaggcaaatctcaaagagtctcatgggccaccgaaaccaggaacaccctcgaggatatccttc
        actagggatagccattctagaacgacaagcgacggtcgcgtctgctgcctcgaaatcatctctcgcggaaccaatgatgggactggttcaaggtacggcatgcattaatgaagcgtttga
        ccgctggtgtctgacaaaattacatttacgtgtatcggctaacaaaatctactatcgaccacaacaggcattatgatggcttttccgcagctgaggcctggcactgtgaacacatgcccc
        tttataacgcggcatcaaccttagtactcgaactgcctagatctaactaatgtcctcaaaggatccatttagcggtggaacaggtacacccaaattgtcccctctatggcggccattcac
        tggattattagtgctttatgctcgcccacaatttgacgatgccacactccatgcacttaagttcactgaatgaattggagattaataaccctaccgctgttttcggttcatgtgggtctc
        ggcccggccaaagaacgtattactttgttcccacgagatcgtctgagagatgctctacttagtatagcagttgggatgaacaggaagacgcgagggaaaccacaaagcacctttcgtgaa
        caagacgcctctccaaatcgcgaccggctggaaggtttaggcccactcgcgaggtttagtgacccttattacacaagaggtccgtattaatgcaccgaaacttcccgggaactcattgta
        tctcgtatccttaggactgttggatactgccctgtacattagtgtttacagacaaacgcatcacccttaaatggccagccgaaaaaatggtgcataaaactagtaatccgcgttgtgtga
        ttaacaagaatttttgcactacgggttgagtgcgtttatggtcgtaaatatgagtaacgagataggagaagaggagtcccagtaccatggccttggtgtgcagtaagttgattataaggc
        ggtcttaacctaggagcgtgagtgctcacaagctccgggcaaaagagggtaaggctcagaacgctatcctatcgcctgaaccccgcctttcgggtccggtgcccgctcagctgaagatca
        gtcgtccgtaagagcccggtcgagtcgactcactctttactataacctacaaatcccccccaactgagttaaagacccctcgtggtcgcgctctgcaggacagctagtgacactagacga
        aaagccgactgcaatgtcagattcggggagccatcaatccttacattcgcaaggcttacccaaaatttccagacggaattgaggtgaaattacttatcggggacactaggttacgcggtc
        tatcttgttctattcccccctacacagacgcgcgagcctcacagtgcaccagttctaattatacccgagtgcggtaggtacccttcctaatgccttcaaggtgtcgcatcatagcttcgt
        gggagccgcagaggtcttagctagtggagacggtttaaacctcagacgcgggtcgagcaacgagcacagaaaacggtgaatatttatcatcatatacatggcgtggaagcaaattgggct
        cgtcgtgattacagtacaaagggcttgttaggcggacctcgtcggagatggcctcctcccgtccccgtttgcgtgtttgtcggagagctaggaacagatcctgaggggatcgaggccgat
        tcaattgggaaacggtaacgcctcgatactttcgctcctatctctattttattagattcctaggatccgaacgattccctcaagcgttttccgagaagcccaattggccagtacggtact
        cggccgtatcgatgacagccaaattgggcggaatcagtctgggaagccggtaacctcggcccacggatcccagatcgtgttcagctagcatgccatcgacatctggcgccttctgcagca
        gtatagaacttagcctatttccgccagaatcatagaggttgatggtcgggggagagttgtgaggtcacatcgacccacagtgattggggcatagttgttgtctgcccattgctatctgtc
        tatttccaacgtgaactacaattgtgcctcaatgcgtcccccgcccgcacgactgacttcacttagcaacagttgacgtgcatttaatatcccactttgttcggccagactgggaccctt
        ccacagattgacatttcgttccctaccgtgcgacctccat

    
            """
             )
