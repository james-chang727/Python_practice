MARGIN = 10

def pyramidLine(symbol, lineNumber, height):
    line = ""
    line += spacesForPyramidLine(lineNumber, height)
    line += symbolsForPyramidLine(symbol, lineNumber)
    line += "\n"
    return line


def symbolsForPyramidLine(symbol, lineNum):
    lineSymbols = ""
    for symbolsCount in range((lineNum * 2) - 1):
        lineSymbols += symbol
    return lineSymbols


def spacesForPyramidLine(lineNum, height):
    lineSpaces = ""
    for spacesCount in range(MARGIN + height + 1 - lineNum):
        lineSpaces += " "
    return lineSpaces


def pyramidString(character, height):
    pattern = "\n"
    for lineCount in range(height):
        pattern += pyramidLine(character, lineCount, height)
    return pattern


def main():
    height = int(input("\n\tEnter the number of lines for the pyramid: "))
    brickCharacter = input("\tEnter the character from which the pyramid should be made: ")
    print(brickCharacter)
    print(pyramidString(brickCharacter, height))


if __name__ == "__main__":
    main()
