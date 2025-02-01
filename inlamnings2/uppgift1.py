
"""

import csv
import pandas as pd

# with open("C:\\Users\\Jahan\\OneDrive - SUAVIS AB\\Skrivbordet\\Nadia\\DataMenegment\\data science\\vscode101\\inlamnings2\\befolkningsfoeraendringar-helar.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
#     data = list(reader)
with open("C:\\Users\\Jahan\\OneDrive - SUAVIS AB\\Skrivbordet\\Nadia\\DataMenegment\\data science\\vscode101\\inlamnings2\\befolkningsfoeraendringar-helar.csv", "r") as file:
    reader = csv.reader(file)
    data = list(reader)
    for i in range(len(data)):
        print(data[i])
    
data[0].append("New_colomn")

# for i in range(1, len(data)):
#     data[i].append("noll_hantering")

for i in range(len(data)):
    print(data[i])

with open("new-file.csv", "w") as new_file:
    writer = csv.writer(new_file)
    writer.writerows(data)

# eller

with open("C:\\Users\\Jahan\\OneDrive - SUAVIS AB\\Skrivbordet\\Nadia\\DataMenegment\\data science\\vscode101\\inlamnings2\\befolkningsfoeraendringar-helar.csv", "r") as file:
    reader = csv.reader(file)
    df = pd.DataFrame(data)
    print (df)
   
"""

import pandas as pd
# Kontrollera antalet maximalt returnerade rader:
pd.options.display.max_rows = 1000
 
# Extract: Hämta och importera csv_fil och läsa in data:

df = pd.read_csv("C:\\Users\\Jahan\\OneDrive - SUAVIS AB\\Skrivbordet\\Nadia\\DataMenegment\\data science\\vscode101\\inlamnings2\\befolkningsfoeraendringar-helar.csv", header=0, sep=";", skipinitialspace=True)

# header=0
#sep=";"
#skipintialspace=True för att ta bort mellanslag mellan kolumnnamn
 
# Utforska och visa dataframe:
print("Första 5 rader i df:", df.head(5))
print("\nSista 5 rader i df:", df.tail(5))
print(f"\nAntal kolumner: {df.shape[1]}")
print(f"Antal rader: {df.shape[0]}")
print("\nKolumnnamn:", df.columns)
print("\nInformation om datan:", df.info())
print("\nData statistik:", df.describe(include="all"))
print("\nHela DataFrame: ", df.to_string()) #använd to_string()för att skriva ut hela DataFrame.
 
# Filtrera baserat på villkor:
filtered_df = df[df["folkmängd"] > 2500]
print(filtered_df)

# Hur många null värden finns det i tabellen
print("isNull")
isNull = df.isnull().sum()
print(isNull)

# Lägg till kolumn Konstiga Beräkningar
data_with_new_colomn = df
data_with_new_colomn["KonBer"] = data_with_new_colomn["födda"] / data_with_new_colomn["döda"]
print (data_with_new_colomn)

# Ta bort en kolumn
data_with_new_colomn = data_with_new_colomn.drop(columns=["justeringspost"])

#Sortera baserat på en eller flera kolumner med sort_values.
data_with_new_colomn = data_with_new_colomn.sort_values(by="år", ascending=True)
print(data_with_new_colomn)



#Använd groupby() och agg() för att summera och analysera nyckeltal.
genomsnitt_for_tiden = data_with_new_colomn.agg(["sum"])/data_with_new_colomn.shape[0]
print(genomsnitt_for_tiden)

data_with_new_colomn.to_excel("uppgipt2_exampel.xlsx", index=False)

