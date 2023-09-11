# Teste-GPT

Teste-GPT é um clone do Chat GPT utilizando Django com modelo GPT-3.5 da OpenAI.

## Instalação
Clone o repositório usando ``` git clone https://www.github.com/victorchryz/teste-gpt.git``` ou baixe o código do repositório para o seu computador local e extraia-o.
> [IMPORTANTE]
> 1. **Eu incentivo o uso de ambientes virtuais para separar as dependências do projeto dos pacotes locais. Leia mais sobre ambientes virtuais [aqui](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/).**
>  - Primeiro, certifique-se de ter o [python](https://www.python.org/) instalado em sua máquina local, pois você usará o [Python Package Installer (PIP)](https://pypi.org/project/pip/) para instalar as dependências do projeto.
   - Instale seu ambiente virtual usando
    
       <code><img width="10" src="https://user-images.githubusercontent.com/25181517/186884150-05e9ff6d-340e-4802-9533-2c3f02363ee3.png" alt="Windows" title="Windows"/></code> **Windows**
       
        ```bash
        python -m venv venv
        ```
        <code><img width="10" src="https://user-images.githubusercontent.com/25181517/186884153-99edc188-e4aa-4c84-91b0-e2df260ebc33.png" alt="Ubuntu" title="Ubuntu"/></code> **Linux**

        ```bash
        sudo apt install virtualenv
        ```
      e

        ```bash
        python3 -m venv venv
        ```
- Ative o ambiente virtual usando:
       
     <code><img width="10" src="https://user-images.githubusercontent.com/25181517/186884150-05e9ff6d-340e-4802-9533-2c3f02363ee3.png" alt="Windows" title="Windows"/></code> **Windows**

     ```bash
     venv\Scripts\activate
     ```
     <code><img width="10" src="https://user-images.githubusercontent.com/25181517/186884153-99edc188-e4aa-4c84-91b0-e2df260ebc33.png" alt="Ubuntu" title="Ubuntu"/></code> **Linux**
     
     ```bash
     source venv/bin/activate
     ```
2. Antes de executar os comandos abaixo, instale e/ou atualize os módulos pip e wheel do python executando o seguinte comando no terminal:

     <code><img width="10" src="https://user-images.githubusercontent.com/25181517/186884150-05e9ff6d-340e-4802-9533-2c3f02363ee3.png" alt="Windows" title="Windows"/></code> **Windows**

      ```bash
      python -m pip install --upgrade wheel pip 
      ```
     <code><img width="10" src="https://user-images.githubusercontent.com/25181517/186884153-99edc188-e4aa-4c84-91b0-e2df260ebc33.png" alt="Ubuntu" title="Ubuntu"/></code> **Linux**
     
      ```bash
      python3 -m pip install --upgrade wheel pip 
      ```

3.  Instale os requisitos executando o seguinte comando:

```bash
pip install --upgrade --no-cache-dir -r requirements.txt
```

4.  Faça migrações executando:

```bash
python manage.py migrate
```

ou

```bash
python manage.py makemigrations
```

## Uso

1. Gerando Django SECRET_KEY:

Quanto à chave SECRET_KEY no Django, ela é usada para criptografar e proteger informações sensíveis, como cookies e senhas. Essa chave é usada para garantir a segurança do seu aplicativo Django.

A chave SECRET_KEY é uma sequência de caracteres aleatórios e exclusivos que você deve gerar e manter em sigilo.

É importante manter sua chave SECRET_KEY em segredo e não compartilhá-la publicamente. Recomenda-se armazenar a chave em uma variável de ambiente ou em um arquivo separado que não seja controlado pelo sistema de controle de versão, como o Git.

Para gerar uma chave SECRET_KEY no Django, você pode usar uma função de geração de chave aleatória fornecida pelo próprio framework.

Você pode executar o seguinte comando no terminal para gerar uma nova chave SECRET_KEY:

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Isso irá gerar uma chave aleatória e exibi-la no terminal. Copie essa chave gerada.

Você pode definir a chave SECRET_KEY no arquivo de configuração chatbot/.env do seu projeto. Localize a linha que contém a definição da chave SECRET_KEY e substitua o valor atual pela nova chave gerada. Por exemplo:

```bash
SECRET_KEY=nova_SECRET_KEY_gerada
```

Certifique-se de substituir 'nova_chave_gerada' pela chave que você gerou anteriormente.

2. Vá para OpenAI e obtenha sua [API key](https://platform.openai.com/account/api-keys) após abra o arquivo em ```teste-gpt/chatbot/.env``` e edite o **```.env```** Esse é o arquivo que você deve adicionar sua API Key.


```python
OPENAI_API_KEY=sua_OPENAI_KEY_Aqui
```
ou

Após o login bem-sucedido, vá em **⚙ Configurações** na barra lateral da sua conta e atualize sua API Key.

3. Execute o servidor local usando:

```bash
python manage.py runserver
```
e acesse [http://127.0.0.1:8000](http://127.0.0.1:8000) no seu navegador.

## Contribuição
Contribuições são bem-vindas! Se você tiver sugestões, correções de bugs ou melhorias para este projeto, fique à vontade para abrir uma issue ou enviar um pull request.

Certifique-se de atualizar os testes conforme apropriado.

Para obter mais informações sobre a API usada, leia [isto](https://platform.openai.com/docs/api-reference).

## Créditos & Agradecimentos

Este projeto foi baseado em [test-gpt](https://github.com/s41ntm4rt1n/test-gpt),
Deixo aqui uma imensa gratidão ao [BRIANMARTIN](https://github.com/s41ntm4rt1n) pela enorme contribuição para o início deste projeto.