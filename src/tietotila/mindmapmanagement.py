"""
Tämä moduuli toimii valmiissa versiossa sovelluslogiikan moduulina
"""
import pickle
import os
from mindmapscreen import MindMap, Deck, Card, Node


class MindmapManagement(MindMap, Deck, Card):
    """
    uokka metodeille joilla johdetaan mindmapscreen toimintoja
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

    def save_nodes_and_lines_to_file(self, file_path=None):
        """
        Tallentaa solmujen ja viivojen tiedot pickle-tiedostoon.
        """
        if file_path is None:
            current_file_path = os.path.dirname(os.path.abspath(__file__))
            user_folder_path = os.path.join(
                current_file_path, "history", self.user)
            os.makedirs(user_folder_path, exist_ok=True)
            file_path = os.path.join(user_folder_path, f"{self.folder}.pickle")

        nodes_history = self.nodes_to_dict()
        lines_history = self.lines_to_dict()

        with open(file_path, "wb") as f:
            pickle.dump({"nodes": nodes_history, "lines": lines_history}, f)

    def load_nodes_and_lines_from_file(self, file_path=None):
        """
        Lataa solmujen ja viivojen tiedot pickle-tiedostosta ja luo niistä Node-olioita.
        """
        if file_path is None:
            current_file_path = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(
                current_file_path, "history", self.user, f"{self.folder}.pickle")

        try:
            with open(file_path, "rb") as f:
                data = pickle.load(f)
        except (FileNotFoundError, EOFError, pickle.UnpicklingError):
            print("Virhe ladattaessa tiedostoa. Luo uusi tyhjä mindmap.")
            data = {"nodes": [], "lines": []}

        nodes_history = data["nodes"]
        lines_history = data["lines"]

        # Luo Node-oliot nodes_history -listasta
        self.nodes = []
        for node_dict in nodes_history:
            node = Node(
                self.canvas, node_dict["x"], node_dict["y"], node_dict["text"])
            self.nodes.append(node)

        # Luo viivat lines_history -listasta (edellyttää, että solmut on luotu ensin)
        self.lines = []
        for line_dict in lines_history:
            start_node = self.nodes[line_dict["start_node_index"]]
            end_node = self.nodes[line_dict["end_node_index"]]
            line = self.canvas.create_line(
                start_node.x, start_node.y, end_node.x, end_node.y)
            self.lines.append(line)
