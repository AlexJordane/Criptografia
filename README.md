# Criptografia a partir de Funções Afim

Conjunto de aplicações educacionais interativas (Web e Python) para o estudo de **Criptografia Clássica (Cifra Afim)**, **Funções Afim** e **Aritmética Modular**.

O projeto permite explorar na prática como uma função afim definida em módulo 26 pode ser utilizada para codificar mensagens de texto e sob quais condições algébricas existe uma função inversa capaz de decodificá-las.

## Links de Acesso

- **Aplicação Online (GitHub Pages):** https://alexjordane.github.io/Criptografia/
  - **Modo Exploratório (Chave Manual):** https://alexjordane.github.io/Criptografia/cripto.html
  - **Modo Automático (Chave Oculta):** https://alexjordane.github.io/Criptografia/cripto2.html
- **Repositório no GitHub:** https://github.com/AlexJordane/Criptografia/

---

## Fundamento Matemático

Cada letra do alfabeto ($A, B, C, \dots, Z$) é associada a um número inteiro de $0$ a $25$.

- **Codificação:** Aplica-se a função afim modular:
  $$C(x) = (ax + b) \pmod{26}$$
  onde $a$ e $b$ são números inteiros que compõem a chave da cifra, sendo necessário que $a$ e $26$ sejam primos entre si ($\text{mdc}(a, 26) = 1$).

- **Decodificação:** Aplica-se a função inversa utilizando o inverso multiplicativo $a^{-1} \pmod{26}$ (isto é, o inteiro tal que $a \cdot a^{-1} \equiv 1 \pmod{26}$):
  $$D(y) = a^{-1}(y - b) \pmod{26}$$

---

## Arquivos e Ferramentas do Repositório

### 1. Página Inicial (`index.html`)
Portal de entrada que apresenta o fundamento matemático da Cifra Afim e direciona para as duas ferramentas web interativas.

### 2. Cifra Afim com Parâmetros Manuais (`cripto.html`)
Ferramenta voltada para a experimentação pedagógica dos coeficientes:
- O usuário escolhe manualmente os valores inteiros de $a$ (coprimo com 26) e $b$.
- Calcula e exibe automaticamente em tempo real o inverso multiplicativo $a^{-1} \pmod{26}$.
- Padroniza o texto (remove acentos, espaços e pontuações) e realiza a codificação ou decodificação.

### 3. Codificador com Chave Oculta / Automática (`cripto2.html`)
Ferramenta pensada para dinâmicas de troca de mensagens cifradas sem necessidade de combinar previamente os valores de $a$ e $b$:
- **Ao codificar:** Sorteia aleatoriamente um coeficiente $a$ coprimo com 26 (positivo ou negativo) e um deslocamento $b$, cifra a mensagem e embute os parâmetros codificados nos **2 primeiros** e nos **2 últimos** caracteres do criptograma.
- **Ao decodificar:** Extrai automaticamente os valores de $a$ e $b$ das extremidades da mensagem cifrada, calcula $a^{-1} \pmod{26}$ e restaura o texto original.

### 4. Script em Python (`cripto.py`)
Implementação em linha de comando (CLI) em Python puro das funções `inverso_multiplicativo`, `codificar` e `decodificar`, ideal para estudo do algoritmo em disciplinas de programação e matemática.

**Como executar o script Python:**
```bash
python3 cripto.py
```

---

## Autoria

Elaborado por **Alex Jordane**, em colaboração com Inteligência Artificial (Gemini).
