from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("C:\\Users\\Jahan\\OneDrive - SUAVIS AB\\Skrivbordet\\Nadia\\DataMenegment\\data science\\vscode101\\inlamnings2\\uppgipt2_exampel4.xlsx", 
                   header=0, 
                   decimal=".")



df["Kommun"] = df["Kommun"].astype(str).str.strip().str.upper()
print(df)
# Filtrera ut Stockholm
stockholm_data = df[df["Kommun"] == "STOCKHOLM"]

# Omvandla data till lång format med .melt(), så att varje år hamnar i en separat rad.
stockholm_melted = stockholm_data.melt(id_vars=["Kommun"], 
                                       var_name="År", 
                                       value_name="Skatt")

# Omvandla "År"-kolumnen till numerisk form. Tar bort ordet "Skatt" från varje rad i "År"-kolumnen.
stockholm_melted["År"] = stockholm_melted["År"].str.replace("Skatt", "").astype(int)

# Konvertera "Skatt" till numeriskt format (ifall det finns text)
stockholm_melted["Skatt"] = pd.to_numeric(stockholm_melted["Skatt"], errors="coerce")

#print(stockholm_melted)

# Förbered data för modellträning
X = stockholm_melted[["År"]]
y = stockholm_melted[["Skatt"]]

# Skapa och träna modellen
model = LinearRegression()
model.fit(X, y)

# Förutsäg skatt för 2026
skatt2026 = pd.DataFrame([[2026]], columns=X.columns)
print("Förutspår skatt för 2026:")
predicted_skatt = model.predict(skatt2026)
print(predicted_skatt)




# Visualisering
plt.figure(figsize=(8, 5))

# Rita upp historiska skattevärden
plt.scatter(stockholm_melted["År"], stockholm_melted["Skatt"], color='blue', label="Verkliga värden")

# Rita upp den linjära regressionslinjen
plt.plot(stockholm_melted["År"], model.predict(stockholm_melted[["År"]]), color='red', linestyle='--', label="Linjär regression")

# Markera prediktionen för 2026
plt.scatter([2026], predicted_skatt, color='green', marker='o', label="Prediktion 2026")

# Diagraminställningar
plt.title("Förutsägelse av skattesats i Stockholm")
plt.xlabel("År")
plt.ylabel("Skattesats")
plt.xticks(range(stockholm_melted["År"].min(), 2027))  # Anpassar axeln
plt.legend()
plt.grid()
plt.show()



