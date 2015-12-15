###############################################################################
# Copyright (c) 2004, 2015  Ericsson AB
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v1.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v10.html
#
# Contributor: david.ferenc.vranics@ericsson.com
###############################################################################

#try to import Qt
try:
  import sys
  
  from PyQt4.QtGui import *
  from PyQt4.QtCore import *
except:
  print "\nPlease install python-qt4 package!\n"
  sys.exit(1)

################################################

class CloseEdit(QWidget):
  def __init__(self, parent = None):
    super(CloseEdit, self).__init__(parent)
    
    self.packetType = "close"
    
    self.vLayout = QVBoxLayout()

    self.label = QLabel("Packet contents:")
    self.packetEdit = QTextEdit()
    self.packetEdit.setPlainText("\
client_id := omit")
   
    self.vLayout.addWidget(self.label)
    self.vLayout.addWidget(self.packetEdit)
    
    self.setLayout(self.vLayout)
    
  #this should convert things to text
  def serialize(self, param = None):
    offset = "          "
    s = ""
    s = s + offset + "HTTPMessageType :=\n"
    s = s + offset + "{\n"
    s = s + offset + "  " + "close :=\n"
    s = s + offset + "  " + "{\n"
    s = s + offset + "    " + str(self.packetEdit.toPlainText()).replace("\n", "\n    " + offset) + "\n"
    s = s + offset + "  " + "}\n"
    s = s + offset + "}\n"
    return s
