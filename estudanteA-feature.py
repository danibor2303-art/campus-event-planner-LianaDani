def adicionarEvento(listaEventos, nome, data, local, categoria):
    meuEvento = {
        "nome": nome,
        "data": data,
        "local": local,
        "categoria": categoria
    }

    listaEventos.append(meuEvento)