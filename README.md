# Álbum de Figurinhas da Copa 2026

Projeto desenvolvido em Python para gerenciamento de figurinhas da Copa do Mundo 2026.

O sistema permite cadastrar, consultar, remover e persistir figurinhas, além de disponibilizar os dados através de uma API construída com Flask.

---

# Tecnologias utilizadas

* Python 3
* Flask
* JSON

---

# Arquitetura do Projeto

```text
JavaScript
    ↓
Flask API
    ↓
Album.py
    ↓
figurinhas.json
```

### Camadas

#### JavaScript

Responsável por consumir a API futuramente.

#### Flask API

Responsável por receber requisições HTTP e retornar respostas em JSON.

#### Album.py

Contém toda a regra de negócio do álbum.

#### figurinhas.json

Responsável por armazenar os dados das figurinhas.

---

# Estrutura do projeto

```bash
album-copa/

├── album.py
├── api.py
├── main.py
├── figurinhas.json
└── README.md
```

---

# Como executar o projeto

### Aplicação via terminal

```bash
python main.py
```

### API Flask

```bash
python api.py
```

Após iniciar a API:

```text
http://127.0.0.1:5000
```

---

# Funcionalidades atuais

## Terminal

* Adicionar figurinha
* Adicionar várias figurinhas
* Buscar figurinhas por país
* Remover figurinha
* Mostrar figurinhas agrupadas por país
* Mostrar figurinhas repetidas
* Salvar dados automaticamente em JSON

## API

* GET /info
* GET /figurinhas
* GET /pais/<nome>

---

# Conceitos praticados

* Programação Orientada a Objetos (POO)
* Classes
* Métodos
* Listas
* Dicionários
* Loops
* Condições
* Manipulação de arquivos JSON
* Organização em módulos
* APIs REST
* Flask
* Persistência de dados

---

# Roadmap

## Fase 1 

Album.py funcionando

## Fase 2 

Persistência com JSON

## Fase 3 

API Flask

## Fase 4 (Estou nessa fase)

* Criar POST /figurinhas
* Criar DELETE /figurinhas
* Validações básicas

## Fase 5

* JavaScript consumindo a API

## Fase 6

* Melhorias e validações

## Fase 7

* Migração para PostgreSQL

---

Projeto criado para prática, aprendizado de Python, APIs e desenvolvimento backend.
