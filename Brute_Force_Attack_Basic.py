# "Brute Force Attack" (Kaba Kuvvet Saldırısı), bir güvenlik sistemine giriş yapabilmek için tüm olası kombinasyonları denemeyi içeren bir saldırı türüdür. Bu tür bir saldırı, genellikle şifrelerin veya anahtarların güvenliğini kırmak için kullanılır. Temel anlamda, bu saldırı yönteminin amacı, sistemin veya verinin korunan kısmına erişmek için tüm olası kombinasyonları sistematik bir şekilde denemektir.


sifre = "748202"

flag = False

rakamlar = "0123456789"

for basamak1 in rakamlar:
    for basamak2 in rakamlar:
        for basamak3 in rakamlar:
            for basamak4 in rakamlar:
                for basamak5 in rakamlar:
                    for basamak6 in rakamlar:
                        deneme = (basamak1+basamak2+basamak3+basamak4+basamak5+basamak6)
                        print(deneme)
                        if deneme == sifre:
                            print("Parolanız: " + deneme)
                            flag = True
                            break
                    if flag == True:
                        break
                if flag == True:
                    break
            if flag == True:
                break
        if flag == True:
            break
    if flag == True:
        break
