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
