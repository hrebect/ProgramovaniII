import QtQuick 2.14
import QtQuick.Controls 2.14
import QtQml.Models 2.1
import QtLocation 5.14
import QtPositioning 5.14
import QtQuick.Layouts 1.15

RowLayout {

	implicitWidth: 2000	// width on the start of the program
	implicitHeight: 2000	// height on the start of the program
	anchors.fill: parent
    
    // Create property holding model of currently selected city
    property var currentModelItem;
    
    ColumnLayout {
        id: clmn
        Layout.fillHeight: true //full hight
        width: 250
        spacing: 20
        
        CheckBox {
            id: boxCities
            checked: true
            text: qsTr("Města")
        }
        CheckBox {
            id: boxVillage
            checked: true
            text: qsTr("Obce")
        }
        Binding {
                target: MapOfCities
                property: "cities"
                value: boxCities.checked
        }

        Binding {
                target: MapOfCities
                property: "villages"
                value: boxVillage.checked
        }

        Text {
            text: "Počet obyvatel"
            font.family: "Helvetica"
            font.pointSize: 12
        }

       
        RangeSlider {
            id: populationSlider
            Layout.alignment: Qt.AlignHCenter
            from: 0
            to: 1500000

            Component.onCompleted: {
                    populationSlider.setValues(0, 1500000)
            }

        }

        Binding {
                target: MapOfCities
                property: "min_population"
                value: populationSlider.first.value
        }

        Binding {
                target: MapOfCities
                property: "max_population"
                value: populationSlider.second.value
        }
    
        Row {
            width: parent.width
            height: childrenRect.height
                                       
            Text {
                text: "Od: "
                font.family: "Helvetica"
                font.pointSize: 9
            }
            
            TextInput{
                id: popMin
                width:100
                text: populationSlider.first.value
                font.family: "Helvetica"
                font.pointSize: 9
            }                    
               
            Text {
                text: " do: "
                font.family: "Helvetica"
                font.pointSize: 9
            }
            
            TextInput{
                id: popMax
                text: MapOfCities.max_population
                font.family: "Helvetica"
                font.pointSize: 9
            }

            Binding {
                target: MapOfCities
                property: "min_population"
                value: popMin.text
            }

            Binding {
                target: MapOfCities
                property: "max_population"
                value: popMax.text
            }
        }

        Text {
            width: parent.width
            Layout.alignment: Qt.AlignHCenter
            text: "Kraje"
            font.family: "Helvetica"
            font.pointSize: 11
        }

        ComboBox {
            id: comboKraj
            width: parent.width
            Layout.alignment: Qt.AlignHCenter
            model: MapOfCities.kraje
            onActivated: { MapOfCities.loadOkresy()
                comboOkres.model = MapOfCities.okresy}
        }

        Binding {
                    target: MapOfCities
                    property: "kraj_current"
                    value: comboKraj.currentText
        }
      
        Text {
            width: parent.width
            Layout.alignment: Qt.AlignHCenter
            text: "Okresy"
            font.family: "Helvetica"
            font.pointSize: 11
        }

        ComboBox {
            id: comboOkres
            width: parent.width
            Layout.alignment: Qt.AlignHCenter
            model: MapOfCities.okresy
        }

        Binding {
                    target: MapOfCities
                    property: "okres_current"
                    value: comboOkres.currentText
        }
        
        Button {
            id: filter
            width: parent.width
            Layout.alignment: Qt.AlignHCenter
			text: "Filtrovat"
			onClicked: {MapOfCities.filterData()
                        cityList.currentIndex = -1 
                        mapWindow.fitViewportToVisibleMapItems()
            }                    
		}
    }

    Plugin {
        id: mapPlugin
        name: "osm" // We want OpenStreetMap map provider
        PluginParameter {
             name:"osm.mapping.custom.host"
             value: "https://www.openstreetmap.org/#map" //"https://maps.wikimedia.org/osm/"
        }
    }

    Map {   
        id: mapWindow
        Layout.fillWidth: true
        Layout.fillHeight: true
        plugin: mapPlugin
        activeMapType: supportedMapTypes[supportedMapTypes.length-2] // Use our custom tile server
        center: QtPositioning.coordinate(49.74375, 15.338639) //center of Czechia, should be calculated froma actual dataset
        zoomLevel: 8.25 //should be calculated froma actual dataset

        MapItemView {
            model: MapOfCities
            delegate: MapQuickItem {
                coordinate: model.location
                sourceItem: Row {
                    spacing: 5
                    Rectangle {
                        width: 10
                        height:10
                        color: "blue"
                        radius:5
                    }
                    Text {
                        text:  model.display
                        color: {
                                color = "black"
                                if(model.mestoLabel == "město v Česku")
                                    color = "red"
                                }
                        font.bold: {
                                font.bold = false
                                if(model.mestoLabel == "město v Česku")
                                    font.bold = true   
                                }
                    }
                }
            }
        }
    }  
    ListView {

        id: cityList
        width: 200
		Layout.fillHeight: true
        Layout.alignment: Qt.AlignRight       
        currentIndex: -1 //load data with empty current item
        focus: true

        Component {
            id: cityListDelegate
            Item {
                width: childrenRect.width
                height: childrenRect.height +10
        
                Column{
                    Text {
                        text: model.display
                        color:  {
                                color = "black"
                                if(model.mestoLabel == "město v Česku")
                                    color = "red"
                                }
                        font.bold: true

                    }
                    Row{
                        Text{text: "Rozloha: "
                        }

                        Text {
                            textFormat: Text.RichText
                            text: model.area+" km<sup>2</sup>"
                        }
                    }

                    Row{
                        Text{text: "Počet Obyvatel: "
                        }

                        Text {
                            text: model.population
                        }
                    }
                }
                
                MouseArea {
                    anchors.fill: parent
                    onClicked: cityList.currentIndex = index
                }
            }
        }
        
        model: DelegateModel {
            id: cityListDelegateModel
            
            model: MapOfCities
            delegate: cityListDelegate
            
        }
        

        // When current item of the list is changed, update the currentModelItem property, change map zoom        
        onCurrentItemChanged: {currentModelItem = cityListDelegateModel.items.get(cityList.currentIndex).model
                                mapWindow.center =  currentModelItem.location
                                mapWindow.zoomLevel = 12
        }

        highlight: Rectangle {
            color: "lightsteelblue"
        }           
    }
}