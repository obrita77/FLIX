import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle

# Configurações da janela
Window.size = (450, 800)  
Window.clearcolor = (0, 0, 0, 1)  

class FilmeSorteadorApp(App):
    def build(self):
        # Lista de filmes com ano e gênero
        self.filmes = [
            {"nome": "Matrix", "ano": 1999, "genero": "Ficção Científica", "emoji": ""},
            {"nome": "Toy Story", "ano": 1995, "genero": "Animação", "emoji": ""},
            {"nome": "Avatar", "ano": 2009, "genero": "Aventura", "emoji": ""},
            
        ]

        # Layout principal
        layout = BoxLayout(orientation='vertical', spacing=12, padding=20)

        # Título
        self.titulo = Label(
            text=" MATIAXX77FLIX ",
            font_size=30,
            color=(0.9, 0.9, 1, 1),
            size_hint=(1, 0.1),
            bold=True
        )
        layout.add_widget(self.titulo)

        # Campo de texto para o nome
        self.nome_input = TextInput(
            hint_text="Digite seu nome aqui...",
            hint_text_color=(0.6, 0.6, 0.6, 1),
            multiline=False,
            font_size=18,
            size_hint=(1, 0.08),
            background_color=(0.15, 0.15, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(0.4, 0.6, 1, 1),
            padding=[15, 10],
            background_normal=''
        )
        layout.add_widget(self.nome_input)

        # Botão para sugerir filme
        self.botao = Button(
            text="SORTEAR FILME ALEATÓRIO",
            font_size=20,
            size_hint=(1, 0.08),
            background_color=(0.9, 0.2, 0.2, 1),
            background_normal='',
            color=(1, 1, 1, 1),
            bold=True
        )
        self.botao.bind(on_press=self.sugerir_filme)
        layout.add_widget(self.botao)

        # Separador
        separador = Label(
            text="▬" * 30,
            font_size=16,
            color=(0.4, 0.4, 0.4, 1),
            size_hint=(1, 0.04)
        )
        layout.add_widget(separador)

        # Título do catálogo
        catalogo_titulo = Label(
            text=" CATÁLOGO COMPLETO DE FILMES",
            font_size=22,
            color=(1, 1, 1, 1),
            size_hint=(1, 0.06),
            bold=True
        )
        layout.add_widget(catalogo_titulo)

        # Subtítulo do catálogo
        catalogo_subtitulo = Label(
            text=f"Total de {len(self.filmes)} filmes disponíveis",
            font_size=14,
            color=(0.7, 0.7, 0.7, 1),
            size_hint=(1, 0.04),
            italic=True
        )
        layout.add_widget(catalogo_subtitulo)

        # ScrollView para a lista de filmes
        scroll = ScrollView(size_hint=(1, 0.4), bar_width=10)
        
        # GridLayout para os filmes
        filmes_layout = GridLayout(cols=1, spacing=8, size_hint_y=None, padding=[0, 5])
        filmes_layout.bind(minimum_height=filmes_layout.setter('height'))
        
        # Adicionar cada filme à lista com layout melhorado
        for i, filme in enumerate(self.filmes, 1):
            # Container para cada filme
            filme_container = BoxLayout(
                orientation='horizontal', 
                size_hint_y=None, 
                height=60,
                spacing=10
            )
            
            # Número do filme
            numero_label = Label(
                text=f"{i:02d}",
                font_size=14,
                color=(0.6, 0.8, 1, 1),
                size_hint_x=0.1,
                bold=True
            )
            
            # Emoji e informações do filme
            info_container = BoxLayout(orientation='vertical', spacing=2)
            
            # Nome do filme com emoji
            nome_label = Label(
                text=f"{filme['emoji']} [b]{filme['nome']}[/b]",
                font_size=16,
                color=(1, 1, 1, 1),
                size_hint_y=0.6,
                halign='left',
                markup=True
            )
            
            # Detalhes do filme
            detalhes_label = Label(
                text=f" {filme['genero']} •  {filme['ano']}",
                font_size=12,
                color=(0.8, 0.8, 0.8, 1),
                size_hint_y=0.4,
                halign='left'
            )
            
            info_container.add_widget(nome_label)
            info_container.add_widget(detalhes_label)
            
            filme_container.add_widget(numero_label)
            filme_container.add_widget(info_container)
            
            # Adicionar retângulo de fundo para cada filme
            with filme_container.canvas.before:
                Color(0.1, 0.1, 0.1, 1)
                Rectangle(pos=filme_container.pos, size=filme_container.size)
            
            filmes_layout.add_widget(filme_container)
        
        scroll.add_widget(filmes_layout)
        layout.add_widget(scroll)

        # Separador antes da sugestão
        separador_sugestao = Label(
            text="⭐" * 20,
            font_size=16,
            color=(0.4, 0.4, 0.4, 1),
            size_hint=(1, 0.04)
        )
        layout.add_widget(separador_sugestao)

        # ÁREA DA SUGESTÃO DE FILME (NO FINAL)
        self.sugestao_titulo = Label(
            text="AGUARDANDO SORTEIO",
            font_size=20,
            color=(0.7, 0.7, 0.7, 1),
            size_hint=(1, 0.06),
            bold=True
        )
        layout.add_widget(self.sugestao_titulo)

        self.resultado_label = Label(

            font_size=16,
            color=(0.6, 0.6, 0.6, 1),
            size_hint=(1, 0.15),
            halign='center',
            valign='middle',
            text_size=(400, None)
        )
        layout.add_widget(self.resultado_label)

        # Rodapé
        rodape = Label(
            
            font_size=12,
            color=(0.5, 0.5, 0.5, 1),
            size_hint=(1, 0.04)
        )
        layout.add_widget(rodape)

        return layout

    def sugerir_filme(self, instance):
        nome = self.nome_input.text.strip()

        if nome == "":
            self.sugestao_titulo.text = "ERRO"
            self.sugestao_titulo.color = (1, 0.5, 0.5, 1)
            self.resultado_label.text = "Por favor, digite seu nome primeiro!\n\nClique no campo acima e digite seu nome."
            self.resultado_label.color = (1, 0.6, 0.6, 1)
            return

        # Sorteia um filme aleatório
        filme = random.choice(self.filmes)

        # Atualiza o título da sugestão
        self.sugestao_titulo.text = " FILME SORTEADO!"
        self.sugestao_titulo.color = (0.6, 1, 0.6, 1)

        # Exibe a mensagem final NO FINAL DA PÁGINA
        self.resultado_label.text = f"""[b] {nome.upper()}![/b]

 [b]SUA SUGESTÃO DE FILME É:[/b]
{filme['emoji']} [b]{filme['nome']}[/b] ({filme['ano']})
 {filme['genero']}

 [i]Bom filme![/i]"""
        self.resultado_label.markup = True
        self.resultado_label.color = (1, 1, 1, 1)

# Executar o app
if __name__ == '__main__':
    FilmeSorteadorApp().run()