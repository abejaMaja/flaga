<<<<<<< HEAD
# flaga
=======
# Flaga


#### 1. Login do serwera.

```
ssh nazwa_uzytkownika@adres_ip
```


PS: W trakcie instalacji gdy proces się zatrzymuje z zapytaniem "Do you want to continue? [Y/n]" na końcu, napisz "Y" aby przejść dalej.


### Uprawnienia root dla AWS Ubuntu 18/20 (Nie trzeba tego kroku robić dla VPS z Home i większość innych):
Ustawiamy uprawnienia root ("administratora").


```
sudo passwd # <----- To dla AWS tylkooo!
```
Podaj hasło i zapisz. Wpisz jeszcze poniższe i podaj hasło.
```
su -  # <----- Też tylko dla AWS!! xD
```

Jesteś na serwerze jako root.

PS: w terminalu używaj skrótów:
-> ctrl+shift+c <--- kopiuj w terminalu
-> ctrl+shift+v <--- wklej w terminalu

#### 2. Uaktualniamy paczki (packages).

```
apt update
apt upgrade
```

#### 3. Git.

VPS Ubuntu 18/20 (Home i większość innych):
```
apt install git
cd /var/www
git clone https://github.com/abejaMaja/flaga.git # <--- wklej dokładnie tą linię do terminala
cd flaga
python3 xD.py
```

AWS Ubuntu 18/20 (Home i większość innych):
```
apt install git
mkdir /var/www # <---- to w AWS trzeba zrobić a nie trzeba w VPS (większości)
cd /var/www
git clone https://github.com/abejaMaja/flaga.git
cd flaga
python3 xD.py # <---- z dużej litery xD.py a nie xd.py z małej litery.
```


#### 4. Wewnątrz środowiska (env).

Wszystkie polecenia wykonywane w tym kroku są wykonywane w folderze /var/www/flaga
Napisz
```
pwd
```
aby sprawdzić w jakim katalogu jesteś.


#### Tworzenie i aktywacja środowiska (WAŻNE!):
```
python3 -m venv flagaenv
source flagaenv/bin/activate
```

#### Tworzenie zmiennej:
```
export FLASK_APP=app.py
```

Następnie podaj swoją domenę
```
nano settings.ini
```
wywołując nano albo jed wpisz w nowym pliku po spacji nazwę swojej domeny np (bez "www.") wg wzoru:
```
domena = nazwa_domeny.pl
```

Aby zapisać wciśnij ctrl+s
Aby zamknąć wciśnij ctrl+x


Instalacja wymaganych bibliotek.
```
pip3 install -r requirements.txt
```

Uruchom skrypt przygotowujący hosting w serwerze (1 raz).
```
python3 xd.py
```

#### 5. Restartujemy nginxa i serwisy.

```
systemctl daemon-reload
systemctl restart nginx
systemctl restart flaga.service
```


#### 6. Zmiana napisu.

Będąc w folderze flaga edytujemy zawartość pliku xd.txt.
```
cd /var/www/flaga
nano xd.txt
```

I przeładowujemy stronę.
```
systemctl daemon-reload
systemctl restart nginx
systemctl restart flaga.service
```

#### Jak skońćzysz
Możesz opuścić Terminal pisząć

```
exit
```

Strona nadal będzie stała.


#### Resetowanie środowiska

Zrób to w sytuacji jak coś Ci się zchrzani i będziesz chciał usunąć pliki bo:
a) Masz błąd ze ścieżką gunicorna
b) Zle podałes domenę w setting.ini

[Poprawimy to po streamie]

```
python3 oczysc.py
```
>>>>>>> First commit
