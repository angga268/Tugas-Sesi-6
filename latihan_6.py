#Program menentukan Nilai 

print ("=======PROGRAM NILAI=======")

nilai = int(input('Masukan NIlai  : '))

if nilai >= 90:
    grade = 'A'
    Predikat = 'Anjazz Kelazz'
elif nilai >= 80:
    grade = 'B'
    Predikat = 'Mantavv'
elif nilai >= 70:
    grade = 'C'
    Predikat = 'NT Deck'
elif nilai >= 60:
    grade = 'D'
    Predikat = 'Cemazz ko dek'
else :
    grade = 'E'
    Predikat = 'Turuu dek'

print ('Grade       : %s' %grade)
print ('Predikat    : %s' %Predikat)

