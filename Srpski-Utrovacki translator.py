#Srpski -> Utrovacki translator
#Utrovacki je slican kao satrovacki 
#Sem sto klasicne zamene dva ili tri zadnja slova 
#Imamo ubacivanje slova 'u' na pocetak,'za' izmedju i 'nje' na kraj 
pitanje = 'da'
while pitanje == 'da':
    recenica = raw_input('Unesite recenicu: ')
    original = recenica
    if len(original) > 4:
        z3 = original[-3:]
        ostalo = original[:-3]
        print 'u' + z3 + 'za' + ostalo + 'nje'
    else:
        z2 = original[-2:]
        ostalo = original[:-2]
        print 'u' + z2 + 'za' + ostalo + 'nje',
    print
    pitanje = raw_input('Da li zelite da unesete novu rec?')

       

