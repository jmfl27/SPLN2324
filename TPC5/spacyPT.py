import spacy
import sys

nlp = spacy.load("pt_core_news_sm")

expansion = {
    "DET": "Determinante",
    "NOUN": "Nome",
    "AUX": "Auxiliar",
    "VERB": "Verbo",
    "ADV": "Advérbio",
    "ADP": "Preposição",
    "PUNCT": "Pontuação"
}

def extract(frase,md):
    doc = nlp(frase)
    with open(md,"w",encoding="utf-8") as tabela:
        tabela.write("| Palavra | Tipo | Lema |\n")
        tabela.write("|---------|------|------|\n")
        
        for token in doc:
            tipo = expansion.get(token.pos_,token.pos_)
            tabela.write(f"|{token.text}|{tipo}|{token.lemma_}|\n")

if len(sys.argv) != 2:
    input = "default.txt"
else:
    input = sys.argv[1]

with open(input, "r", encoding="utf-8") as arquivo_txt:
    frase = arquivo_txt.read().strip().replace('\n', ' ')

out = input.split(".")[0]
extract(frase, f"{out}Out.md")

print(f"Informações extraídas com sucesso de '{input}' e foram escritas no arquivo {out}Out.md")