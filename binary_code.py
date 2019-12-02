for i in range(256):
    b = bytes([i])
    print(b,int.from_bytes(b, byteorder='little', signed=True))

# to 
hash_255 = [i for i in range(128)]
hash_255.extend([i for i in range(128,0,-1)])
    
"""
b'\x00' 0
b'\x01' 1
b'\x02' 2
b'\x03' 3
b'\x04' 4
b'\x05' 5
b'\x06' 6
b'\x07' 7
b'\x08' 8
b'\t' 9
b'\n' 10
b'\x0b' 11
b'\x0c' 12
b'\r' 13
b'\x0e' 14
b'\x0f' 15
b'\x10' 16
b'\x11' 17
b'\x12' 18
b'\x13' 19
b'\x14' 20
b'\x15' 21
b'\x16' 22
b'\x17' 23
b'\x18' 24
b'\x19' 25
b'\x1a' 26
b'\x1b' 27
b'\x1c' 28
b'\x1d' 29
b'\x1e' 30
b'\x1f' 31
b' ' 32
b'!' 33
b'"' 34
b'#' 35
b'$' 36
b'%' 37
b'&' 38
b"'" 39
b'(' 40
b')' 41
b'*' 42
b'+' 43
b',' 44
b'-' 45
b'.' 46
b'/' 47
b'0' 48
b'1' 49
b'2' 50
b'3' 51
b'4' 52
b'5' 53
b'6' 54
b'7' 55
b'8' 56
b'9' 57
b':' 58
b';' 59
b'<' 60
b'=' 61
b'>' 62
b'?' 63
b'@' 64
b'A' 65
b'B' 66
b'C' 67
b'D' 68
b'E' 69
b'F' 70
b'G' 71
b'H' 72
b'I' 73
b'J' 74
b'K' 75
b'L' 76
b'M' 77
b'N' 78
b'O' 79
b'P' 80
b'Q' 81
b'R' 82
b'S' 83
b'T' 84
b'U' 85
b'V' 86
b'W' 87
b'X' 88
b'Y' 89
b'Z' 90
b'[' 91
b'\\' 92
b']' 93
b'^' 94
b'_' 95
b'`' 96
b'a' 97
b'b' 98
b'c' 99
b'd' 100
b'e' 101
b'f' 102
b'g' 103
b'h' 104
b'i' 105
b'j' 106
b'k' 107
b'l' 108
b'm' 109
b'n' 110
b'o' 111
b'p' 112
b'q' 113
b'r' 114
b's' 115
b't' 116
b'u' 117
b'v' 118
b'w' 119
b'x' 120
b'y' 121
b'z' 122
b'{' 123
b'|' 124
b'}' 125
b'~' 126
b'\x7f' 127
b'\x80' -128
b'\x81' -127
b'\x82' -126
b'\x83' -125
b'\x84' -124
b'\x85' -123
b'\x86' -122
b'\x87' -121
b'\x88' -120
b'\x89' -119
b'\x8a' -118
b'\x8b' -117
b'\x8c' -116
b'\x8d' -115
b'\x8e' -114
b'\x8f' -113
b'\x90' -112
b'\x91' -111
b'\x92' -110
b'\x93' -109
b'\x94' -108
b'\x95' -107
b'\x96' -106
b'\x97' -105
b'\x98' -104
b'\x99' -103
b'\x9a' -102
b'\x9b' -101
b'\x9c' -100
b'\x9d' -99
b'\x9e' -98
b'\x9f' -97
b'\xa0' -96
b'\xa1' -95
b'\xa2' -94
b'\xa3' -93
b'\xa4' -92
b'\xa5' -91
b'\xa6' -90
b'\xa7' -89
b'\xa8' -88
b'\xa9' -87
b'\xaa' -86
b'\xab' -85
b'\xac' -84
b'\xad' -83
b'\xae' -82
b'\xaf' -81
b'\xb0' -80
b'\xb1' -79
b'\xb2' -78
b'\xb3' -77
b'\xb4' -76
b'\xb5' -75
b'\xb6' -74
b'\xb7' -73
b'\xb8' -72
b'\xb9' -71
b'\xba' -70
b'\xbb' -69
b'\xbc' -68
b'\xbd' -67
b'\xbe' -66
b'\xbf' -65
b'\xc0' -64
b'\xc1' -63
b'\xc2' -62
b'\xc3' -61
b'\xc4' -60
b'\xc5' -59
b'\xc6' -58
b'\xc7' -57
b'\xc8' -56
b'\xc9' -55
b'\xca' -54
b'\xcb' -53
b'\xcc' -52
b'\xcd' -51
b'\xce' -50
b'\xcf' -49
b'\xd0' -48
b'\xd1' -47
b'\xd2' -46
b'\xd3' -45
b'\xd4' -44
b'\xd5' -43
b'\xd6' -42
b'\xd7' -41
b'\xd8' -40
b'\xd9' -39
b'\xda' -38
b'\xdb' -37
b'\xdc' -36
b'\xdd' -35
b'\xde' -34
b'\xdf' -33
b'\xe0' -32
b'\xe1' -31
b'\xe2' -30
b'\xe3' -29
b'\xe4' -28
b'\xe5' -27
b'\xe6' -26
b'\xe7' -25
b'\xe8' -24
b'\xe9' -23
b'\xea' -22
b'\xeb' -21
b'\xec' -20
b'\xed' -19
b'\xee' -18
b'\xef' -17
b'\xf0' -16
b'\xf1' -15
b'\xf2' -14
b'\xf3' -13
b'\xf4' -12
b'\xf5' -11
b'\xf6' -10
b'\xf7' -9
b'\xf8' -8
b'\xf9' -7
b'\xfa' -6
b'\xfb' -5
b'\xfc' -4
b'\xfd' -3
b'\xfe' -2
b'\xff' -1
"""
