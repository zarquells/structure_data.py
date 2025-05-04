class Pilha:
# definindo os atributos dos objetos desta classe
    def __init__(self, capacidade, valores = []):
        self.capacidade = capacidade
        self.valores = valores
        self.topo    = -1
    
# definindo retorno padrão dos objetos desta classe
    def __str__(self):
        return f'Pilha Atual: {self.valores}'

# criando os métodos aplicáveis a esta classe

    # métodos internos
    def pilha_cheia(self):
        if self.topo == self.capacidade -1:
            return True
        else: 
            return False
    
    def pilha_vazia(self):
        if self.topo == -1:
            return True
        else:
            return False
    
    # métodos externos
    def empilhar(self, valor):
        if self.pilha_cheia():
            return False, 'Não foi possível realizar esta operação. A pilha se encontra cheia.'
        else:
            self.valores.append(valor)
            self.topo += 1
            return True, f'Operação realizada com sucesso. Pilha atualizada: {self.valores}'
        
    def desempilhar(self):
        if self.pilha_vazia():
            return False, 'Não foi possível realizar esta operação. A pilha se encontra vazia.'
        else:
            self.valores.pop()
            self.topo -= 1
            return True, f'Operação realizada com sucesso. Pilha atualizada: {self.valores}'

# exemplos de uso de objeto da classe Pilha
pilha1 = Pilha(3, [1, 2])
pilha1.empilhar(1)
pilha1.empilhar(2)
pilha1.empilhar(3)
print(pilha1)
print(pilha1.empilhar(4))
pilha1.desempilhar()
pilha1.desempilhar()
pilha1.desempilhar()
print(pilha1)
print(pilha1.desempilhar())