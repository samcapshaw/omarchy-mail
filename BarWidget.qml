import QtQuick
import qs.Ui

BarWidget {
  id: root
  moduleName: "io.github.samcapshaw.mail"
  implicitWidth: button.implicitWidth
  implicitHeight: button.implicitHeight
  WidgetButton {
    id: button
    anchors.fill: parent
    bar: root.bar
    text: "󰇮"
    tooltipText: "Mail for Omarchy"
    onPressed: function(mouseButton) {
      if (mouseButton === Qt.LeftButton && root.bar)
        root.bar.run("omarchy-shell omarchy-mail open")
    }
  }
}
