def array(kalimat):
    huruf_besar = 'ABCDEFGHIJKLMMNOPQRSTUVWXYZ'
    huruf_kecil = 'abcdefghijklmnopqrstuvwxyz'
    angka = '0123456789'
    jumlahHurufBesar = ''
    jumahHurufKecil = ''
    jumlahAngka = ''
    for karakter in kalimat:
        if karakter in huruf_besar:
            jumlahHurufBesar += karakter
        if karakter in huruf_kecil:
            jumahHurufKecil += karakter
        if karakter in angka:
            jumlahAngka += karakter
    
    print('Jumlah huruf besar adalah '+str(len(jumlahHurufBesar)))
    print('Jumlah huruf Kecil adalah '+str(len(jumahHurufKecil)))
    print('Jumlah angka adalah '+str(len(jumlahAngka)))

kalimat = input('Ketikkan kalimat: ')
array(kalimat)

def jumlahKata():
    listNya = kalimat.split()
    print('Jumlah katanya adalah '+str(len(listNya)))
jumlahKata()