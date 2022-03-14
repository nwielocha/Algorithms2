// Czarnych musi być wszedzie tyle samo
// wartownicy też wliczaja sie jako czarne
// 1. każdy węzeł mam przypisany kolor: czerwony lub czarny
// 2. korzeń jest czarny
// 3. liście są czarne; przyjmujemy wariant drzewa z
// wartownikami - liśćmi są wartownicy
// 4. czerwony węzeł nie może mieć czerwonego syna
// 5. na każdej ścieżce od korzenia do liści jest tyle samo
// czarnych węzłów

#include <iostream>
using namespace std;

struct wezel {
    int kolor;
    int klucz;
    wezel *lewy;
    wezel *prawy;
    wezel *ojciec;
};

struct wezel *root;

void left_rotate();

void dodaj_wezel(int n) {
    struct wezel* aktualny = root;
    struct wezel* dodawany = new wezel;
    dodawany->klucz = n;
    dodawany->lewy = NULL;
    dodawany->prawy = NULL;
    if (root == NULL) {
        dodawany->ojciec = NULL;
        root = dodawany;
        return;
    }
    else
    {
        while (aktualny != NULL) {
            if (aktualny->klucz == dodawany->klucz) {
                aktualny->kolor++;
                return;
            }
            if (aktualny->klucz < dodawany->klucz) {
                if (aktualny->prawy == NULL) {
                    dodawany->ojciec = aktualny;
                    aktualny->prawy = dodawany;
                    return;
                }
                else {
                    aktualny = aktualny->prawy;
                }
            }
            if (aktualny->klucz > dodawany->klucz) {
                if (aktualny->lewy == NULL) {
                    dodawany->ojciec = aktualny;
                    aktualny->lewy = dodawany;
                    return;
                }
                else {
                    aktualny = aktualny->lewy;
                }
            }
        }
    }
}

struct wezel* usun_klucz(struct wezel* wezel, int szukany) {
    if (wezel == NULL) {
        return wezel;
    }
    if (szukany < wezel->klucz) {
        return wezel->lewy = usun_klucz(wezel->lewy, szukany);
    }
    else if (szukany > wezel->klucz) {
        return wezel->prawy = usun_klucz(wezel->prawy, szukany);
    }
    if (szukany == wezel->klucz) {
        if (wezel->ile == 1) {
            if (root->lewy == NULL && root->prawy == NULL) {
                delete(root);
                root = nullptr;
                return nullptr;
            }
            if (wezel->lewy == nullptr) {
                struct wezel* tmp = wezel->prawy;
                delete(wezel);
                return tmp;
            }
            else if (wezel->prawy == nullptr) {
                struct wezel* tmp = wezel->lewy;
                delete(wezel);
                return tmp;
            }
            struct wezel* tmp = wezel->prawy;
            wezel->klucz = tmp->klucz;
            wezel->kolor = tmp->kolor;
            while (tmp->lewy != nullptr) {
                tmp = tmp->lewy;
            }
            wezel->prawy = usun_klucz(wezel->prawy, tmp->klucz);
        }
        else {
            wezel->kolor = wezel->kolor - 1;
        }
        
    }
    return wezel;
}
void szukaj_klucz(struct  wezel* wezel, int szukany) {
    int ojciec = 0;
    int lewy = 0;
    int prawy = 0;
    if (wezel->klucz == szukany)
    {
        if (wezel->ojciec != NULL) {
            struct wezel* tmp = wezel->ojciec;
            ojciec = tmp->klucz;
        }
        if (wezel->lewy != NULL) {
            struct wezel* tmp = wezel->lewy;
            lewy = tmp->klucz;
        }
        if (wezel->prawy != NULL) {
            struct wezel* tmp = wezel->prawy;
            prawy = tmp->klucz;
        }
        
        cout << "Znaleziono klucz: " << wezel->klucz << endl << "Powtorzenia: " << wezel->kolor << endl << "Ojciec: " << ojciec << endl << "Prawy syn: " << prawy << endl << "Lewy syn: " << lewy << endl;
    }
    else if (wezel->klucz > szukany && wezel->lewy != NULL)
        szukaj_klucz(wezel->lewy, szukany);
    else if (wezel->klucz < szukany && wezel->prawy != NULL)
        szukaj_klucz(wezel->prawy, szukany);
 }
void drukowanie(struct wezel* wezel)
{
    if (wezel->lewy != NULL) {
        drukowanie(wezel->lewy);
    }
    cout << endl << wezel->klucz << "[" << wezel->kolor << "]" << endl;
    if (wezel->prawy != NULL) {
        drukowanie(wezel->prawy);
    }
}

int main()
{
    int dziala = 1;
    int odp, dane;
    while (dziala == 1) {
        cout << endl;
        cout << "Co chcesz zrobić?(1.Dodaj/2.Usun/3.Szukaj/4.Drukuj/5.Wyjdz)" << endl;
        cin >> odp;
        cout << endl;
        switch (odp) {
        case 1: {
            cout << "Wprowadz klucz: " << endl;
            cin >> dane;
            dodaj_wezel(dane);
            break;
        }
        case 2: {
            cout << "Wprowadz klucz: " << endl;
            cin >> dane;
            if (root == NULL) {
                cout << "NIE MA NIC DO USUNIECIA" << endl;
            }
            else {
                usun_klucz(root, dane);
            }
            break;
        }
        case 3: {
            cout << "Wprowadz szukany klucz: " << endl;
            cin >> dane;
            if (root == NULL) {
                cout << "NIE MA NIC DO PRZESZUKANIA" << endl;
            }
            else {
                szukaj_klucz(root, dane);
            }
            break;
            
        }
        case 4: {
            if (root == NULL) {
                cout << "NIE MA NIC DO DRUKOWANIA" << endl;
            }
            else {
                drukowanie(root);
            }
            break;
        }
        case 5: {
            dziala = 0;
            break;
        }
        }
    }
    return 0;
}