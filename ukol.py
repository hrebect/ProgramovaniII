from PySide2.QtCore import QObject, Signal, Slot, Property, QUrl, QAbstractListModel, QByteArray
from PySide2.QtGui import QGuiApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtPositioning import QGeoCoordinate
from PySide2 import QtCore
from enum import Enum
import typing
import sys
import json

VIEW_URL = "ukol_view.qml"  # load GUI
CITY_LIST_FILE = "data.json"


class CityMap(QAbstractListModel):
    class Roles(Enum):
        """Enum with added custom roles"""
        LOCATION = QtCore.Qt.UserRole + 0
        AREA = QtCore.Qt.UserRole + 1
        POPULATION = QtCore.Qt.UserRole + 2
        OKRES = QtCore.Qt.UserRole + 3
        KRAJ = QtCore.Qt.UserRole + 4
        STATUS = QtCore.Qt.UserRole + 5
        LOGO = QtCore.Qt.UserRole + 6

    def __init__(self, filename=None):
        """Initialize and load list from given file"""
        QAbstractListModel.__init__(self)
        self.city_list_all = []
        self.city_list_filtred = []

        # Initialize variables
        self._min_population = 0
        self._max_population = 1500000
        self._min_density = 0
        self._max_density = 2700
        self._cities = True
        self._villages = True
        self._kraje = []
        self._okresy = ['Vše']
        self._kraj_current = 'Vše'
        self._okres_current = 'Vše'
        self._logo = ''

        if filename:
            self.load_from_json(filename)
            self.loadKraje()

    def loadKraje(self):
        # Load regions
        set_kraje = set([d['krajLabel'] for d in self.city_list_all if 'krajLabel' in d])
        self._kraje = list(set_kraje)
        self._kraje.sort()
        self._kraje.insert(0, 'Vše')

    @Slot()
    def loadOkresy(self):
        # Load districts, called from qml
        set_okresy = set([d['okresLabel'] for d in self.city_list_all if
                          ('okresLabel' in d and d['krajLabel'] == self.kraj_current)])
        self._okresy = list(set_okresy)
        self._okresy.sort()
        self._okresy.insert(0, "Vše")

    def load_from_json(self, filename):
        with open(filename, encoding="utf-8") as f:
            self.city_list_all = json.load(f)  # list of all on future

            # Create QGeoCoordinate from the original JSON location
            for c in self.city_list_all:  # list of all in future
                pos = c['location']
                lon, lat = pos.split("(")[1].split(")")[0].split(
                    " ")  # Get the part between brackets and split it on space
                c['location'] = QGeoCoordinate(float(lat), float(
                    lon))  # Create QGeoCoordinate and overwrite original `location` entry

        # Fill data for first open
        self.city_list_filtred = self.city_list_all

    def rowCount(self, parent: QtCore.QModelIndex = ...) -> int:
        """ Return number of cities in the list"""
        return len(self.city_list_filtred)

    def data(self, index: QtCore.QModelIndex, role: int = ...) -> typing.Any:
        """ For given index and role return information of the city"""
        if role == QtCore.Qt.DisplayRole:  # On DisplayRole return name
            return self.city_list_filtred[index.row()]["muniLabel"]
        elif role == self.Roles.LOCATION.value:  # On location role return coordinates
            return self.city_list_filtred[index.row()]["location"]
        elif role == self.Roles.AREA.value:  # On area role return area
            return self.city_list_filtred[index.row()]["area"]
        elif role == self.Roles.POPULATION.value:  # On population role return population
            return self.city_list_filtred[index.row()]["population"]
        elif role == self.Roles.OKRES.value:  # On population role return population
            return self.city_list_filtred[index.row()]["okresLabel"]
        elif role == self.Roles.KRAJ.value:  # On population role return population
            return self.city_list_filtred[index.row()]["krajLabel"]
        elif role == self.Roles.STATUS.value and "mestoLabel" in self.city_list_filtred[
            index.row()]:  # On population role return population
            return self.city_list_filtred[index.row()]["mestoLabel"]
        elif role == self.Roles.LOGO.value and "logo" in self.city_list_filtred[
            index.row()]:  # On population role return population
            return self.city_list_filtred[index.row()]["logo"]

    def roleNames(self) -> typing.Dict[int, QByteArray]:
        """Returns dict with role numbers and role names for default and custom roles together"""
        # Append custom roles to the default roles and give them names for a usage in the QML
        roles = super().roleNames()
        roles[self.Roles.LOCATION.value] = QByteArray(b'location')
        roles[self.Roles.AREA.value] = QByteArray(b'area')
        roles[self.Roles.POPULATION.value] = QByteArray(b'population')
        roles[self.Roles.OKRES.value] = QByteArray(b'okresLabel')
        roles[self.Roles.KRAJ.value] = QByteArray(b'krajLabel')
        roles[self.Roles.STATUS.value] = QByteArray(b'mestoLabel')
        roles[self.Roles.LOGO.value] = QByteArray(b'logo')
        print(roles)
        return roles

    # Getters
    def get_min_population(self):
        return self._min_population

    def get_max_population(self):
        return self._max_population

    def get_min_density(self):
        return self._min_density

    def get_max_density(self):
        return self._max_density

    def get_cities(self):
        return self._cities

    def get_villages(self):
        return self._villages

    def get_kraje(self):
        return self._kraje

    def get_okresy(self):
        return self._okresy

    def get_kraj_current(self):
        return self._kraj_current

    def get_okres_current(self):
        return self._okres_current

    # Setters
    def set_min_population(self, val):
        if val != self._min_population:
            self._min_population = int(val)
            self.min_pop_changed.emit()

    def set_max_population(self, val):
        if val != self._max_population:
            self._max_population = int(val)
            self.max_pop_changed.emit()

    def set_min_density(self, val):
        if val != self._min_density:
            self._min_density = int(val)
            self.min_den_changed.emit()

    def set_max_density(self, val):
        if val != self._max_density:
            self._max_density = int(val)
            self.max_den_changed.emit()

    def set_cities(self, val):
        if val != self._cities:
            self._cities = val
            self.cities_changed.emit()

    def set_villages(self, val):
        if val != self._villages:
            self._villages = val
            self.villages_changed.emit()

    def set_kraj_current(self, val):
        if val != self._kraj_current:
            self._kraj_current = val
            self.kraj_current_changed.emit()

    def set_okres_current(self, val):
        if val != self._okres_current:
            self._okres_current = val
            self.okres_current_changed.emit()

    def clearCities(self) -> None:
        """ Clear all cities and villages from the list"""
        self.beginRemoveRows(self.index(0).parent(), 0, self.rowCount() - 1)
        self.city_list_filtred = []
        self.endRemoveRows()

    # Declare a notification method
    min_pop_changed = Signal()
    max_pop_changed = Signal()
    min_den_changed = Signal()
    max_den_changed = Signal()
    cities_changed = Signal()
    villages_changed = Signal()
    kraj_current_changed = Signal()
    okres_current_changed = Signal()

    min_population = Property(int, get_min_population, set_min_population, notify=min_pop_changed)
    max_population = Property(int, get_max_population, set_max_population, notify=max_pop_changed)
    min_density = Property(int, get_min_density, set_min_density, notify=min_den_changed)
    max_density = Property(int, get_max_density, set_max_density, notify=max_den_changed)
    cities = Property(bool, get_cities, set_cities, notify=cities_changed)
    villages = Property(bool, get_villages, set_villages, notify=villages_changed)
    kraje = Property(list, get_kraje)
    okresy = Property(list, get_okresy)
    kraj_current = Property(str, get_kraj_current, set_kraj_current, notify=kraj_current_changed)
    okres_current = Property(str, get_okres_current, set_okres_current, notify=okres_current_changed)

    # Filter data
    @Slot()
    def filterData(self):

        # Clear all items
        self.clearCities()

        # Create list filtered by population and population density
        city_list_min_max = []
        for feature in self.city_list_all:
            if "population" in feature:
                if self.max_population > int(feature["population"]) > self.min_population:
                    if "area" in feature:
                        density = int(feature["population"]) / float(feature["area"])
                        if self.max_density > density > self.min_density:
                            city_list_min_max.append(feature)

        # Filter list by region
        if self.kraj_current != 'Vše':
            city_list_kraj = [d for d in city_list_min_max if d['krajLabel'] == self.kraj_current]
        else:
            city_list_kraj = city_list_min_max

        # Filter list by district
        if self.okres_current != 'Vše':
            city_list_okres = [d for d in city_list_kraj if d['okresLabel'] == self.okres_current]
        else:
            city_list_okres = city_list_kraj

        # Write filtred list into GUI
        i = 0
        for feature in city_list_okres:

            # Return villiages if wanted
            if self.villages:
                if 'mestoLabel' not in feature:
                    self.beginInsertRows(self.index(0).parent(), i, i)
                    self.city_list_filtred.append(feature)
                    self.endInsertRows()
                    i += 1
            # Return cities if wanted
            if self.cities:
                if 'mestoLabel' in feature and feature['mestoLabel'] == "město v Česku":
                    self.beginInsertRows(self.index(0).parent(), i, i)
                    self.city_list_filtred.append(feature)
                    self.endInsertRows()
                    i += 1


app = QGuiApplication(sys.argv)
view = QQuickView()
url = QUrl(VIEW_URL)

# Create the instance of a CityMap
city_map = CityMap(CITY_LIST_FILE)
# Get the context of the view
ctxt = view.rootContext()

# Set that 'city_map' will be available as 'MapOfCities' property in QML
ctxt.setContextProperty("MapOfCities", city_map)

view.setSource(url)
view.show()
app.exec_()