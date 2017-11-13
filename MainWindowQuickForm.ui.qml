import QtQuick 2.4

Item {
    width: 400
    height: 400

    TextInput {
        id: textInput
        x: 40
        y: 48
        width: 80
        height: 20
        text: qsTr("Text Input")
        font.pixelSize: 12
    }
}
