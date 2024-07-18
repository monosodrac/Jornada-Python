# Título: NekkoChat
# Botão Iniciar Chat
    # Popup (janela na frente da tela)
    # Título: Bem-vindo ao NekkoChat
    # Campo de texto: -> Escreva seu nome no chat
    # Botão entrar no chat
        # Sumir com o título NekkoChat
        # Sumir com o botão iniciar chat
        # Fechar a janela (popup)
        # Carregar o chat
            # As mensagens que já foram enviadas
            # Campo: Digite sua mensagem
            # Botão de enviar
# pip install flet -> somente no terminal

# importar o flet
import flet as ft

# criar a função principal do aplicativo
def main(pagina):
    # criar todas as funcionalidades
    # criar o elemento
    titulo = ft.Text('NekkoChat')

    titulo_janela = ft.Text('Bem-vindo ao NekkoChat')
    campo_nome_usuario = ft.TextField(label='Escreva o seu nome no chat')

    chat = ft.Column()

    def enviar_msg_tunel(mensagem):
        texto_chat = ft.Text(mensagem)
        chat.controls.append(texto_chat)
        pagina.update()

    pagina.pubsub.subscribe(enviar_msg_tunel)

    def enviar_msg(evento):
        texto_msg = campo_msg.value
        nome_usuario = campo_nome_usuario.value
        mensagem = f'{nome_usuario}: {texto_msg}'
        pagina.pubsub.send_all(mensagem)
        campo_msg.value = ''
        pagina.update()

    campo_msg = ft.TextField(label='Digite sua mensagem', on_submit=enviar_msg)  # ft.FilePicker -> para adicionar opção de anexar arquivos
    botao_enviar_msg = ft.ElevatedButton('Enviar', on_click=enviar_msg)

    linha_msg = ft.Row([campo_msg, botao_enviar_msg])

    def entrar_chat(evento):
        # Sumir com o título NekkoChat
        pagina.remove(titulo)
        # Sumir com o botão iniciar chat
        pagina.remove(botao_iniciar)

        # Fechar a janela (popup)
        janela.open = False

        # Carregar o chat
        pagina.add(chat)
        pagina.add(linha_msg)   # pagina.add(campo_msg)   pagina.add(botao_enviar_msg)
        mensagem = f'{campo_nome_usuario.value} entrou no chat'
        pagina.pubsub.send_all(mensagem)

        pagina.update()

    botao_entrar = ft.ElevatedButton('Entrar no chat', on_click=entrar_chat)
    janela = ft.AlertDialog(title=titulo_janela, content=campo_nome_usuario, actions=[botao_entrar])

    def iniciar_chat(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()
    botao_iniciar = ft.ElevatedButton('Iniciar Chat', on_click=iniciar_chat)
    # adicionar o elemento na página
    pagina.add(titulo)
    pagina.add(botao_iniciar)

# rodar o aplicativo
ft.app(main, view=ft.WEB_BROWSER)