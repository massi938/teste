carrinho = [["id",1,"Produto","Iphone",{"preço":499}],["id",2,"Produto","Kindle",{"preço":179}],
            ["id",3,"Produto","Macbook",{"preço":1199}]]

lista = ["id",3,"Produto","Macbook","preço",1199]

teste = list(map(lambda x: x=="preço",lista))

print(teste)