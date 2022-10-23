import random
oyun = ['Taş','Kağıt','Makas']
tas=oyun[0]
kagıt=oyun[1]
makas=oyun[2]

print('Taş-Kagıt-Makas Oyununa Hosgeldiniz!\nİstediğiniz zaman Çıkış yazarak oyunu bitirebilirsiniz.')

while True:
    secim= input('Lütfen seçiminizi büyük harfle başlayacak şekilde yazınız.\nTaş mı? Kağıt mı? Makas mı?')
    comsecim= random.choice(oyun)
    if secim == tas:
        if comsecim==tas:
            print('Bilgisayar taşı secti. \nBerabere kaldınız.')
        elif comsecim==kagıt:
            print('Bilgisayar kagıtı secti. \nBilgisayar kazandı.')
        else:
            print('Bilgisayar makası secti. \nTebrikler siz kazandınız!')
    if secim == kagıt:
        if comsecim==tas:
            print('Bilgisayar taşı secti. \nTebrikler siz kazandınız!')
        elif comsecim==kagıt:
            print('Bilgisayar kagıtı secti. \nBerabere kaldınız.')
        else:
            print('Bilgisayar makası secti. \nBilgisayar kazandı.')
    if secim == makas:
        if comsecim==tas:
            print('Bilgisayar taşı secti. \nBilgisayar kazandı.')
        elif comsecim==kagıt:
            print('Bilgisayar kagıtı secti. \nTebrikler siz kazandınız!')
        else:
            print('Bilgisayar makası secti. \nBerabere kaldınız.')
    if secim!=tas and secim!=kagıt and secim!=makas and secim!='Çıkış':
        print('Lütfen girdiğinizi kontrol ediniz. Hatalı yazdınız.')
    if secim=='Çıkış':
        print('Program Kapatılıyor...')
        break