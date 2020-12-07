class Notebook():
    def __init__(self, cpu_name, display_inch):
        self.cpu = cpu_name
        self.dispalysize = display_inch

MacbookPro = Notebook('M1',13)

print(MacbookPro.cpu)
print(MacbookPro.dispalysize)