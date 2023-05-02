"""
Tämä moduuli on graafinen käyttöliittymä (GUI) muistilappujen hallintaan, joka on toteutettu
Pythonin `tkinter`-kirjastolla. Se luo ja hallinnoi muistilappuja, jotka sisältävät etu- ja
takapuolen tekstin. Käyttäjä voi selata kortteja, lisätä uusia kortteja, näyttää korttien
vastauksia ja pitää kirjaa siitä, kuinka monta kertaa he ovat nähneet kortin tai muistaneet
sen sisällön.

Luokat:

1. DeckView: Näkymä yksittäiselle korttipakalle, joka sisältää kortit ja toiminnot niiden
   hallintaan.
2. Deck: Yksittäinen korttipakka, joka sisältää Card-olioita.
3. Card: Muistilappu, jolla on etu- ja takapuolen teksti.
4. Node: Graafinen solmu MindMapissa, joka sisältää Deck-olion ja liittyy muihin solmuihin
   viivoilla.
5. MindMap: Graafinen esitys solmuista ja niiden välisistä yhteyksistä, joka mahdollistaa
   solmujen luomisen, muokkaamisen ja yhdistämisen.
"""
import tkinter as tk
from tkinter import simpledialog
import atexit


class DeckView(tk.Toplevel):
    """
    Luokka luo ja hallinnoi muistilappujen pakkaa käyttäen tkinter-kirjastoa.
    """

    def __init__(self, master, deck):
        """
        Alustaa DeckView-olion ja asettaa sen perustiedot.
        """
        super().__init__(master)
        self.title("Pakka: " + deck.name)
        self.deck = deck
        self.card_index = 0
        self.showing_answer = False
        self.current_card_index = 0  # lisätty
        self.pass_count = 0
        self.dont_remember_count = 0
        self.almost_count = 0
        self.remember_count = 0
        self.geometry("600x400")
        self.build_widgets()

    def build_widgets(self):
        """
        Rakentaa ja järjestää pakkaa hallinnoivat käyttöliittymäkomponentit.
        """
        self.clear_widgets()
        self.add_button = tk.Button(
            self, text="Lisää", command=self.add_card_view)
        self.add_button.grid(row=0, column=0, sticky='nw')
        self.card_label = tk.Label(self)
        self.card_label.grid(row=2, column=0, columnspan=2, sticky='nsew')
        self.show_answer_button = tk.Button(
            self, text="Näytä vastaus", bg="blue", fg="blue", command=self.show_answer)
        self.show_answer_button.grid(
            row=3, column=0, columnspan=2, sticky='nsew')
        self.card_label = tk.Label(
            self, wraplength=500, height=10, font=("Arial", 22))
        self.card_label.grid(row=2, column=0, columnspan=2, sticky='nsew')
        self.grid_rowconfigure(1, weight=1, pad=5)
        self.grid_columnconfigure(1, weight=1, pad=5)
        if len(self.deck.cards) > 0:
            self.card_label.config(
                text=self.deck.cards[self.card_index].back_text)
        else:
            self.card_label.config(text="Ei kortteja")
        self.update_deck_view()

    def add_card_view(self):
        """
        Näyttää näkymän, jossa käyttäjä voi lisätä uuden kortin.
        """
        self.clear_widgets()
        self.back_button = tk.Button(
            self, text="Takaisin", command=self.build_widgets)
        self.back_button.grid(row=0, column=0, sticky='nw')
        self.deck_label = tk.Label(self, text="Pakka:" + self.deck.name)
        self.deck_label.grid(row=0, column=1, sticky='nw')
        self.front_label = tk.Label(self, text="Etupuoli:")
        self.front_label.grid(row=1, column=0, sticky='w')
        self.front_entry = tk.Text(self, bg="white", fg="black", insertbackground="black",
                                   height=2, bd=0, highlightthickness=1, highlightbackground="black")  # muutos
        self.front_entry.grid(row=1, column=1, sticky='ew')
        self.back_label = tk.Label(self, text="Takapuoli:")
        self.back_label.grid(row=2, column=0, sticky='w')
        self.back_entry = tk.Text(self, bg="white", fg="black", insertbackground="black",
                                  height=2, bd=0, highlightthickness=1, highlightbackground="black")  # muutos
        self.back_entry.grid(row=2, column=1, sticky='ew')
        self.save_button = tk.Button(
            self, text="Tallenna", command=self.save_card)
        self.save_button.grid(row=3, column=0, columnspan=2, sticky='ew')
        self.update()

    def clear_widgets(self):
        """
        Poistaa kaikki nykyiset komponentit näkymästä.
        """
        for widget in self.winfo_children():
            widget.destroy()

    def update_deck_view(self):
        """
        Päivittää näkymän näyttämään seuraavan kortin.
        """
        if len(self.deck.cards) == 0:
            return
        elif len(self.deck.cards) > 0:
            if self.current_card_index < len(self.deck.cards):
                self.card_label.config(
                    text=self.deck.cards[self.current_card_index].front_text)
        self.update()

    def save_card(self):
        """
        Tallentaa käyttäjän syöttämän kortin.
        """
        front_text = self.front_entry.get(1.0, tk.END).strip()
        print(front_text)
        back_text = self.back_entry.get(1.0, tk.END).strip()
        print(back_text)
        if front_text and back_text:
            card = Card(front_text, back_text)
            self.deck.add_card(card)
            print("kortti lisätty")
            # Tulosta kaikki kortit listasta
            print(self.deck.cards)
            for i, card in enumerate(self.deck.cards):
                print(f"Kortti {i + 1}:")
                print(f"  Etupuoli: {card.front_text}")
                print(f"  Takapuoli: {card.back_text}")
            self.front_entry.delete(1.0, tk.END)
            self.back_entry.delete(1.0, tk.END)
            print("valmiina ottammaan vastaan uuden kortin.")
            self.add_card_view()
            self.update()
        else:
            print("ei voi tallentaa vajaata korttia")

    def show_answer(self):
        """
        Näyttää tai piilottaa nykyisen kortin vastauksen.
        """
        if not self.deck.cards:
            return
        if not self.showing_answer:
            self.card_label.config(
                text=self.deck.cards[self.card_index].back_text)
            self.show_answer_button.config(text="Piilota vastaus")
            self.showing_answer = True
            self.pass_button = tk.Button(
                self, text="Ohi", command=lambda: self.next_card("pass"))
            self.pass_button.grid(row=3, column=0, sticky='ew')
            self.dont_remember_button = tk.Button(
                self, text="En muista", command=lambda: self.next_card("dont_remember"))
            self.dont_remember_button.grid(row=3, column=1, sticky='ew')
            self.almost_button = tk.Button(
                self, text="Melkein", command=lambda: self.next_card("almost"))
            self.almost_button.grid(row=4, column=0, sticky='ew')
            self.remember_button = tk.Button(
                self, text="Muistin", command=lambda: self.next_card("remember"))
            self.remember_button.grid(row=4, column=1, sticky='ew')
        else:
            self.next_card("pass")

    def next_card(self, answer_quality):
        """
        Siirtyy seuraavaan korttiin ja tallentaa käyttäjän arvioinnin.
        """
        if answer_quality == "pass":
            self.pass_count += 1
        elif answer_quality == "dont_remember":
            self.dont_remember_count += 1
        elif answer_quality == "almost":
            self.almost_count += 1
        elif answer_quality == "remember":
            self.remember_count += 1
        self.card_index = (self.card_index + 1) % len(self.deck.cards)
        self.update_deck_view()
        self.card_label.config(
            text=self.deck.cards[self.card_index].front_text)  # Muuta tämä rivi
        self.show_answer_button.config(text="Näytä vastaus")
        self.showing_answer = False
        self.pass_button.destroy()
        self.dont_remember_button.destroy()
        self.almost_button.destroy()
        self.remember_button.destroy()

    def show_counts(self):
        """
        Tulostaa laskurien arvot konsoliin (pass, dont_remember, almost, remember).Tämä lisätään ohjelmaan release 2 yhteydessä
        """
        print(f"Ohi: {self.pass_count}")
        print(f"En muista: {self.dont_remember_count}")
        print(f"Melkein: {self.almost_count}")
        print(f"Muistin: {self.remember_count}")


class Deck:
    """
    Deck on pakka, joka sisältää korteista koostuvan listan.
    """

    def __init__(self, name):
        """
        Alustaa pakan nimen ja tyhjän korttilistan.
        """
        self.name = name
        self.cards = []

    def add_card(self, card):
        """
        Lisää kortin pakan korttilistaan.
        """
        self.cards.append(card)
        print(
            f"Nyt ollaan Deck luokassa ja painettiin add card to deck ja tässä self.cards lista{self.cards}")

    def remove_card(self, card):
        """
        Poistaa kortin pakan korttilistasta.
        """
        self.cards.remove(card)

    def show_deck(self, master):
        """
        Näyttää pakan sisällön DeckView-luokan avulla.
        """
        DeckView(master, self)


class Card:
    """
    Card on kortti, jolla on etu- ja takapuoli.
    """

    def __init__(self, front_text, back_text):
        """
        Alustaa kortin etu- ja takapuolen tekstit.
        """
        self.front_text = front_text
        self.back_text = back_text


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
        self.deck = Deck(text)  # Lisää tämä rivi

    def show_deck(self):
        """
        Näyttää solmun pakan sisällön.
        """
        self.deck.show_deck(self.canvas.master)

    def add_card_to_deck(self, card_text):
        """
        Lisää kortin solmun pakan korttilistaan.
        """
        card = Card(card_text)
        self.deck.add_card(card)


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
        self.user = None
        self.folder = None

    def create_node(self, event):
        """
        Luo uuden solmun ja lisää sen miellekarttaan.
        """
        x, y = event.x, event.y
        text = simpledialog.askstring('Node Text', 'Enter node text:')
        if text:
            node = Node(self.canvas, x, y, text)
            self.nodes.append(node)

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

    def get_path(self, user, folder):
        self.user = user
        self.folder = folder
