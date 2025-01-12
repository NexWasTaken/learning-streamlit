import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

placeholder_dna_seq = """GAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG
ATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC
TGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"""

# Page Title

st.write("""
# DNA Nucleotide Count Web App
         
This app counts the nucleotide composition of query DNA.
         
---
""")

# Input Box
st.header("Enter DNA Sequence")

sequence_input = ""

sequence = st.text_area("Sequence Input", sequence_input, placeholder=placeholder_dna_seq)
sequence = sequence.splitlines()
sequence = "".join(sequence)

st.write("---")

st.header("Output")

# 1. Dictionary
st.subheader("Dictionary")

def dna_nucleotide_count(dna_seq):
    return dict([
        ("A", dna_seq.count("A")),
        ("T", dna_seq.count("T")),
        ("G", dna_seq.count("G")),
        ("C", dna_seq.count("C"))
    ])

dna_dict = dna_nucleotide_count(sequence)
dna_dict_label = list(dna_dict)
dna_dict_values = list(dna_dict.values())

dna_dict

# 2. Text
st.subheader("Text")
st.write(f"There are {dna_dict['A']} adenine (A).")
st.write(f"There are {dna_dict['T']} thymine (T).")
st.write(f"There are {dna_dict['G']} guanine (G).")
st.write(f"There are {dna_dict['C']} cytosine (C).")

# 3. DataFrame
st.subheader("DataFrame")
df = pd.DataFrame.from_dict(dna_dict, orient="index")
df = df.rename({0: "Count"}, axis="columns")
df.reset_index(inplace=True)
df = df.rename(columns={"index":"Nucleotide"})
st.write(df)

# Bar Chart
st.subheader("Bar Chart")
p = alt.Chart(df).mark_bar().encode(x="Nucleotide", y="Count")
p = p.properties(width=alt.Step(65))
st.write(p)