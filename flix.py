import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

# Configurações da janela
Window.size = (400, 700)
Window.clearcolor = (0, 0, 0, 1)  # FUNDO PRETO

class FilmeSorteadorApp(App):
    def build(self):
        # Lista de filmes com ano
        self.filmes = [
            ("Matrix", 1999),
            ("Toy Story", 1995),
            ("Avatar", 2009),
            ("O Rei Leão", 1994),
            ("Homem-Aranha", 2002),
            
        ]

        # Layout principal
        layout = BoxLayout(orientation='vertical', spacing=15, padding=25)

        # Título
        self.titulo = Label(
            text="MATIAXX77FLIX",
            font_size=28,
            color=(0.8, 0.8, 1, 1),  # Azul claro para contrastar com preto
            size_hint=(1, 0.15),
            bold=True
        )
        layout.add_widget(self.titulo)

        # Campo de texto para o nome
        self.nome_input = TextInput(
            hint_text="Digite seu nome",
            hint_text_color=(0.6, 0.6, 0.6, 1),  # Cinza para hint
            multiline=False,
            font_size=18,
            size_hint=(1, 0.12),
            background_color=(0.15, 0.15, 0.15, 1),  # Cinza muito escuro
            foreground_color=(1, 1, 1, 1),  # Texto branco
            cursor_color=(0.4, 0.6, 1, 1),  # Azul para cursor
            padding_y=(10, 10)
        )
        layout.add_widget(self.nome_input)

        # Botão para sugerir filme
        self.botao = Button(
            text="SORTEAR FILME",
            font_size=20,
            size_hint=(1, 0.12),
            background_color=(0.9, 0.2, 0.2, 1),  # VERMELHO
            background_normal='',
            color=(1, 1, 1, 1),  # Texto branco
            bold=True
        )
        self.botao.bind(on_press=self.sugerir_filme)
        layout.add_widget(self.botao)

        # Label para exibir o resultado
        self.resultado_label = Label(
            text="Digite seu nome e clique para sortear",
            font_size=18,
            color=(0.8, 0.8, 0.8, 1),  # Cinza claro
            size_hint=(1, 0.15),
            halign='center',
            valign='middle'
        )
        layout.add_widget(self.resultado_label)

        # Título do catálogo
        catalogo_titulo = Label(
            text="CATÁLOGO DE FILMES ",
            font_size=20,
            color=(1, 1, 1, 1),  # BRANCO (alterado de amarelo)
            size_hint=(1, 0.08),
            bold=True
        )
        layout.add_widget(catalogo_titulo)

        # ScrollView para a lista de filmes
        scroll = ScrollView(size_hint=(1, 0.3))
        
        # GridLayout para os filmes
        filmes_layout = GridLayout(cols=1, spacing=5, size_hint_y=None)
        filmes_layout.bind(minimum_height=filmes_layout.setter('height'))
        
        # Adicionar cada filme à lista
        for filme, ano in self.filmes:
            filme_label = Label(
                text=f"• {filme} ({ano})",
                font_size=16,
                color=(1, 1, 1, 1),  # BRANCO (alterado de azul claro)
                size_hint_y=None,
                height=30,
                halign='left',
                text_size=(380, None)
            )
            filmes_layout.add_widget(filme_label)
        
        scroll.add_widget(filmes_layout)
        layout.add_widget(scroll)

        return layout

    def sugerir_filme(self, instance):
        nome = self.nome_input.text.strip()

        if nome == "":
            self.resultado_label.text = "Por favor, digite seu nome."
            self.resultado_label.color = (1, 0.5, 0.5, 1)  # Vermelho claro para erro
            return

        # Sorteia um filme aleatório
        filme, ano = random.choice(self.filmes)

        # Exibe a mensagem final
        self.resultado_label.text = f"Olá, {nome}! 🎉\nSua sugestão de filme é:\n[b]{filme} ({ano})[/b]"
        self.resultado_label.markup = True
        self.resultado_label.color = (0.6, 1, 0.6, 1)  # Verde claro para sucesso

# Executar o app
if __name__ == '__main__':
    FilmeSorteadorApp().run()