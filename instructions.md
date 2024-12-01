# Guia: Como Rodar a Aplicação do Zero

Este guia descreve os passos necessários para configurar, construir e executar a aplicação a partir do zero.

---

## Passo 1: Instalar Dependências
Execute o comando abaixo para instalar todas as dependências necessárias:

```bash
npm install
```

## Passo 2: Construir a Nova Versão do Aplicativo
Gere o build da nova versão do aplicativo com o comando:

```bash
npm run dump app -- -r requirements.txt
```

## Passo 3: Testar a Aplicação
Para testar a aplicação localmente, execute:

```bash
npm run serve
```

## Passo 4: Gerar Distribuição Final
Para gerar o build de produção da aplicação, utilize:

```bash
npm run dist
```