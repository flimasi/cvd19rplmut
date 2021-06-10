import os
import constant

class scapev:

    def __init__(self, rna):
        self.rna = rna

    def get_status(self):
        return self.__status

    def set_status(self, rna):
        self.__status = rna

    def main(self):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, self+'.txt')

def infect(name: str, mutation: str):
    print(name)
    f = open("infected/"+ name+".txt", "w")
    f.write(mutation)
    f.close()

def mutations(name: str, mutation: str):
    print(name)
    f = open("mutations/"+ mutation+".txt", "w")  # 'r' for reading and 'w' for writing
    f.write(mutation)

    # Write inside file
    f.close()


def vacineResult(codevac: str):
    print('apply vacine')
    file = "mutations/" + codevac + ".txt"
    exx = os.path.exists(file)
    if(exx):
        os.unlink(file)  # 'r' for reading and 'w' for writing
