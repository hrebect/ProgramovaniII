### Dokumentace
## Struktura
Aplikace Prohlížeč měst a obcí se skládá za 2 částí. V souboru `ukol.py` se nachází třídy a metody, které komunikují s grafickým rozhraním definovaným v souboru `ukol_view.qml`.
## ukol.py
V tříde `Roles` jsou definovány role, které slouží ke vytvoření vlstních rolí, které jsou posléze přiřazeny pomocí funkce `data` a `roleNames` k datů. Data jsou nahrávány pomocí funkce `load_from_json`, která načítá vtupní data ve formátu .json.
V následující části jsou funkce `get` a `set` jednotlivých proměnných. z nich jsou potoé vytvořeny `Properties`, pro načítání proměnných v souboru `ukol_view.qml`. `min_population` a `max_population` nesou informaci o maximálním a minimálním počtu obyvatel, `min_density` a `max_density` nesou informace o hustotě obyvatelstva, property `cities` a `villages` nesou informaci o nastavení filteru, `kraje` obsahuje list názvů krajů, `okresy` obsahují list okresů v jednotlivých krajích, `kraj_current` a `okres_curren` nesou informaci a aktuálně zvoleném kraji a okresu, kterými se mají data filtrovat.

Funkce `filterData` Zajišťuje upravu původních dat pomocí zvolených parametrů filtru.

## ukol_view.qml
Uživatelské rozhraní je rozděleno na 3 hlaví sloupce pomocí `RowLayout`. V prvním sloupci je položka `ColumnLayout` s kompletním nastavením filteru, v druhém sloupci se nachází mapové pole `Map` a v posledním sloupci je položka `ListView` se seznamem jednotlivých měst.
Výběr filtru na města/obce je zajištěn pomocí `ChecBox`, které jsou propojeny s property `cities` a `villages`. Výběr počtu a hustoty obyvtel je zajištěn pomocí `RangedSlider`, které jsou napojeny  `min_population`, `max_population`, `min_density` a `max_density`. Výběr okresu a kraje je pomocí `ComoBox`, který komunikuje s `kraje` a `okresy`, pro načítání aktuálních seznamů a s `kraj_current` a `okres_curren` pro ukládání zvoleného parametru.

Spuštění samotného filtrování je zajištěno `Button`, které spouští funkci `filterData`. výsledek je poté vyzualizován v mapovém poly a v seznamu. Mapové pole používá jako podlkald mapy se serveru OpenStreetMap. v seznamu `ListView` lze pomocí komponenty `MouseArea` zvolit konkrétní obec.
