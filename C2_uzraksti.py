# ----------------------------------------------------------------------
# C2. Nauda un griezieni
# ----------------------------------------------------------------------

# Lietotājam ir 20 eiro, viens grieziens maksā 3 eiro. Izvadi, cik griezienu viņš var atļauties un cik naudas paliek pāri. Visu kodu raksti pats.
#
# Šis fails ir tukšs. Visu kodu raksti pats zem šīs rindas.
# ----------------------------------------------------------------------                                                                                                Katru rezultāta rindu sāc ar zvaigznīti un atstarpi.


nauda = 20
cena = 3

griezieni = nauda // cena
atlikums = nauda % cena
print("Griezienu skaits: ", griezieni)
print("Atlikums: ", atlikums, "eiro")
