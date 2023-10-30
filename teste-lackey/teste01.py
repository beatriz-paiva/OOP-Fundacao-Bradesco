import lackey as lk


lk.rightClick(lk.Pattern("testeSAJ.png").targetOffset(-9, 16))
lk.sleep(1)
lk.type('Copiar para outra fila')
lk.sleep(2)
lk.click(lk.Pattern("testeSAJ.png").targetOffset(-5, 60))