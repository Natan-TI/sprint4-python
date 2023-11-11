onibus = {
    'número' : ['477A', '5142', '476G', '364A', '4115', '407M', '5705', '874T', '975A'],
    'nome' : ['Term. PINHEIROS',
              'Term. PQ DOM PEDRO II',
              'IBIRAPUERA',
              'Hospital Ipiranga',
              'PRAÇA DA REPÚBLICA',
              'METRÔ VILA MARIANA',
              'METRÔ VERGUEIRO',
              'LAPA',
              'VILA BRASILÂNDIA'],
    'lotação' : [3.0, 2.5, 4.0, 4.5, 1.0, 3.5, 5.0, 1.5, 2.0],
    'tempo de chegada' : ['10min', '13min', '7min', '23min', '16min', '5min', '15min', '3min', '19min']
}

destinos = ['Vila Mariana', 'Av. Paulista', 'Av. Lins de Vasconcelos']

usuario = {
    'email' : "",
    'senha' : "",
    'nome' : "",
    'endereço' : {
        'rua' : "",
        'numero' : "",
        'bairro' : "",
        'cep' : ""
    },
}

opcoes = ('1', '2', '3', '4', '5')

opcoes_fav = [str(i) for i in range(len(onibus['nome']))]