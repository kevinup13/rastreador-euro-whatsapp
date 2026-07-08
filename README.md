# 📈 Rastreador de Cotação do Euro com Alertas Automatizados no WhatsApp

Este projeto é uma automação em Python desenvolvida para monitorar a cotação do Euro em tempo real e disparar notificações automáticas para o WhatsApp sempre que a moeda atingir um valor financeiro estratégico definido pelo usuário.

O projeto foi construído explorando duas abordagens distintas de desenvolvimento: **Automação de Interface (RPA)** e **Integração de APIs de Produção (Back-end)**.

---

## 🧠 Arquitetura e Abordagens Desenvolvidas

### 1. Abordagem via Interface (RPA) com `pywhatkit`

* **Como funciona:** O script utiliza o navegador local para abrir o *WhatsApp Web*, simular a digitação humana da mensagem e realizar o disparo através da interface gráfica.
* **Foco:** Solução ágil, local e 100% gratuita para automações desktop de rotina.

### 2. Abordagem Profissional via API com `Twilio SDK`

* **Como funciona:** O script comunica-se de forma silenciosa diretamente com os servidores da **Twilio** via requisições HTTP (POST), trafegando dados estruturados em segundo plano sem a necessidade de abrir navegadores.
* **Foco:** Arquitetura escalável de back-end, segura, performática e aderente aos padrões exigidos pelo mercado corporativo.

---

## 🛠️ Tecnologias e Conceitos Aplicados

* **Python 3.13+**
* **Consumo de APIs REST:** Utilização da biblioteca `requests` para captura de dados JSON atualizados da AwesomeAPI Economia.
* **Tratamento de Exceções:** Implementação de `raise_for_status()` para garantir a resiliência do sistema contra falhas de conexão de rede.
* **Segurança da Informação:** Isolamento de credenciais sensíveis (`Account SID` e `Auth Token`) utilizando variáveis de ambiente com `python-dotenv`.
* **Versionamento Limpo:** Uso estratégico de `.gitignore` para impedir o vazamento de chaves privadas e dependências locais (`venv/`).

---

## Como instalar as dependencias do projeto

``` bash
pip install -r requirements.txt
```

## Como executar

para o arquivo rastreador_alert.py

```bash
python rastreador_alert.py
```

para o arquivo rastreador.py

```bash
python rastreador.py
```
