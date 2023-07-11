## Hledání volných polch svahů
Program `calculate_slope.py` načítá 2 vstupní parametry: 
1) digitální model terénu `--terrain <jmeno_souboru>`
2) digitální model povrchu `--surface <jmeno_souboru>`.

Na začátku jsou stanoveny 2 konstanty: limit maximálního rozdílu výšek mezi rastry, který stanovuje případ, kdy pixely ještě považujeme za totožné,
a velikost kroku, tj. šířku a výšku rastrového okna, s nímž program počítá v jedné iteraci tak, aby se data během výpočtu vešly do RAM.

Limit rozdílu výšek byl stanoven
na 10 cm, velikost rastrového okna pak na 512x512 pixelů. Po načtení vstupních rastrů program vypočítá průnik jejich ohraničujících obdélníků. 
Následně v oblasti tohoto průniku začne postupně načítat oba rastry po oknech.V každém okně nejdřív dojde k výpočtu rozdílu mezi oběma rastry, 
tam kde rozdíl nepřesahuje stanovený limit, považujeme rastry za shodné, pomocí čehož se vytvoří maska. Následně dojde k výpočtu sklonu získáním hodnot gradientů v obou osách 
a z nich potom vypočítáním úhlu. Poté už se jen na matici hodnot sklonů aplikuje maska tak, aby byl sklon definovaný pouze tam, kde jsou oba rastry shodné. 
Nakonec se jak matice masky, tak sklonů zapíše do nově vznikajících rastrů.
