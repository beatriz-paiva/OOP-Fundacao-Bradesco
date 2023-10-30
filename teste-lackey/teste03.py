import lackey as lk

imagens = {
    1: (lk.Pattern("discord.png"),
        lk.Pattern("discord.png")),
    2: (lk.Pattern("direct.png")),
    3: (lk.Pattern("encontrar-pessoa.png")),
    4: (lk.Pattern("barra-conversa.png"))
}

# lk.type("d", lk.Key.WIN)
lk.doubleClick(imagens[1])
lk.sleep(1)
lk.click(imagens[2])
lk.sleep(1)
lk.click(imagens[3])
lk.sleep(2)
lk.type("j.teles")
lk.sleep(1)
lk.type(lk.Key.ENTER)
lk.sleep(1)
lk.click(imagens[4])
img = lk.Pattern("barra-conversa.png")
lk.sleep(1)
if lk.exists(imagens[4]):
    lk.type("Teste usando lackey")
    lk.type(lk.Key.ENTER)
else:
    print("erro")