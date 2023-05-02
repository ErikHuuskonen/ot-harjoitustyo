"""
Tämä moduuli vastaa folderselectionscreen 
moduulin toiminnoista,jotka eivät liity tkinter toimintoihin
"""
import os

class FolderManagement():
    """
    Luokka metodeille joilla johdetaan folderselectionscreen toimintoja
    """
    def create_empty_pickle_file(self, file_name, folder_path):
        """
        Luo tyhjän .pickle-tiedoston annetulla nimellä ja tallentaa sen haluttuun kansioon.
        """
        os.makedirs(folder_path, exist_ok=True)
        full_file_path = os.path.join(folder_path, file_name)
        with open(full_file_path, "wb") as f:
            print(f)
    def save_files(self):
        """
        metodi vastaa siitä että luodut tiedostot tallentuvat varmasti
        """
        print("kutsuit save files metodia")
