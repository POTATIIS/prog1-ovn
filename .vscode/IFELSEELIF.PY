Vaken = input('Sover du? [Ja/Nej]').lower()
if Vaken == 'ja':
    print('vakna för i helvete')
    Duscha = input('Ska du duscha? [Ja/Nej]').lower()
elif Vaken == 'nej':
    print('bra, du är vaken')    
else:
    print('Detonera sängen')
if Duscha == 'Ja':
    print('Gå och duscha')
elif Duscha == 'Nej':
    print('Usch, gå och duscha äckel')
else:
    print('Är du hjärndöd?')
Buss = input('Tar du bussen till skolan? [Ja/Nej]').lower()
if Buss == 'Ja':
    print('Gå till bussen så att du kommer i tid')
elif Buss == 'Nej':
    print('Hur tänkte du ta dig till skolan?')
else:
    print('Hallå, vill du missa bussen?')    
NTI = input('Kom du i tid idag? [Ja/Nej]').lower()
if NTI == 'Ja':
    print('vad bra, ditt CSN är säkert')
elif NTI == 'Nej':
    print('Vill du ha CSN')
else:
    print('Hallå, har du åkt än?')
            