# Cria questões sobre as capitais brasileiras de forma aleatória
# para a prova de geografia.
import random

# Dados da prova. As chaves são os estados e os valores as suas capitais
capitais = {
    'Acre': 'Rio Branco',
    'Alagoas': 'Maceió',
    'Amapá': 'Macapá',
    'Amazonas': 'Manaus',
    'Bahia': 'Salvador',
    'Ceará': 'Fortaleza',
    'Espírito Santo': 'Vitória',
    'Goiás': 'Goiânia',
    'Maranhão': 'São Luís',
    'Mato Grosso': 'Cuiabá',
    'Mato Grosso do Sul': 'Campo Grande',
    'Minas Gerais': 'Belo Horizonte',
    'Pará': 'Belém',
    'Paraíba': 'João Pessoa',
    'Paraná': 'Curitiba',
    'Pernambuco': 'Recife',
    'Piauí': 'Teresina',
    'Rio de Janeiro': 'Rio de Janeiro',
    'Rio Grande do Norte': 'Natal',
    'Rio Grande do Sul': 'Porto Alegre',
    'Rondônia': 'Porto Velho',
    'Roraima': 'Boa Vista',
    'Santa Catarina': 'Florianópolis',
    'São Paulo': 'São Paulo',
    'Sergipe': 'Aracaju',
    'Tocantins': 'Palmas',
    'Distrito Federal': 'Brasília'
}

# Gerar 30 provas
for prova_num in range(30):
    # TODO: Criar os arquivos da prova e respostas
    arquivo_prova = open(f'prova-geografia-{prova_num + 1}.txt', 'w', encoding='utf-8')
    arquivo_respostas = open(f'prova-geografia-respostas-{prova_num + 1}.txt', 'w')
    
    # TODO: Escrever o cabeçalho da prova.
    arquivo_prova.write('Nome:\n\nData:\n\nPeríodo:\n\n')
    arquivo_prova.write((' ' * 20) + f'Prova Capitais Brasileiras (Questionário {prova_num + 1})')
    arquivo_prova.write('\n\n')
        
    # TODO: Misturar a ordem dos estados.
    estados = list(capitais.keys())
    random.shuffle(estados)
    
    # TODO: Percorrer todos os 26 estados, fazendo uma questão para cada um
    for questao_num in range(26):
        resposta_correta = capitais[estados[questao_num]]
        respostas_erradas = list(capitais.values())
        del respostas_erradas[respostas_erradas.index(resposta_correta)]
        respostas_erradas = random.sample(respostas_erradas, 3)
        respostas = respostas_erradas + [resposta_correta]
        random.shuffle(respostas)
        
        # TODO: Escrever a questão e as opções no arquivo
        arquivo_prova.write(f'{questao_num + 1}. Qual é a capital de {estados[questao_num]}?\n')
        for i in range(4):
            arquivo_prova.write(f"    {'ABCD'[i]}. {respostas[i]}\n")
        arquivo_prova.write("\n")
        
        # TODO: Escrever a resposta no arquivo de respostas
        arquivo_respostas.write(f"{questao_num + 1}. {'ABCD'[respostas.index(resposta_correta)]}\n")
    
    arquivo_prova.close()
    arquivo_respostas.close()