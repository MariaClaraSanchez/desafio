# Challenge

Este desafio envolve a implementação de um CRUD em Python sem o uso de frameworks.

## 🚀 Início

Antes de executar o programa, é necessário configurar o ambiente. Siga as etapas abaixo:

### 📋 Pré-requisitos do Back-end

- Certifique-se de ter o Python instalado na sua máquina.
- Crie um ambiente virtual.

### 🔧 Instalação

1. Instale o gerenciador de ambiente virtual com o seguinte comando:

```
pip install venv
```
2º Criar sua máquina virtual:
```
python -m venv nome_maquina_virtual-env
```
3º Escolha o comando de acordo com seu sistema opercional:
#### Para Windows:
```
nome_maquina_virtual-env\Scripts\activate
```
#### Para Unix ou no MacOS:
```
source nome_maquina_virtual-env/bin/activate
```

## Instalando Dependências
Antes de iniciar o projeto é necessário instalar as configurações de ambiente de um modo mais fácil e prático é só usar o gerenciado de pacote [pip](https://pip.pypa.io/en/stable/) para instalar as dependências.
```bash
pip install -r requirements.txt
```

## Arquivo Yaml

Para executar o projeto é necessário criar um arquivo `config.yaml` dentro da pasta back do projeto. Segue exemplo de estrutura do arquivo:

```yaml

db:
    host: "url"
    port: 100
    user: "nome-do-usuário"
    password: "senha"
    database: "nome-do-banco-de-dados"

```

### 📋 Pré-requisitos Back end

Dentro da pasta 'front', abra o arquivo 'tela1.html' e execute-o com um servidor local.
# Inicializando

Após seguir todas as etapas acima, é só inicializar e visualizar o projeto.
