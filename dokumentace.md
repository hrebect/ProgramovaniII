### Dokumentace
## Struktura
Aplikace Prohlížeč měst a obcí se skládá za 2 částí. V souboru `ukol.py` se nachází třídy a metody, které komunikují s grafickým rozhraním definovaným v souboru `ukol_view.qml`.
## ukol.py
V tříde `Roles` jsou definovány role, které slouží ke vytvoření vlstních rolí, které jsou posléze přiřazeny pomocí funkce `data` a `roleNames` k datů. Data jsou nahrávány pomocí funkce `load_from_json`, která načítá vtupní data ve formátu .json.
V následující části jsou funkce `get` a `set` jednotlivých proměnných. z nich jsou potoé vytvořeny `Properties`, pro načítání proměnných v souboru `ukol_view.qml`. `min_population` a `max_population` nesou informaci o maximálním a minimálním počtu obyvatel, `min_density` a `max_density` nesou informace o hustotě obyvatelstva, property `cities` a `villages` nesou informaci o nastavení filteru, `kraje` obsahuje list názvů krajů, `okresy` obsahují list okresů v jednotlivých krajích, `kraj_current` a `okres_curren` nesou informaci a aktuálně zvoleném kraji a okresu, kterými se mají data filtrovat.

Funkce `filterData` Zajišťuje upravu původních dat pomocí zvolených parametrů filtru.
