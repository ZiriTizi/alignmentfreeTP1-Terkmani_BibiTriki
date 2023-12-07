from os import listdir, path
import time

start = time.time()

def load_fna(filename):
    """ Loads a fasta formated file into a list of sequences.
    :param str filename: The file to load
    :return Array: An array of strings where each string is a sequence from the fasta
    """
    texts = []
    txt = []

    with open(filename) as fp:
        for line in fp:
            if line[0] == '>':
                if len(txt) > 0:
                    texts.append("".join(txt))
                txt = []
            else:
                txt.append(line.strip())          
    if len(txt) > 0:
        texts.append("".join(txt))
    cleaned_texts = [''.join([char for char in seq if char in 'ACGT']) for seq in texts]    
    return cleaned_texts

def load_directory(directory):
    """ Loads all the fasta files from a directory
    :param str directory: Path to the directory to load.
    :return dict: A dict containing pairs filename: sequence array.
    """
    files = {}
    for filename in listdir(directory):
        if filename[filename.rfind('.')+1:] in ["fa", "fasta", "fna"]:
            files[filename] = load_fna(path.join(directory, filename))
    
    return files


if __name__ == "__main__":
    files = load_directory("ata")
    print(len(files))


print(time.time() - start)
