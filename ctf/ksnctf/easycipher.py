import string

cipher = "EBG KVVV vf n fvzcyr yrggre fhofgvghgvba pvcure gung ercynprf n yrggre jvgu gur yrggre KVVV yrggref nsgre vg va gur nycunorg. EBG KVVV vf na rknzcyr bs gur Pnrfne pvcure, qrirybcrq va napvrag Ebzr. Synt vf SYNTFjmtkOWFNZdjkkNH. Vafreg na haqrefpber vzzrqvngryl nsgre SYNT."

testcipher = "fvzcyr"
result = []

for i in range(0,26):
	result = []
	for x in testcipher:
		new = ord(x) + i
                if new > 122:
                    new = new - 26
		result.append(chr(new))
        print i, ":", "".join(result)


result = []
for r in range(len(cipher)):
    check = ord(cipher[r])
    if (check <= 90 and check >= 65): 
        newchar = check + 13
        if newchar > 90:
            newchar -= 26
    elif (check <= 122 and check >= 97):
        newchar = check + 13
        if newchar > 122:
            newchar -= 26
    else:
        newchar = check
    result.append(chr(newchar))


print "Decoded: " + "".join(result)


