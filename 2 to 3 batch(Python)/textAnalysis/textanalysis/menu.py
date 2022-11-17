from . import TextAnalysis

class TextAnalysisMenu:
    """Text analysis menu class."""

    def start(self):
        ta = TextAnalysis.TextAnalysis()

        while True:
            print("Text Analysis")
            print()
            print("1. Predefined text")
            print("2. Keyboard input")
            print("3. File input")
            print("4. Exit")
            print()
            opt = int(input("Enter your choice: (1-4) : "))

            if opt == 1:
                ta.setAutomaticText()
            elif opt == 2:
                ta.setKeyboardInput()
            elif opt == 3:
                ta.setFileText()
            elif opt == 4:
                break
            else:
                print("Invalid input. Try again.\n\n")
                continue

            ta.displayText()
            ta.analyseText()
            ta.showResult()

        # Destroy the Object
        del ta