def Ascii_to_Binary(text,separate_by=None):
    """
    To convert any ascii string put vlue in text peramiter
    To converte every charecter by  separated binary vlue put separat_by 
    """
	
    result = ""
    for ch in text:
        bits = ''
        bits += format(ord(ch),'b')
        bitlen =len(bits)
        if bitlen < 8:
            diff= 8 - bitlen
            bits = (diff * '0') + bits
        result += bits
        if separate_by != None:
            result += separate_by
    return result


def Binary_to_Ascii(data,separate_by=None):
   
	
    result = ""
    if separate_by != None :
        for octed in data.split(separate_by):
            decimal=int(octed,2)
            char = chr(decimal)
            result = result + char
    else :
        BitData =[]
        while data:
            BitData.append(data[:8])
            data = data[8:]

        for octed in BitData:
            decimal=int(octed,2)
            char = chr(decimal)
            result = result + char
            
    return result
