# Local Eats - Business Logic

def calcular_total_pedido(itens, frete=0, cupom=None):
    """
    Calcula o valor total de um pedido.
    itens: lista de dicionários com 'preco' e 'quantidade'
    frete: valor do frete (float)
    cupom: dicionário com 'tipo' ('fixo' ou 'percentual') e 'valor'
    """
    total = sum(item['preco'] * item['quantidade'] for item in itens)
    
    if cupom:
        if cupom['tipo'] == 'fixo':
            total -= cupom['valor']
        elif cupom['tipo'] == 'percentual':
            total -= total * (cupom['valor'] / 100)
            
    total += frete
    return max(0, total)
