from tkinter import Frame, Tk, BOTH, Text, Menu, END
from tkinter import filedialog

def get_static_data(files_name):
    data_gens = []
    for string in open(files_name, 'r'):
        to = string.find('\n')
        cut = string[0:to]
        one_data = cut.split('\t')
        data_gens.append(one_data)
    return data_gens

static_data = get_static_data('data24.txt')
panel = get_static_data('panel5.txt')
class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Окно для выбора файла")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Открыть", command=self.onOpen)
        menubar.add_cascade(label="Файл", menu=fileMenu)

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)

    def onOpen(self):
        ftypes = [('txt файлы', '*.txt'), ('Все файлы', '*')]
        dlg = filedialog.Open(self, filetypes = ftypes)
        fl = dlg.show()

        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END, text)

    def readFile(self, filename):
        with open(filename, "r") as new_file:
            source_gen_line = []
            for string in new_file:
                if string != '\n':
                    source_gen_line.append(string)
            new_list_gen = []
            new_file = open('new_file_gen.txt', 'w')
            for static_gen in static_data:
                for source_gen in source_gen_line:                     
                    if source_gen.find(static_gen[1] + ',') != -1:
                        to = source_gen.find('\n')
                        source_gen = source_gen[0:to]
                        list_one_gen = source_gen.split(',')
                        if list_one_gen[3] == static_gen[2]*2:
                            sign = '+/+'
                        elif list_one_gen[3].find(static_gen[2]) != -1:
                            sign = '+/-'
                        elif list_one_gen[3] == '--':
                            sign = '--'
                        else:
                            sign = '-/-'
                        intermediate_list = [static_gen[0], static_gen[1], static_gen[2], list_one_gen[3], sign]
                        new_list_gen.append(intermediate_list)
            
            for gen_str in new_list_gen:
                new_file = open('new_file_gen.txt', 'a')
                for panel_one in panel:                    
                    if gen_str[1] == panel_one[1]:
                        new_file.write('\t' + panel_one[0] + '\n')
                        print('\t' + panel_one[0] + '\n')
                new_file.write(gen_str[0] + '\t' + gen_str[1] + '\t' + gen_str[2] + '\t' + gen_str[3] + '\t' + gen_str[4] + '\n') 
                print(gen_str[0] + '\t' + gen_str[1] + '\t' + gen_str[2] + '\t' + gen_str[3] + '\t' + gen_str[4] + '\n') 
                new_file.close()
            
        return 'the end'

def main():
    root = Tk()
    ex = Example()
    root.geometry("300x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
