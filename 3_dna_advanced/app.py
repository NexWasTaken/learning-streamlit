import streamlit as st

# Codon table
CODON_TABLE = {
    "AUG": "Methionine (Start)", "UUU": "Phenylalanine", "UUC": "Phenylalanine",
    "UUA": "Leucine", "UUG": "Leucine", "UCU": "Serine", "UCC": "Serine",
    # Add the rest of the codon table
}

# Functions
def transcribe_dna_to_mrna(dna):
    return dna.upper().replace("T", "U")

def translate_mrna_to_protein(mrna):
    protein = []
    for i in range(0, len(mrna) - 2, 3):  # Read in codons
        codon = mrna[i:i + 3]
        protein.append(CODON_TABLE.get(codon, "Stop"))
    return protein

# Streamlit App
st.title("DNA Transcription and Translation Helper")

st.header("Input DNA Sequence")
dna_sequence = st.text_area("Enter a DNA sequence (A, T, C, G):").strip()

if st.button("Process"):
    if all(nucleotide in "ATCG" for nucleotide in dna_sequence.upper()):
        st.success("Valid DNA sequence!")

        # Transcription
        mrna_sequence = transcribe_dna_to_mrna(dna_sequence)
        st.subheader("Transcribed mRNA Sequence")
        st.write(mrna_sequence)

        # Translation
        protein_sequence = translate_mrna_to_protein(mrna_sequence)
        st.subheader("Translated Protein Sequence")
        st.write(" → ".join(protein_sequence))

        # Codon Table
        st.subheader("Codon Table")
        st.json(CODON_TABLE)
    else:
        st.error("Invalid DNA sequence. Please use only A, T, C, and G.")

# Download Option
if st.button("Download Sequences"):
    download_text = f"DNA: {dna_sequence}\n\nmRNA: {mrna_sequence}\n\nProtein: {' → '.join(protein_sequence)}"
    st.download_button("Download Results", download_text, file_name="dna_translation.txt")
