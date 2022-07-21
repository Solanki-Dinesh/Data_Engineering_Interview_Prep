import fitz

with fitz.open("students.pdf") as pdf:
    for page in pdf:
        print(page.get_text())
