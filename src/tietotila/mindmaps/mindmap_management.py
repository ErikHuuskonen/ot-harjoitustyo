"""
Tämä moduuli toimii valmiissa versiossa sovelluslogiikan moduulina
"""
import pickle
import os
from src.tietotila.mindmaps.mindmap_screen import MindMap, Node


class MindmapManagement(MindMap):
    """
    Luokka metodeille joilla johdetaan mindmapscreen toimintoja
    """

    def list_to_dict(self):
        """
        Muuttaa jokaisen self.nodes listassa olevan Node olion sanakirjaksi
        ja lisää tämän sanakirjan uuteen listaan node_history.
        """
        node_history = []
        line_history = []
        for node in self.nodes:
            node_dict = {
                'x': node.x,
                'y': node.y,
                'text': node.text
            }
            node_history.append(node_dict)
        for line in self.lines:
            coords = self.canvas.coords(line)
            line_dict = {
                'x1': coords[0],
                'y1': coords[1],
                'x2': coords[2],
                'y2': coords[3]
            }
            line_history.append(line_dict)
        return node_history, line_history

    def save_nodes_and_lines_to_file(self, file_path):
        """
        Tallentaa solmujen ja viivojen tiedot pickle-tiedostoon.
        
        Args:
            file_path: 
                Merkkijono, joka määrittää tiedoston sijainnin, johon solmujen ja viivojen tiedot tallennetaan.
        """
        nodes_history, lines_history = MindmapManagement.list_to_dict(self)
        with open(file_path, "wb") as f:
            pickle.dump({"nodes": nodes_history, "lines": lines_history}, f)

    def load_nodes_and_lines_from_file(self, file_path):
        """
        Lataa solmujen ja viivojen tiedot pickle-tiedostosta ja luo niistä Node-olioita.
        
        Args:
            file_path: 
                Merkkijono, joka määrittää tiedoston sijainnin, josta solmujen ja viivojen tiedot ladataan.
        """
        if file_path is None:
            current_file_path = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(
                current_file_path, "history", self.user, f"{self.folder}.pickle")
        try:
            with open(file_path, "rb") as f:
                data = pickle.load(f)
        except (FileNotFoundError, EOFError, pickle.UnpicklingError):
            print("Tiedosto on tyhjä, ei syytä huoleen.")
            data = {"nodes": [], "lines": []}
        nodes_history = data["nodes"]
        lines_history = data["lines"]
        self.nodes = []
        for node_dict in nodes_history:
            node = Node(
                self.canvas, node_dict["x"], node_dict["y"], node_dict["text"])
            self.nodes.append(node)
        self.lines = []
        for line_dict in lines_history:
            start_node = self.nodes[line_dict["start_node_index"]]
            end_node = self.nodes[line_dict["end_node_index"]]
            line = self.canvas.create_line(
                start_node.x, start_node.y, end_node.x, end_node.y)
            self.lines.append(line)
