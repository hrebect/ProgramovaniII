import QtQuick 2.14
import QtQuick.Controls 2.14
import QtQml.Models 2.1
import QtLocation 5.14
import QtPositioning 5.14
import QtQuick.Layouts 1.15



RowLayout {

	implicitWidth: 2000	// width on the start of the program
	implicitHeight: 2000	// height on the start of the program
    //Layout.fillHeight: true 
    
	anchors.fill: parent
    

    // Create property holding model of currently selected city
    property var currentModelItem;
    
    

    ColumnLayout {
        id: clmn
        //height: parent.height
        Layout.fillHeight: true //full hight
        //Layout.alignment: Qt.AlignHCenter
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
            first.value: MapOfCities.min_population
            second.value: MapOfCities.max_population

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
            model: ["Vše","Jihočeský", "Jihomoravský", "Karlovarský", "Královéhradecký", "Liberecký", "Moravskoslezský", "Olomoucký", "Pardubický", "Plzeňský", "Praha", "Středočeský", "Ústecký", "Vysočina", "Zlínský"]
            onActivated: {
                    if (currentIndex == 1)
                        comboOkres.model = ["Vše", "České Budějovice", "Český Krumlov", "Jindřichův Hradec", "Písek", "Prachatice", "Strakonice", "Tábor"]
                    if (currentIndex == 2)
                        comboOkres.model = ["Vše", "Blansko", "Brno-město", "Brno-venkov", "Břeclav", "Hodonín", "Vyškov", "Znojmo"]
                    if (currentIndex == 3)
                        comboOkres.model = ["Vše", "Cheb", "Karlovy Vary", "Sokolov"]
                    if (currentIndex == 4)
                        comboOkres.model = ["Vše", "Hradec Králové", "Jičín", "Náchod", "Rychnov nad Kněžnou", "Trutnov"]
                    if (currentIndex == 5)
                        comboOkres.model = ["Vše", "Česká Lípa", "Jablonec nad Nisou", "Liberec", "Semily"]
                    if (currentIndex == 6)
                        comboOkres.model = ["Vše", "Bruntál", "Frýdek-Místek", "Karviná", "Nový Jičín", "Opava", "Ostrava-město"]
                    if (currentIndex == 7)
                        comboOkres.model = ["Vše", "Jeseník", "Olomouc", "Prostějov", "Přerov", "Šumperk"]
                    if (currentIndex == 8)
                        comboOkres.model = ["Vše", "Chrudim", "Pardubice", "Svitavy", "Ústí nad Orlicí"]
                    if (currentIndex == 9)
                        comboOkres.model = ["Vše", "Domažlice", "Klatovy", "Plzeň-jih", "Plzeň-město", "Plzeň-sever", "Rokycany", "Tachov"]
                    if (currentIndex == 10)
                        comboOkres.model = ["Vše","Praha"]
                    if (currentIndex == 11)
                        comboOkres.model = ["Vše", "Benešov", "Beroun", "Kladno", "Kolín", "Kutná Hora", "Mělník", "Mladá Boleslav", "Nymburk", "Praha-východ", "Praha-západ", "Příbram", "Rakovník"]
                    if (currentIndex == 12)
                        comboOkres.model = ["Vše", "Děčín", "Chomutov", "Litoměřice", "Louny", "Most", "Teplice", "Ústí nad Labem"]
                    if (currentIndex == 13)
                        comboOkres.model = ["Vše", "Havlíčkův Brod", "Jihlava", "Pelhřimov", "Třebíč", "Žďár nad Sázavou"]
                    if (currentIndex == 14)
                        comboOkres.model = ["Vše", "Kroměříž", "Uherské Hradiště", "Vsetín", "Zlín"]                      
                }
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
            model: ["Vše"]
        }


        

        Button {
            id: filter
            width: parent.width
            Layout.alignment: Qt.AlignHCenter
			text: "Filtrovat"
			onClicked: MapOfCities.filterData()

		}


    }

    Plugin {
        id: mapPlugin
        name: "osm" // We want OpenStreetMap map provider
        PluginParameter {
             name:"osm.mapping.custom.host"
             value:"https://maps.wikimedia.org/osm/" // We want custom tile server for tiles without labels
        }
    }

    Map {
        
        id: mapWindow
        Layout.fillWidth: true
        Layout.fillHeight: true
            

        plugin: mapPlugin
        activeMapType: supportedMapTypes[supportedMapTypes.length -2] // Use our custom tile server

        center: currentModelItem.location // Center to the selected city
        zoomLevel: 12

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

        // When current item of the list is changed, update the currentModelItem property
        onCurrentItemChanged: currentModelItem = cityListDelegateModel.items.get(cityList.currentIndex).model

        highlight: Rectangle {
            color: "lightsteelblue"
        }

        
           
    }

}