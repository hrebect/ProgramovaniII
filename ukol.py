from PySide2.QtCore import QObject, Signal, Slot, Property, QUrl, QAbstractListModel, QByteArray
from PySide2.QtGui import QGuiApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtPositioning import QGeoCoordinate
from PySide2 import QtCore
from enum import Enum
import typing
import sys
import json

VIEW_URL = "ukol_view.qml"   # load GUI
CITY_LIST_FILE = "data.json"

class CityMap(QAbstractListModel):

    class Roles(Enum):
        """Enum with added custom roles"""
        LOCATION = QtCore.Qt.UserRole+0
        AREA = QtCore.Qt.UserRole+1
        POPULATION = QtCore.Qt.UserRole+2
        OKRES = QtCore.Qt.UserRole+3
        KRAJ = QtCore.Qt.UserRole+4
        STATUS = QtCore.Qt.UserRole+5
    
    def __init__(self,filename=None):
        """Initialize and load list from given file"""
        QAbstractListModel.__init__(self)
        self.city_list_all = []
        self.city_list_filtred = []
        
        # Min and max Value
        self._min_population = 0
        self._max_population = 1500000
        self._cities = True
        self._villages = True                
        
        if filename:
            self.load_from_json(filename)
       


    def load_from_json(self,filename):
        with open(filename,encoding="utf-8") as f:
            self.city_list_all = json.load(f)  #list of all on future

            # Create QGeoCoordinate from the original JSON location
            for c in self.city_list_all:  #list of all in future
                pos = c['location']
                lon,lat = pos.split("(")[1].split(")")[0].split(" ") # Get the part between brackets and split it on space
                c['location'] = QGeoCoordinate(float(lat),float(lon)) # Create QGeoCoordinate and overwrite original `location` entry
        
         
        

    def rowCount(self, parent:QtCore.QModelIndex=...) -> int:
        """ Return number of cities in the list"""
        return len(self.city_list_filtred)

    def data(self, index:QtCore.QModelIndex, role:int=...) -> typing.Any:
        """ For given index and role return information of the city"""
        if role == QtCore.Qt.DisplayRole: # On DisplayRole return name
            return self.city_list_filtred[index.row()]["muniLabel"]
        elif role == self.Roles.LOCATION.value: # On location role return coordinates
            return self.city_list_filtred[index.row()]["location"]
        elif role == self.Roles.AREA.value: # On area role return area
            return self.city_list_filtred[index.row()]["area"]
        elif role == self.Roles.POPULATION.value: # On population role return population
            return self.city_list_filtred[index.row()]["population"]
        elif role == self.Roles.OKRES.value: # On population role return population
            return self.city_list_filtred[index.row()]["okresLabel"]
        elif role == self.Roles.KRAJ.value: # On population role return population
            return self.city_list_filtred[index.row()]["krajLabel"]
        elif role == self.Roles.STATUS.value: # On population role return population
            return self.city_list_filtred[index.row()]["mestoLabel"]

        
            
     
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
        print(roles)
        return roles
    
    # Getters
    def get_min_population(self):
        return self._min_population

    def get_max_population(self):
        return self._max_population

    def get_cities(self):
        return self._cities

    def get_villages(self):
        return self._villages


    # Setters
    def set_min_population(self, val):
        if val != self._min_population:
            self._min_population = val
            self.min_pop_changed.emit()
    
    def set_max_population(self, val):
        if val != self._max_population:
            self._max_population = val
            self.max_pop_changed.emit()

    def set_cities(self, val):
        if val != self._cities:
            self._cities = val
            self.cities_changed.emit()

    def set_villages(self, val):
        if val != self._villages:
            self._villages = val
            self.villages_changed.emit()
    
    def clearCities(self) -> None:
        """ Clear all cities and villages from the list"""
        self.beginRemoveRows(self.index(0).parent(), 0, self.rowCount()-1)
        self.city_list_filtred = []
        self.endRemoveRows()        
    
    # Declare a notification method        
    min_pop_changed = Signal()
    max_pop_changed = Signal()
    cities_changed = Signal()
    villages_changed = cities_changed

    min_population = Property(int, get_min_population, set_min_population, notify=min_pop_changed)
    max_population = Property(int, get_max_population, set_max_population, notify=max_pop_changed)
    cities = Property(bool, get_cities, set_cities, notify=cities_changed)
    villages = Property(bool, get_villages, set_villages, notify=villages_changed)

    



    # Filter data
    @Slot()
    def filterData(self):

        self.clearCities()

        i = 0


        for feature in self.city_list_all:

            self.beginInsertRows(self.index(0).parent(), i, i)
            self.city_list_filtred.append(feature)
            self.endInsertRows()
            i +=1

       

app = QGuiApplication(sys.argv)
view = QQuickView()
url = QUrl(VIEW_URL)

# Create the instance of a CityMap
city_map = CityMap(CITY_LIST_FILE)
# Get the context of the view
ctxt = view.rootContext()

# Set that 'city_map' will be available as 'MapOfCities' property in QML
ctxt.setContextProperty("MapOfCities",city_map)

view.setSource(url)
view.show()
app.exec_()