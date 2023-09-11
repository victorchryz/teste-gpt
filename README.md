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
        python -m venv env  
        ```
        <code><img width="10" src="https://user-images.githubusercontent.com/25181517/186884153-99edc188-e4aa-4c84-91b0-e2df260ebc33.png" alt="Ubuntu" title="Ubuntu"/></code> **Linux**

        ```bash
        python3 -m venv env
        ```
- Ative o ambiente virtual usando:
       
     <code><img width="10" src="https://user-images.githubusercontent.com/25181517/186884150-05e9ff6d-340e-4802-9533-2c3f02363ee3.png" alt="Windows" title="Windows"/></code> **Windows**

     ```bash
     env\Scripts\activate
     ```
     <code><img width="10" src="https://user-images.githubusercontent.com/25181517/186884153-99edc188-e4aa-4c84-91b0-e2df260ebc33.png" alt="Ubuntu" title="Ubuntu"/></code> **Linux**
     
     ```bash
     source env/bin/activate
     ```
2.  Instale os requisitos executando o seguinte comando:

```bash
pip install -r requirements.txt
```

3.  Faça migrações executando:
```bash
python manage.py makemigrations
```

ou

```bash
python manage.py migrate
```

4. Execute o servidor local usando:

```bash
python manage.py runserver
```
e acesse [http://127.0.0.1:8000](http://127.0.0.1:8000) no seu navegador.
 
## Uso
Vá para OpenAI e obtenha sua [API key](https://platform.openai.com/account/api-keys) após abra o arquivo em ```teste-gpt/chatbot/.env``` e edite o **```.env```** Esse é o arquivo que você deve adicionar sua API Key.

```python
API_KEY= #Sua OpenAI API key.
```
ou

Após o login bem-sucedido, vá em **⚙ Configurações** na barra lateral da conta e atualize sua API Key.

## Contribuição
Contribuições são bem-vindas! Se você tiver sugestões, correções de bugs ou melhorias para este projeto, fique à vontade para abrir uma issue ou enviar um pull request.

Certifique-se de atualizar os testes conforme apropriado.

Para obter mais informações sobre a API usada, leia [isto](https://platform.openai.com/docs/api-reference).

## Créditos & Agradecimentos

Este projeto foi baseado em [test-gpt](https://github.com/s41ntm4rt1n/test-gpt),
Deixo aqui uma imensa gratidão ao [BRIANMARTIN](https://github.com/s41ntm4rt1n) pela enorme contribuição para o início deste projeto.