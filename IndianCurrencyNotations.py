
def indianCurrencyNotation(number:str) -> str:
    # Store Last Three Number
    LastThreeNumber = [number[-3:]]

    numList = []
    # Loop the string in reversed order skiping to 2 value
    for i in range(-3, -len(number), -2):
        numList.insert(0,number[i-2:i])

    # Joint the list wiht ',' and return the -> str
    return ','.join(numList + LastThreeNumber)

if __name__ == "__main__":
    # Test Case
    numberString = '504678'
    print(f'Input -> {numberString}')
    print(f'Output -> {indianCurrencyNotation(numberString)}')