import argparse
import os
from colorama import Fore

parser = argparse.ArgumentParser()
parser.add_argument('--file_txt', type=str, default="C:/Users/giuli/OneDrive/Desktop/documenti.txt", help='percorso del file txt di testo contenente la lista di documenti che vuoi controllare')
parser.add_argument('--cartella_documenti', type=str, default="C:/Users/giuli/OneDrive/Desktop/documenti", help='percorso della cartella con i documenti che vuoi controllare')
args = parser.parse_args()


def check_documents(txt_file_path, documents_directory_path):
    files = os.listdir(documents_directory_path)
    missing_files = False
    for file_idx, file in enumerate(files):
        if os.path.isfile(documents_directory_path+"/"+file):
            files[file_idx] = os.path.splitext(file)[0]
    with open(txt_file_path, 'r') as file_txt:
        lines = file_txt.readlines()
        for line in lines:
            line = line.replace(")", ".", 1)
            line = line.replace("\n", "")
            line = line.strip()
            if line not in files:
                missing_files = True
                print(Fore.RED + f"Non ho trovato nella cartella il file {line}" + Fore.RESET)
    if not missing_files:
        print(Fore.GREEN + "I file ci sono tutti!" + Fore.RESET)


if __name__ == '__main__':
    check_documents(args.file_txt, args.cartella_documenti)