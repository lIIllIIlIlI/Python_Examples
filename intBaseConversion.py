
myOffset = 10

# Binary/decimal/hexal strings can be explicitely converted to decimal
myBinaryString = "1100"
myBinary = int(myBinaryString,2)
print("Binary converted to bin, myBinary in decimal: {}".format(myBinary))
decBinAdd = myBinary + myOffset
print("Offset added to binary: {}. New binary number: {}".format(decBinAdd, bin(decBinAdd)))

myHexString = "0x110"
myHex = int(myHexString,16)
myAlphaHexString = "0xaef"
myAlphaHex = int(myAlphaHexString,16)

mergedHex = myHex + myAlphaHex + myOffset
print("Offset added to hex: {}. New hex number:{}".format(mergedHex, hex(mergedHex)))

def getBitMask(offset, bitMaskWidth, dataTypeSize):
    """
    Generates and returns a hexadecimal bit mask that is aligned to the data type size via
    padding.

    @offset: desired shift of the bitmask
    @bitMaskWidth: number of bits for the bitmask
    """
    bitWidth = dataTypeSize * 8
    hexDigitNumber = int(bitWidth / 4)
    rawBitMask = ""
    if offset + bitMaskWidth > bitWidth:
        logger.warning("Overflow in BitMask converter. The sum of the Offset %s and \
the bit mask width %s exceeds the given width of %s bit", offset, bitMaskWidth, bitWidth)
    for bitPosition in range(bitWidth):
        if bitPosition >= offset and bitPosition < offset + bitMaskWidth:
            rawBitMask += "1"
        else:
            rawBitMask += "0"
    bitMask = hex(int(rawBitMask, 2))
    bitMask = insertHexPadding(bitMask, hexDigitNumber)
    return bitMask

def insertHexPadding(hexString, paddingWidth):
    """
    Pads the given hexadecimal string with zeros to reach the desired paddingWidth in lenght.
    """
    if(hexString[:2] != "0x"):
        logger.warning("Can't insert padding in non-hexadecimal string")
    else:
        hexString = hexString[:2] + hexString[2:].zfill(paddingWidth)
    return hexString

def convertToCleanDecimal(value):
    """
    Converts an extracted bin or hex value to a clean decimal value.
    Removes '(', ')', 'u' and 'U'. Values that are already clean and 
    decimal are returned untouched.
    
    Example: (0x3d)U --> 61
              0b01 --> 1
    """
    hexRegex = r'0x[0-9a-fA-F]'
    binPattern = r'0b[0-1]'
    if value:
        if re.search(hexRegex, value) or re.search(binPattern, value):
            value = re.sub(r'[u|U]', "", value)
            value = re.sub(r'[\(|\)]', "", value)
        if re.search(hexRegex, value):
            value = int(value, 16)
        elif re.search(binPattern, value):
            value = int(value, 2)
    return value
