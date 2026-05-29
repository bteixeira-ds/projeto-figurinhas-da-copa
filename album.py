class Album:
    def __init__ (self):
        self.figurinhas = []
        
    def adicionar_figurinha(self, pais, numero):
        figurinha = {
            "pais": pais,
            "numero": numero
        }
        self.figurinhas.append(figurinha)
        
    def adicionar_varias_figurinhas(self, pais, numeros):
        for numero in numeros:
            self.adicionar_figurinha(pais, numero)
        
    def mostrar_figurinhas(self):
        print("\n")
        print("=" * 40)
        print("ÁLBUM DE FIGURINHAS DA COPA")
        print("=" * 40)
        print("\n")
        
        paises = {}
        
        for figurinha in self.figurinhas:
            pais = figurinha["pais"]
            numero = figurinha["numero"]
            
            if pais not in paises:
                paises[pais] = []
                
            if numero not in paises[pais]:
                paises[pais].append(numero)
            
        for pais, numeros in paises.items():
            numeros_texto = ", ".join(map(str, numeros))
            if len(numeros) == 1:
                print(f"{pais} - Figurinha {numeros_texto}")
            else:
                print(f"{pais} = Figurinhas {numeros_texto}")
            
        print("\n")
        print("=" * 40)
            
    def total_figurinhas(self):
        print(f"Você tem {len(self.figurinhas)} figurinhas")
        
    def mostrar_repetidas(self):
        contador = {}
        
        for figurinha in self.figurinhas:
            chave = f'{figurinha["pais"]} - {figurinha["numero"]}'
            if chave in contador:
                contador[chave] += 1
            else:
                contador[chave] = 1
        for chave, quantidade in contador.items():
            if quantidade > 1:
                print(f"{chave} está repetida {quantidade} vezes")
                
    def figurinhas_faltando(self):
        total_album = 994
        faltam = total_album - len(self.figurinhas)
        print(f"faltam {faltam} figurinhas para completar o álbum")
