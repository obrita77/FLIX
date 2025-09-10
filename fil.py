from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
import random

# Cores personalizadas
COR_FUNDO = (0, 0, 0, 1)                 # Preto
COR_TEXTO = (1, 0, 0, 1)                 # Vermelho
COR_BOTAO = (1, 1, 1, 1)                 # Branco
COR_BOTAO_SELECIONADO = (0.3, 0.3, 0.3, 1)  # Cinza escuro para botão selecionado

# Listas de filmes por gênero com anos de lançamento
FILMES_ACAO = [
    {"nome": "Matrix", "ano": 1999},
    {"nome": "Mad Max: Estrada da Fúria", "ano": 2015},
    {"nome": "John Wick", "ano": 2014},
    {"nome": "Duro de Matar", "ano": 1988},
    {"nome": "Missão Impossível", "ano": 1996}
]

FILMES_COMEDIA = [
    {"nome": "Se Beber, Não Case", "ano": 2009},
    {"nome": "As Branquelas", "ano": 2004},
    {"nome": "Superbad", "ano": 2007},
    {"nome": "Escola de Rock", "ano": 2003},
    {"nome": "Debi & Lóide", "ano": 1994}
]

FILMES_ANIMACAO = [
    {"nome": "Toy Story", "ano": 1995},
    {"nome": "O Rei Leão", "ano": 1994},
    {"nome": "Procurando Nemo", "ano": 2003},
    {"nome": "Frozen", "ano": 2013},
    {"nome": "Shrek", "ano": 2001}
]

FILMES_DRAMA = [
    {"nome": "O Poderoso Chefão", "ano": 1972},
    {"nome": "Forrest Gump", "ano": 1994},
    {"nome": "Cidadão Kane", "ano": 1941},
    {"nome": "Um Sonho de Liberdade", "ano": 1994},
    {"nome": "A Lista de Schindler", "ano": 1993}
]

class FilmeApp(App):
    def build(self):
        # Layout principal
        self.layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
       
        # Fundo colorido
        with self.layout.canvas.before:
            Color(*COR_FUNDO)
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)
       
        # Atualizar fundo ao redimensionar
        self.layout.bind(size=self.atualizar_fundo, pos=self.atualizar_fundo)
       
        # Título
        titulo = Label(
            text="Sugestor de Filmes por Gênero",
            font_size=24,
            bold=True,
            color=COR_TEXTO
        )
        self.layout.add_widget(titulo)
       
        # Campo de nome
        self.campo_nome = TextInput(
            hint_text="Digite seu nome",
            size_hint=(1, None),
            height=50,
            foreground_color=COR_TEXTO,
            background_color=(1, 1, 1, 0.9)
        )
        self.layout.add_widget(self.campo_nome)
       
        # Label para seleção de gênero
        label_genero = Label(
            text="Selecione um gênero:",
            color=COR_TEXTO,
            font_size=18,
            size_hint=(1, None),
            height=30
        )
        self.layout.add_widget(label_genero)
       
        # Layout para os botões de gênero
        grid_generos = GridLayout(cols=2, spacing=10, size_hint=(1, None), height=100)
        self.layout.add_widget(grid_generos)
       
        # Botões de seleção de gênero (ToggleButtons)
        self.genero_acao = ToggleButton(
            text="Ação",
            group="generos",
            background_color=COR_BOTAO,
            color=COR_FUNDO
        )
       
        self.genero_comedia = ToggleButton(
            text="Comédia",
            group="generos",
            background_color=COR_BOTAO,
            color=COR_FUNDO
        )
       
        self.genero_animacao = ToggleButton(
            text="Animação",
            group="generos",
            background_color=COR_BOTAO,
            color=COR_FUNDO
        )
       
        self.genero_drama = ToggleButton(
            text="Drama",
            group="generos",
            background_color=COR_BOTAO,
            color=COR_FUNDO
        )
       
        # Adicionar botões ao grid
        grid_generos.add_widget(self.genero_acao)
        grid_generos.add_widget(self.genero_comedia)
        grid_generos.add_widget(self.genero_animacao)
        grid_generos.add_widget(self.genero_drama)
       
        # Layout para botões de ação
        grid_botoes = GridLayout(cols=2, spacing=10, size_hint=(1, None), height=50)
        self.layout.add_widget(grid_botoes)
       
        # Botão de sugestão
        botao_sugerir = Button(
            text="Sugerir Filme",
            background_color=COR_BOTAO,
            color=COR_FUNDO,
            bold=True
        )
        botao_sugerir.bind(on_press=self.sugerir_filme)
        grid_botoes.add_widget(botao_sugerir)
       
        # Botão limpar
        botao_limpar = Button(
            text="Limpar",
            background_color=COR_BOTAO,
            color=COR_FUNDO,
            bold=True
        )
        botao_limpar.bind(on_press=self.limpar_campos)
        grid_botoes.add_widget(botao_limpar)
       
        # Mensagem de sugestão
        self.label_sugestao = Label(
            text="",
            color=COR_TEXTO,
            font_size=20,
            size_hint=(1, None),
            height=60
        )
        self.layout.add_widget(self.label_sugestao)
       
        # Mensagem adicional
        self.label_extra = Label(
            text="",
            color=COR_TEXTO,
            font_size=16,
            italic=True,
            size_hint=(1, None),
            height=30
        )
        self.layout.add_widget(self.label_extra)
       
        # Mensagem de erro
        self.label_erro = Label(
            text="",
            color=COR_TEXTO,
            font_size=16,
            size_hint=(1, None),
            height=30
        )
        self.layout.add_widget(self.label_erro)
       
        # Inicializar gênero selecionado
        self.genero_selecionado = None
       
        # Vincular eventos aos botões de gênero
        self.genero_acao.bind(on_press=self.selecionar_genero)
        self.genero_comedia.bind(on_press=self.selecionar_genero)
        self.genero_animacao.bind(on_press=self.selecionar_genero)
        self.genero_drama.bind(on_press=self.selecionar_genero)
       
        return self.layout

    def atualizar_fundo(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def selecionar_genero(self, instance):
        self.genero_selecionado = instance.text
        instance.background_color = COR_BOTAO_SELECIONADO
        for btn in [self.genero_acao, self.genero_comedia, self.genero_animacao, self.genero_drama]:
            if btn != instance:
                btn.background_color = COR_BOTAO

    def sugerir_filme(self, instance):
        self.label_erro.text = ""
        self.label_sugestao.text = ""
        self.label_extra.text = ""
       
        nome = self.campo_nome.text.strip()
       
        if not nome:
            self.label_erro.text = "Erro: digite seu nome para continuar"
            return
        if nome.isdigit():
            self.label_erro.text = "Erro: por favor, digite um nome válido"
            return
        if not self.genero_selecionado:
            self.label_erro.text = "Erro: selecione um gênero de filme"
            return
       
        if self.genero_selecionado == "Ação":
            filme = random.choice(FILMES_ACAO)
        elif self.genero_selecionado == "Comédia":
            filme = random.choice(FILMES_COMEDIA)
        elif self.genero_selecionado == "Animação":
            filme = random.choice(FILMES_ANIMACAO)
        elif self.genero_selecionado == "Drama":
            filme = random.choice(FILMES_DRAMA)
        else:
            self.label_erro.text = "Erro: gênero não reconhecido"
            return
       
        self.label_sugestao.text = f"Olá, {nome}! Sua sugestão de filme de {self.genero_selecionado} é: {filme['nome']} ({filme['ano']})."
        self.label_extra.text = "Acho que você possa gostar desse filme!"

    def limpar_campos(self, instance):
        self.campo_nome.text = ""
        self.label_sugestao.text = ""
        self.label_extra.text = ""
        self.label_erro.text = ""
        for btn in [self.genero_acao, self.genero_comedia, self.genero_animacao, self.genero_drama]:
            btn.state = 'normal'
            btn.background_color = COR_BOTAO
        self.genero_selecionado = None

if __name__ == '__main__':
    FilmeApp().run()
