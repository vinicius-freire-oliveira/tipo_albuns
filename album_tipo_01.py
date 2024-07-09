# Definindo a classe Albuns
class Albuns:
    # Método de inicialização da classe, recebe nome e ano como parâmetros e os atribui aos atributos internos
    def __init__(self, nome, ano):
        self._nome = nome
        self.ano = ano

    # Propriedade que retorna o nome do álbum
    @property
    def nome(self):
        return self._nome
    
    # Setter para modificar o nome do álbum
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    # Método para retornar uma representação em string do álbum
    def __str__(self):
        return f'{self.ano} - {self.nome}'

# Definindo a classe Coletaneas que herda de Albuns
class Coletaneas(Albuns):
    # Método de inicialização da classe, recebe nome, descricao e ano como parâmetros
    def __init__(self, nome, descricao, ano):
        # Chama o método de inicialização da superclasse (Albuns)
        super().__init__(nome, ano)
        self.descricao = descricao

    # Método para retornar uma representação em string da coletânea
    def __str__(self):
        return f'{self.ano} - {self.nome} - {self.descricao}'

# Definindo a classe Soundtracks que herda de Albuns
class Soundtracks(Albuns):
    # Método de inicialização da classe, recebe nome, descricao e ano como parâmetros
    def __init__(self, nome, descricao, ano):
        # Chama o método de inicialização da superclasse (Albuns)
        super().__init__(nome, ano)
        self.descricao = descricao

    # Método para retornar uma representação em string do soundtrack
    def __str__(self):
        return f'{self.ano} - {self.nome} - {self.descricao}'

# Definindo a classe Tributos que herda de Albuns
class Tributos(Albuns):
    # Método de inicialização da classe, recebe nome, tributo e ano como parâmetros
    def __init__(self, nome, tributo, ano):
        # Chama o método de inicialização da superclasse (Albuns)
        super().__init__(nome, ano)
        self.tributo = tributo

    # Método para retornar uma representação em string do tributo
    def __str__(self):
        return f'{self.ano} - {self.nome} - {self.tributo}'

# Definindo a classe ArquivoTexto
class ArquivoTexto:
    # Método de inicialização da classe, recebe o nome do arquivo como parâmetro e armazena em atributo privado
    def __init__(self, nome):
        self.__nome = nome

    # Método para imprimir o conteúdo do arquivo
    def imprimir_conteudo(self):
        with open(self.__nome, 'r') as arquivo:
            conteudo = arquivo.read()
            print(f"Conteúdo do arquivo {self.__nome}:")
            print(conteudo)
            print()

    # Método para retornar o nome do arquivo
    def get_nome(self):
        return self.__nome

    # Método que retorna a quantidade de linhas do arquivo
    def __len__(self):
        with open(self.__nome, 'r') as arquivo:
            linhas = arquivo.readlines()
        return len(linhas)

    # Método para imprimir a lista de álbuns no arquivo
    def imprimir_lista(self):
        with open(self.__nome, 'r') as arquivo:
            linhas = arquivo.readlines()
        # Lê a primeira linha do arquivo de texto e remove quaisquer espaços em branco no início e no final da linha.
        tipo_album = linhas[0].strip()
        classe_album = None

        # Verifica o tipo de álbum e define a classe correspondente
        if tipo_album == 'Coletaneas':
            classe_album = Coletaneas
        elif tipo_album == 'Soundtracks':
            classe_album = Soundtracks
        elif tipo_album == 'Tributos':
            classe_album = Tributos

        if classe_album:
            lista_albums = []
            # Itera sobre cada linha no objeto 'linhas', excluindo a primeira linha (índice 0).
            for linha in linhas[1:]:
                # Remove espaços em branco e divide a linha pelo caractere '-'.
                dados = linha.strip().split('-')
                # Cria um objeto 'album' usando a classe 'classe_album' com os dados obtidos da linha.
                album = classe_album(*dados)
                # Adiciona o objeto 'album' à lista 'lista_albums'.
                lista_albums.append(album)
                # Imprime o objeto 'album'.
                print(album)

            print(f"Tamanho da lista de {self.__nome}: {len(lista_albums)}")
            print()

# Criando objetos da classe ArquivoTexto para cada arquivo
coletaneas = ArquivoTexto('listagem_coletaneas.txt')
soundtracks = ArquivoTexto('listagem_soundtracks.txt')
tributos = ArquivoTexto('listagem_tributos.txt')

# Chamando o método imprimir_conteudo em cada objeto para imprimir o conteúdo dos arquivos
coletaneas.imprimir_conteudo()
soundtracks.imprimir_conteudo()
tributos.imprimir_conteudo()

# Imprimindo a lista de cada arquivo, o tamanho da lista utilizando o método __len__
coletaneas.imprimir_lista()
print(f"Tamanho da lista de {coletaneas.get_nome()}: {len(coletaneas)}")

soundtracks.imprimir_lista()
print(f"Tamanho da lista de {soundtracks.get_nome()}: {len(soundtracks)}")

tributos.imprimir_lista()
print(f"Tamanho da lista de {tributos.get_nome()}: {len(tributos)}")
