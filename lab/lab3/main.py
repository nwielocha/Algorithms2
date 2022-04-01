# Przygotuj program znajdujący najdłuższy wspólny podciąg korzystający z programowania dynamicznego.
# Program powinien dać do wyboru: odczyt ciągów wejściowych z konsoli lub z dwóch różnych plików tekstowych.
# Program powinien drukować tablicę pomocniczą wraz z odpowiednim oznaczeniem przejść (ta funkcjonalność przyda się na sprawdzianie)
# Zadanie należy przesłać najpóźniej do najbliższej niedzieli włącznie na adres bartlomiej.pawelski@ug.edu.pl

def lcs(X, Y):
    m = len(X)
    n = len(Y)
    L = [[0 for i in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    index = L[m][n]
    lcs = [""] * (index+1)
    lcs[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs[index - 1] = X[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1

    print("LCS of " + X + " and " + Y + " is " + "".join(lcs))
    for i in range(m+1):
        print(L[i])


X = "abaabbaaa"
Y = "babab"
lcs(X, Y)
