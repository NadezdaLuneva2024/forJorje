
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
#pd.options.display.max_rows = 1000
 
# Extract: Hämta och importera csv_fil och läsa in data:

df = pd.read_csv("C:\\Users\\Jahan\\OneDrive - SUAVIS AB\\Skrivbordet\\Nadia\\DataMenegment\\data science\\vscode101\\inlamnings2\\Skattesatser2024.csv", header=0, sep=";", skipinitialspace=True, decimal=".", encoding="iso-8859-1")
Skattesatser2023 = pd.read_csv("C:\\Users\\Jahan\\OneDrive - SUAVIS AB\\Skrivbordet\\Nadia\\DataMenegment\\data science\\vscode101\\inlamnings2\\Skattesatser 2023 v.4_.csv", header=0, sep=";", skipinitialspace=True, decimal=".", encoding="iso-8859-1")
Skattesatser2025 = pd.read_csv("C:\\Users\\Jahan\\OneDrive - SUAVIS AB\\Skrivbordet\\Nadia\\DataMenegment\\data science\\vscode101\\inlamnings2\\Skattesatser kommuner 2025.csv", header=0, sep=";", skipinitialspace=True, decimal=".", encoding="iso-8859-1")

""" Dubbel-backslash (\\) används för att undvika escape-tecken, eller så kan du använda ett r före strängen (råsträng).
    header=0. Detta anger att den första raden (index 0) i filen innehåller kolumnrubrikerna.
            Om du inte anger denna parameter, antar Pandas att filen inte har rubriker och skapar automatiska rubriker som 0, 1, 2, ....
    sep=";"  Anger att kolumnerna i filen är separerade med semikolon (;) istället för kommatecken (,) som är standard.
            Detta är vanligt för CSV-filer i Sverige och andra europeiska länder där kommatecken används som decimaltecken.
    skipintialspace=True för att ta bort mellanslag mellan kolumnnamn
"""
# Utforska och visa dataframe:
"""print("Första 5 rader i df:", df.head(5))
print("\nSista 5 rader i df:", df.tail(5))
print(f"\nAntal kolumner: {df.shape[1]}")
print(f"Antal rader: {df.shape[0]}")
print("\nKolumnnamn:", df.columns)
print("\nInformation om datan:", df.info())
print("\nData statistik:", df.describe(include="all"))
print("\nHela DataFrame: ", df.to_string()) #använd to_string()för att skriva ut hela DataFrame.
"""
# Filtrera baserat på villkor:
filtered_df = df[df["Kyrkoavgift"] < 1]
print(filtered_df)

# Hur många null värden finns det i tabellen
print("isNull")
isNull = df.isnull().sum()
print(isNull)

# hur många oanvändbara värden
hasNan = df[df.columns].isna()
print (hasNan)

# Lägg till kolumn ProsentLandstingAvTotalt
data_with_new_colomn = df
data_with_new_colomn["ProsentLandstingAvTotalt"] = (data_with_new_colomn["Landstings-skatt"] / data_with_new_colomn["Summa, exkl. kyrkoavgift"])*100
print (data_with_new_colomn)

# Ta bort kolumner "Församlings-kod"och "Församling"
data_with_new_colomn = data_with_new_colomn.drop(columns=["Församlings-kod", "Församling"])
print (data_with_new_colomn)

#Sortera baserat på en eller flera kolumner med sort_values.
data_with_new_colomn = data_with_new_colomn.sort_values(by="Summa, inkl. kyrkoavgift", ascending=False)
print(data_with_new_colomn)


#Använd groupby() och agg() för att summera och analysera nyckeltal.
genomsnittSkatt = data_with_new_colomn.groupby("Kommun") ["Summa, inkl. kyrkoavgift"].agg(["mean"]).reset_index()
print(genomsnittSkatt)
genomsnittSkatt2023 = Skattesatser2023.groupby("Kommun") ["Summa, inkl. kyrkoavgift"].agg(["mean"]).reset_index()
genomsnittSkatt2025 = Skattesatser2025.groupby("Kommun") ["Summa, inkl. kyrkoavgift"].agg(["mean"]).reset_index()

#genomsnittSkatt.to_excel("uppgipt2_exampel3.xlsx", index=False)

import matplotlib.pyplot as plt

# Skapa ett stapeldiagram
plt.bar(genomsnittSkatt["Kommun"], genomsnittSkatt["mean"])

plt.title("Skattvisualisering")
plt.xlabel("Kommun")
plt.ylabel("Genomsnitt skatt")
plt.xticks(rotation=45)
plt.show()


#Histogram för kvantitet
plt.hist(genomsnittSkatt["mean"], bins=8)
plt.title("Fördelning av skattsats per komunn")
plt.xlabel("Skattsats %")
plt.ylabel("Antal kommuner")
plt.show()


#Samla ihop 3 tabeller
kommunsSkatPerAr = genomsnittSkatt2023
kommunsSkatPerAr.columns = ["Kommun", "Skatt2023"]
kommunsSkatPerAr["Skatt2024"] = genomsnittSkatt["mean"]
kommunsSkatPerAr["Skatt2025"] = genomsnittSkatt2025["mean"]
#kommunsSkatPerAr.to_excel("uppgipt2_exampel4.xlsx", index=False)



#visualisering i linjediagram

import matplotlib.pyplot as plt
# Kommun     Skatt2023  Skatt2024  Skatt2025
# -----------------------------------------
# Stockholm    32.5       32.7       33.0

# Filtrera ut Stockholm
stockholm_data = kommunsSkatPerAr[kommunsSkatPerAr["Kommun"] == "STOCKHOLM"]

# Omvandla data till lång format med .melt(), så att varje år hamnar i en separat rad.
stockholm_melted = stockholm_data.melt(id_vars=["Kommun"], 
                                       var_name="År", 
                                       value_name="Skatt")

"""
🚀😊Förklaring av melt()-funktionen
Funktionen melt() i Pandas används för att omvandla en bred tabell till en lång tabell.
I ditt fall omvandlar vi tabellen från detta format (bred form):        Kommun	Skatt2023	Skatt2024	Skatt2025
                                                                        Stockholm	32.5	32.7	33.0
Till detta format (lång form):                                      Kommun	År	Skatt
                                                                    Stockholm	Skatt2023	32.5
                                                                    Stockholm	Skatt2024	32.7
                                                                    Stockholm	Skatt2025	33.0
Hur koden fungerar:
stockholm_melted = stockholm_data.melt(id_vars=["Kommun"], 
                                       var_name="År", 
                                       value_name="Skatt")
🔹 id_vars=["Kommun"] - Denna kolumn behålls oförändrad i den nya tabellen.
🔹 var_name="År" - Skapar en ny kolumn som heter "År", där kolumnnamnen från den breda tabellen (Skatt2023, Skatt2024, Skatt2025) hamnar som rader.
🔹 value_name="Skatt" -Skapar en ny kolumn som heter "Skatt", där skattesatserna (32.5, 32.7, 33.0) placeras.
Varför gör vi detta?
För att seaborn och matplotlib fungerar bäst med lång form, där varje observation ligger på en egen rad.
Efter melt(), får vi en tabell där vi enkelt kan plotta skatt över åren med plt.plot()! 🚀😊
"""
# Omvandla "År"-kolumnen till numerisk form. Tar bort ordet "Skatt" från varje rad i "År"-kolumnen.
stockholm_melted["År"] = stockholm_melted["År"].str.replace("Skatt", "").astype(int)

# Skapa linjediagram. Skapar en ny figur med storleken 8x5 tum. Detta gör att diagrammet blir mer läsbart
plt.figure(figsize=(8, 5))
plt.plot(stockholm_melted["År"], #x = stockholm_melted["År"]
        stockholm_melted["Skatt"], #y = stockholm_melted["Skatt"]
        marker="o", #Sätter en cirkel (o) vid varje punkt
        linestyle="-", #en heldragen linje mellan punkterna
        label="STOCKHOLM") #Lägger till en etikett för legenden

# Anpassa diagrammet
plt.title("Skatteutveckling i Stockholm (2023-2025)")
plt.xlabel("År")
plt.ylabel("Skattesats")
plt.xticks(stockholm_melted["År"])  # Visa alla år på x-axeln
plt.grid(True)
plt.legend()

# Visa diagrammet
plt.show()


