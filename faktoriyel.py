# %%
n =int(input("n değerini giriniz(pozitif bir tam sayı)"))
if n<0:
    print("negatif sayılar için faktöriyel hesaplanmaz")
else:
    faktöriyel=1
    for i in range(1,n+1):
        faktöriyel *= i
        print(f"{n}! = {faktöriyel}")

