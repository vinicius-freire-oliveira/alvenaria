"""
Quando num pano de parede existirem aberturas - portas, janelas, basculantes, elementos
vazados, há algumas regras práticas para o levantamento da área de alvenaria:
- Área da abertura inferior a 2 m² - despreza-se o vão da abertura, isto é, não se faz desconto algum na parede;
- Área da abertura igual ou superior a 2 m² - desconta-se da área total o que exceder a 2 m².
"""

class Parede:
    # Método inicializador da classe Parede, definindo a largura e altura da parede
    def __init__(self, largura, altura):
        self.largura = largura  # Define a largura da parede
        self.altura = altura  # Define a altura da parede
        self.aberturas = []  # Inicializa uma lista para armazenar as aberturas na parede

    # Método para adicionar uma abertura na parede
    def adicionar_abertura(self, largura, altura):
        # Adiciona uma tupla (largura, altura) na lista de aberturas
        self.aberturas.append((largura, altura))

    # Método para calcular a área total da parede descontando as aberturas
    def calcular_area(self):
        # Calcula a área total da parede sem descontar as aberturas
        area_parede = self.largura * self.altura
        area_aberturas = 0  # Inicializa a variável para acumular a área das aberturas

        # Itera sobre cada abertura na lista de aberturas
        for abertura in self.aberturas:
            largura_abertura, altura_abertura = abertura  # Desempacota a tupla em largura e altura
            area_abertura = largura_abertura * altura_abertura  # Calcula a área da abertura
            # Se a área da abertura for maior ou igual a 2 m², desconta 2 m² da área total das aberturas
            if area_abertura >= 2:
                area_aberturas += (area_abertura - 2)
        
        # Calcula a área total da parede descontando as aberturas
        area_total = area_parede - area_aberturas
        return area_total  # Retorna a área total calculada

# Exemplo de uso da classe Parede
parede = Parede(6.0, 2.8)  # Cria uma instância da classe Parede com largura 6.0 m e altura 2.8 m
parede.adicionar_abertura(1.5, 1.0)  # Adiciona uma abertura de 1.5 m de largura e 1.0 m de altura
parede.adicionar_abertura(1.5, 2.0)  # Adiciona uma abertura de 1.5 m de largura e 2.0 m de altura

# Calcula a área de alvenaria (área da parede descontando as aberturas)
area_calculada = parede.calcular_area()
# Exibe a área calculada formatada com duas casas decimais
print(f"A área de alvenaria é: {area_calculada:.2f} m²")

