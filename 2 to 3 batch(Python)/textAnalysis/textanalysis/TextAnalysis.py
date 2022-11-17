class TextAnalysis:
    """Analyses the text for the occurrences of the characters,
           and display the count along with histogram pattern."""
    def __init__(self):
        self.Text = ""
        self.Result = {}


    def setAutomaticText(self):
        self.Text = "HeLLO world"

    def setKeyboardInput(self):
        inText = ""
        print("Enter text below (null Enter to finish input) :")
        while True:
            tmpText = input()
            if len(tmpText) == 0:
                break
            inText += tmpText

        self.Text = inText

    def setFileText(self):
        filename = input("Enter the File Name : ")
        with open(filename, "r") as f:
            self.Text = f.read()


    def analyseText(self):
        # Clear Dictionary.
        self.Result.clear()

        # Make all characters lowercase.
        tmpText = self.Text.lower()

        # Take each character (only alphabetic) and count them.
        for c in tmpText:
            if c.isalpha():
                # Check in the dictionary.
                if self.Result.__contains__(c):
                    self.Result[c] += 1
                else:
                    self.Result[c] = 1

        print(self.Result)

    def showResult(self):
        # Take each key & Value from dictionary.
        # Show results.
        for k, v in self.Result.items():
            print("{} {:3d} {}".format(k, v, "*" * v))

    # Display text.
    def displayText(self):
        print(self.Text)