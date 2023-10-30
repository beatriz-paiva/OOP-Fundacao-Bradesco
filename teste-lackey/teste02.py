import lackey as lk


lk.doubleClick(lk.Pattern("discord.png"))
lk.sleep(1)
lk.click(lk.Pattern("direct.png"))
lk.sleep(1)
lk.click(lk.Pattern("encontrar-pessoa.png"))
lk.sleep(2)
lk.type("j.teles")
lk.sleep(1)
lk.type(lk.Key.ENTER)
lk.sleep(1)
lk.click("barra-conversa.png")
lk.sleep(1)
lk.type("Teste usando lackey")
lk.type(lk.Key.ENTER)