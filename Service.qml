import QtQuick
import Quickshell
import Quickshell.Io

Scope {
  id: root
  property var shell: null
  property var manifest: null
  readonly property string sourceDir: decodeURIComponent(Qt.resolvedUrl(".").toString().replace(/^file:\/\//, ""))
  function open() {
    Quickshell.execDetached(["python3", sourceDir + "/launch.py"])
  }
  IpcHandler {
    target: "omarchy-mail"
    function open(): void { root.open() }
  }
}
