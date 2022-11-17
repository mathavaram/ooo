from textanalysis import TextAnalysis

ta = TextAnalysis.TextAnalysis()
# ta.setAutomaticText()
# ta.setKeyboardInput()
ta.setFileText()
ta.displayText()
ta.analyseText()
ta.showResult()