
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
