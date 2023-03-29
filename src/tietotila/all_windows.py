import os
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QApplication, QInputDialog
from PyQt5.QtCore import Qt, QRect, QSize
from PyQt5.QtGui import QPixmap, QColor, QPalette
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QPen, QFont
from PyQt5.QtCore import Qt


class Start(QWidget):
    def __init__(self):
        super().__init__()
        self.logo_path = self.get_logo()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.start_screen = self.create_window()
        self.layout.addWidget(self.start_screen)
        self.setLayout(self.layout)

    def create_window(self):
        pixmap = QPixmap(self.logo_path)
        label = QLabel()
        label.setAlignment(Qt.AlignCenter)
        palette = label.palette()
        palette.setColor(QPalette.Background, QColor("White"))
        label.setAutoFillBackground(True)
        label.setPalette(palette)
        screen_geometry = QApplication.desktop().screenGeometry()
        label.setGeometry(screen_geometry)
        label.setPixmap(pixmap.scaled(label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        return label

    def get_logo(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(os.path.dirname(script_dir))
        resources_dir = os.path.join(parent_dir, 'resources')
        resource_file = os.path.join(resources_dir, 'tietotila_startingscreen.jpg')
        return resource_file

#lisätään central widgettiin ominaisuuksia

class Users(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
    
    def empty(self):
        pass
    
    def new(self):
        pass
    
    def changes(self):
        pass

class Main(QWidget): 
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.label = QLabel("This is the Main screen")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont, QPen, QPainter
from PyQt5.QtWidgets import QApplication, QWidget

class Mindmap(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.master_node = {'name': "master", 'x': 500, 'y': 500, 'color': 'red', 'font_size': 20}
        self.child_nodes = []
        self.connections = []
        self.scale_factor = 1.0
        self.offset_x = 0
        self.offset_y = 0
        self.current_point = None
        self.start_point = None
        self.end_point = None
        self.selected_node = None
        self.drawing_line = False
        self.panning = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        painter.setPen(pen)

        
        for connection in self.connections:
            start_node = connection['start_node']
            end_node = connection['end_node']
            painter.drawLine((start_node['x'] * self.scale_factor) + self.offset_x + start_node['width'] / 2,
                            (start_node['y'] * self.scale_factor) + self.offset_y + start_node['height'] / 2,
                            (end_node['x'] * self.scale_factor) + self.offset_x + end_node['width'] / 2,
                            (end_node['y'] * self.scale_factor) + self.offset_y + end_node['height'] / 2)

    
        self.draw_node(painter, self.master_node)

   
        for child_node in self.child_nodes:
            self.draw_node(painter, child_node)

        if self.start_point is not None and self.drawing_line:
            painter.drawLine(self.start_point, self.current_point)

    def draw_node(self, painter, node):
        font = QFont('SansSerif', node['font_size'])
        painter.setFont(font)
        painter.setBrush(QColor(node['color']))

        x = (node['x'] * self.scale_factor) + self.offset_x
        y = (node['y'] * self.scale_factor) + self.offset_y

    
        max_width = 30000

       
        wrapped_text = painter.fontMetrics().elidedText(node['name'], Qt.TextElideMode.ElideRight, max_width, Qt.TextWordWrap)
        text_rect = painter.fontMetrics().boundingRect(QRect(x, y, max_width, 0), Qt.TextWordWrap | Qt.AlignLeft, wrapped_text)
        text_width = text_rect.width()
        text_height = text_rect.height()

      
        padding = 20
        node['width'] = text_width + padding
        node['height'] = text_height + padding

       
        painter.drawRect(x, y, node['width'], node['height'])

        
        painter.drawText(x + padding / 2, y + padding / 2, max_width, text_height, Qt.AlignLeft | Qt.TextWordWrap, wrapped_text)
    
    
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_point = event.pos()
            self.selected_node = self.get_node_at_position(event.pos())
            if self.selected_node:
                self.drawing_line = True
                self.current_point = event.pos()
            else:
                self.panning = True

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            clicked_node = self.get_node_at_position(event.pos())

            if clicked_node is not None:
                
                input_dialog = QInputDialog(self)
                input_dialog.setWindowTitle("Edit Node Text")
                input_dialog.setLabelText("Enter new text:")
                input_dialog.setTextValue(clicked_node['name'])
                input_dialog.resize(QSize(1200, 2000))  
                ok = input_dialog.exec_()
                new_text = input_dialog.textValue()
                if ok:
                    clicked_node['name'] = new_text
            
            else:
                
                new_node = {'name': 'New Node',
                            'x': (event.x() - self.offset_x) / self.scale_factor - 50,
                            'y': (event.y() - self.offset_y) / self.scale_factor - 50,
                            'color': 'white',
                            'font_size': 16}
                self.child_nodes.append(new_node)

            self.update()

    def mouseMoveEvent(self, event):
        self.current_point = event.pos()
        if self.selected_node is not None and not self.drawing_line and not self.panning:
            self.selected_node['x'] = (event.x() - self.offset_x) / self.scale_factor - 50
            self.selected_node['y'] = (event.y() - self.offset_y) / self.scale_factor - 50
        elif self.panning:
            self.offset_x += event.x() - self.start_point.x()
            self.offset_y += event.y() - self.start_point.y()
            self.start_point = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.end_point = event.pos()
            if self.drawing_line:
                target_node = self.get_node_at_position(event.pos())
                if target_node is not None and target_node != self.selected_node:
                    self.connections.append({'start_node': self.selected_node, 'end_node': target_node})
                self.drawing_line = False
            self.panning = False
            self.update()

    def wheelEvent(self, event): 
        angle = event.angleDelta().y()
        if angle > 0:
            self.scale_factor *= 1.5
        else:
            self.scale_factor *= 0.9
        self.update()

    def get_node_at_position(self, pos):
        for node in [self.master_node] + self.child_nodes:
            x, y, size = (node['x'] * self.scale_factor) + self.offset_x, (node['y'] * self.scale_factor) + self.offset_y, 100 * self.scale_factor
            if x <= pos.x() <= x + size and y <= pos.y() <= y + size:
                return node
        return None

