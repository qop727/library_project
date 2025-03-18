# library_project
Lets create web library. MySQL DB, Py Flask BE, Vue.js FE

Vytvorime webovou stranku:
- FE Typescript (vue.js)
- BE Python (flask)
- DB MySQL - na mem druhem pc s linux fedora (klient i server se nachazeji na stejne vnitrni siti)
- nastaveni rest API
- otestovani API pomoci Postman.

- uprostred webove stranky bude zadavaci pole pro vlozeni autora a nazvu knihy, ktera bude ulozena do DB
- pod zadavacim polem bude tlacitko pro ulozeni
- stranka bude komunikovat s uzivatelem vypisovanim provedenych operaci
- na strance bude dalsi tlacitko pro hledani v databazi knih pomoci klicovych slov
- seznam vyhledavanych knih v databazi se zobrazi ve spodni casti stranky

Muj cil:
- je naucit se a pochopit jak technicky funguje system za vyvojem webovych aplikaci
- ucit se s DB
- ucit se rozumet HTML, CSS, JS, TS
- ucit se s PY
- ucit se s Linux Fedora

Shrnutí celého systému:
Backend: Flask API, které přijímá požadavky pro uložení knihy (POST /api/book) a vyhledávání (GET /api/search). Data jsou ukládána do databáze MySQL.
Databáze: MySQL databáze books_db s tabulkou pro knihy.
Frontend: Aplikace ve Vue.js (psaná v TypeScriptu), která obsahuje formulář pro přidání knihy, vyhledávací pole a seznam výsledků. Frontend komunikuje s API pomocí axios.
Serverové prostředí: Oba stroje (klient i server) jsou v rámci stejné interní sítě. Backend spustíte na Fedora serveru a frontend může běžet na vývojovém stroji.