**🩸 Cadastro de Doadores de Sangue**

Este é um projeto simples em **Python** que realiza o cadastro básico de um possível doador de sangue e verifica se ele atende aos requisitos mínimos para doação.

O programa solicita algumas informações do usuário, calcula a idade automaticamente e informa se a pessoa pode ou não doar sangue com base nos critérios definidos.

---

 **👨‍💻 Autor**

**Brenno Gomes**

---

**📌 Funcionalidades**

* Solicita o **nome completo** do usuário.
* Solicita **peso**, **altura** e **ano de nascimento**.
* Calcula automaticamente a **idade** com base no ano atual.
* Verifica se o usuário atende aos requisitos mínimos para doação:

  * Idade mínima de **16 anos**
  * Peso superior a **50 kg**
* Exibe um **relatório final** com os dados informados e as verificações.

---

**⚙️ Tecnologias Utilizadas**

* **Python 3**
* Biblioteca padrão **datetime** (para calcular a idade automaticamente)

---

**▶️ Como Executar o Projeto**

1. Certifique-se de ter o **Python instalado** em seu computador.

2. Copie o código para um arquivo chamado:

```
cadastro_doadores.py
```

3. Execute o arquivo no terminal ou prompt de comando:

```
python cadastro_doadores.py
```

4. Siga as instruções exibidas no terminal.

---

**📋 Exemplo de Execução**

```
Cadastro de doadores de sangue
Por favor, informe seu nome completo: João Silva
Por favor, informe o seu peso em kg: 72
Por favor, informe sua altura em cm: 175
Por favor, me informa seu ano de nascimento: 2000

Pode doar sangue

    NOME: João Silva
    PESO: 72 kg
    ALTURA: 175 cm
    IDADE: 25
    TEM PESO MINIMO PARA DOAR: True
    TEM IDADE MINIMA PARA DOAR: True
```

---

**🎯 Objetivo do Projeto**

Este projeto foi desenvolvido com fins **educacionais**, para praticar conceitos básicos de programação em Python, como:

* Entrada de dados com `input()`
* Conversão de tipos (`int`, `float`)
* Uso de **condicionais (`if/else`)**
* Uso da biblioteca **datetime**
* Formatação de strings com **f-strings**

---

**📄 Licença**

Este projeto é de uso **educacional** e livre para estudo e modificações.
