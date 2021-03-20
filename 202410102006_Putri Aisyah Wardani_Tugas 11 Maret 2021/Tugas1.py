def array(kalimat):
    konsonan = 'BCDFGHJKLMNPQRSTVWXYZbcdefghjklmnpqrstvwxyz'
    vokal = 'AIUEOaiueo'
    space = ' '
    jumlah_vokal = ''
    jumlah_konsonan = ''
    jumlah_space = ''
    for huruf in kalimat:
        if huruf in vokal:
            jumlah_vokal += huruf
        if huruf in konsonan:
            jumlah_konsonan += huruf
        if huruf in space:
            jumlah_space += huruf
    print('Jumlah huruf vokal adalah ' +str(len(jumlah_vokal)))
    print('Jumlah huruf konsonan adalah '+str(len(jumlah_konsonan)))
    print('Jumlah karakter spasi adalah '+str(len(jumlah_space)))

kalimat = input('Ketikkan kalimat: ')
array(kalimat)