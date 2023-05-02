import tkinter as tk
from tkinter import simpledialog
from mindmapmanagement import MindmapManagement


class Node:
    """
    Node on solmu miellekartassa, joka liittyy pakan tietoihin.
    """

    def __init__(self, canvas, x, y, text):
        """
        Luo uuden solmun ja alustaa sen koordinaatit, tekstin ja pakan.
        """
        self.canvas = canvas
        width = 80
        height = 120
        self.id = canvas.create_rectangle(
            x - width / 2, y - height / 2, x + width / 2, y + height / 2, fill='black', outline='black', width=2)
        self.text_id = canvas.create_text(x, y, text=text, font=('Arial', 12))
        self.x = x
        self.y = y
        self.text = text


class MindMap:
    """
    MindMap on miellekartta, joka koostuu solmuista ja niiden välisistä viivoista.
    """

    def __init__(self, master):
        """
        Alustaa miellekartan ja lisää solmut sekä viivat.
        """
        self.master = master
        self.canvas = tk.Canvas(master, width=1000, height=1200, bg='white')
        self.canvas.pack(fill='both', expand=True)
        self.canvas.pack_forget()
        self.nodes = []
        self.lines = []
        self.master_node = Node(self.canvas, 500, 600, "Master Node")
        self.nodes.append(self.master_node)
        self.canvas.bind('<Double-Button-1>', self.on_double_click)
        self.canvas.bind_all('<MouseWheel>', self.zoom)
        self.canvas.bind_all('<Button-4>', self.zoom)
        self.canvas.bind_all('<Button-5>', self.zoom)
        self.canvas.bind('<Button-1>', self.on_left_button_click)
        self.canvas.bind('<B1-Motion>', self.on_left_button_motion)
        self.canvas.bind('<ButtonRelease-1>', self.on_left_button_release)
        self.canvas.bind('<Shift-Button-1>', self.move_node_start)
        self.canvas.bind('<Shift-B1-Motion>', self.move_node)
        self.canvas.bind('<Shift-ButtonRelease-1>', self.move_node_stop)
        self.line_start_node = None
        self.current_line = None
        self.moving_node = None
        self.drag_data = {"x": 0, "y": 0}

    def create_node(self, event):
        """
        Luo uuden solmun ja lisää sen miellekarttaan.
        """
        x, y = event.x, event.y
        text = simpledialog.askstring('Node Text', 'Enter node text:')
        if text:
            node = Node(self.canvas, x, y, text)
            self.nodes.append(node)
            self.get_history()

    def get_node(self, x, y):
        """
        Palauttaa solmun annetuilla koordinaateilla, jos sellainen on olemassa.
        """
        for node in self.nodes:
            if (x > node.x - 80 / 2) and (x < node.x + 80 / 2) and (y > node.y - 120 / 2) and (y < node.y + 120 / 2):
                return node
        return None

    def on_left_button_click(self, event):
        """
        Aloittaa viivan piirtämisen tai aloittaa liikkumisen.
        """
        node = self.get_node(event.x, event.y)
        if node:
            self.line_start_node = node
            self.current_line = self.canvas.create_line(
                node.x, node.y, event.x, event.y, fill='black', width=2)
        else:
            self.drag_data["x"] = event.x
            self.drag_data["y"] = event.y

    def on_left_button_motion(self, event):
        """
        Päivittää viivan piirtämistä tai liikuttaa miellekarttaa.
        """
        if self.line_start_node and self.current_line:
            self.canvas.coords(self.current_line, self.line_start_node.x,
                               self.line_start_node.y, event.x, event.y)
        else:
            delta_x = event.x - self.drag_data["x"]
            delta_y = event.y - self.drag_data["y"]
            self.canvas.move(tk.ALL, delta_x, delta_y)
            self.drag_data["x"] = event.x
            self.drag_data["y"] = event.y

    def on_left_button_release(self, event):
        """
        Lopettaa viivan piirtämisen tai liikkumisen.
        """
        if self.line_start_node and self.current_line:
            node = self.get_node(event.x, event.y)
            if node and node != self.line_start_node:
                self.canvas.coords(
                    self.current_line, self.line_start_node.x, self.line_start_node.y, node.x, node.y)
                self.lines.append(self.current_line)

            else:
                self.canvas.delete(self.current_line)
            self.line_start_node = None
            self.current_line = None

    def zoom(self, event):
        """
        Zoomaa miellekarttaa sisään tai ulos.
        """
        if event.num == 4 or event.delta > 0:
            factor = 1.1
        else:
            factor = 0.9
        x, y = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
        self.canvas.scale('all', x, y, factor, factor)

    def move_node_start(self, event):
        """
        Aloittaa solmun siirtämisen.
        """
        node = self.get_node(event.x, event.y)
        if node:
            self.moving_node = node

    def move_node(self, event):
        """
        Siirtää solmua.
        """
        if self.moving_node:
            dx = event.x - self.moving_node.x
            dy = event.y - self.moving_node.y
            self.canvas.move(self.moving_node.id, dx, dy)
            self.canvas.move(self.moving_node.text_id, dx, dy)
            self.moving_node.x = event.x
            self.moving_node.y = event.y
            for line_id in self.lines:
                coords = self.canvas.coords(line_id)
                if (coords[0], coords[1]) == (self.moving_node.x - dx, self.moving_node.y - dy):
                    self.canvas.coords(
                        line_id, self.moving_node.x, self.moving_node.y, coords[2], coords[3])
                elif (coords[2], coords[3]) == (self.moving_node.x - dx, self.moving_node.y - dy):
                    self.canvas.coords(
                        line_id, coords[0], coords[1], self.moving_node.x, self.moving_node.y)

    def move_node_stop(self, event):
        """
        Lopettaa solmun siirtämisen.
        """
        self.moving_node = None

    def on_double_click(self, event):
        """
        Näyttää solmun pakan sisällön tai luo uuden solmun.
        """
        node = self.get_node(event.x, event.y)
        if node:
            node.show_deck()
        else:
            self.create_node(event)


if __name__ == "__main__":
    root = tk.Tk()
    app = MindMap(master=root)
    # add this line to pack the canvas
    app.canvas.pack(fill='both', expand=True)
    root.mainloop()


# tässä olevat muutokset astuvat voimaan mindmapscreen tiedostossa
