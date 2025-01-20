
# WhatsApp Auto Sender

Este script permite enviar mensagens automaticamente pelo WhatsApp Web utilizando `pywhatkit` para enviar mensagens instantâneas e `selenium` para clicar no botão de envio.

## Requisitos

Antes de rodar o script, instale as dependências necessárias:

- `pywhatkit`
- `selenium`
- `webdriver-manager`
- `datetime`

Você pode instalar as dependências com o seguinte comando:

```bash
pip install pywhatkit selenium webdriver-manager
```

## Como Usar

1. Certifique-se de que o WhatsApp Web está funcionando no navegador Microsoft Edge.
2. Execute o script.
3. O script pedirá para você inserir o número de telefone e a mensagem.
4. O script abrirá o WhatsApp Web e enviará a mensagem.

### Exemplo de Execução

```bash
Enter the message: Olá, tudo bem?
Enter the phone number: +551200024444

O script usará o número fornecido e enviará a mensagem inserida para esse número.

## Funcionamento

1. Envio Instantâneo: O `pywhatkit.sendwhatmsg_instantly` envia a mensagem diretamente.
2. Automação com Selenium: O Selenium é usado para clicar automaticamente no botão de envio do WhatsApp Web.

## Observações

- O script usa o Microsoft Edge, certifique-se de ter o navegador instalado.
- É necessário escanear o QR Code do WhatsApp Web antes de rodar o script.
