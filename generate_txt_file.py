import argparse
import os
from colorama import Fore

parser = argparse.ArgumentParser()
parser.add_argument('--file_txt_name', type=str, default="C:/Users/giuli/OneDrive/Desktop/documenti_generati.txt", help='percorso del file txt di testo contenente la lista di documenti')
parser.add_argument('--cartella_documenti', type=str, default="C:/Users/giuli/OneDrive/Desktop/documenti", help='percorso della cartella con i documenti che vuoi controllare')
args = parser.parse_args()


def generate_txt(txt_file_path, documents_directory_path):
    files = os.listdir(documents_directory_path)
    file_txt = open(txt_file_path, 'w')
    if os.path.isfile(txt_file_path):
        answer = input(Fore.YELLOW + "Il file esiste già. Vuoi sovrascriverlo? (S, N)" + Fore.RESET)
    if answer == 'S':
        for file_idx, file in enumerate(files):
            if os.path.isfile(documents_directory_path+"/"+file):
                files[file_idx] = os.path.splitext(file)[0]
            files[file_idx] = files[file_idx].replace(".", ")", 1)
            file_txt.write(files[file_idx]+"\n")
        file_txt.close()
        print(Fore.GREEN + f"File di testo generato correttamente! Lo trovi in {txt_file_path}" + Fore.RESET)


if __name__ == '__main__':
    generate_txt(args.file_txt_name, args.cartella_documenti)