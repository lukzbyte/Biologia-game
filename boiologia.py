import time
import os
import sys
import random
from colorama import Fore as cor, Style as estilo


sys.set_int_max_str_digits(10000000)

cores_aleatorias = [cor.BLACK, cor.BLUE, cor.RED, cor.GREEN, cor.YELLOW, cor.CYAN, cor.MAGENTA]

def print_bonito(texto, delay=0.001):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(delay)

def input_bonito(texto, delay=0.001):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(delay)
    input()

    

def alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais):
    decisao = input(estilo.RESET_ALL)
    print_bonito("E a resposta está...........\n")
    if decisao == alternativa_certa:
        jogador['pontuacao'] += pontos_totais
        print_bonito(cor.GREEN+"Correto\n"+estilo.RESET_ALL)
    else:
        print_bonito(cor.RED+"Errada\n"+estilo.RESET_ALL)
        if rolar_dado == 0:
            pontos_totais /= 2
            jogador['pontuacao'] += pontos_totais

jogadores_participando = []
jogo_ativado = 1

biologia_titulo = ("""
   ____ ___ ___  _     ___   ____ ___    _      
  | __ )_ _/ _ \| |   / _ \ / ___|_ _|  / \     
  |  _ \| | | | | |  | | | | |  _ | |  / _ \    
  | |_) | | |_| | |__| |_| | |_| || | / ___ \   
 _|____/___\___/|_____\___/ \____|___/_/_ _\_\_ 
|_   _| | | | ____|  / ___|  / \  |  \/  | ____|
  | | | |_| |  _|   | |  _  / _ \ | |\/| |  _|  
  | | |  _  | |___  | |_| |/ ___ \| |  | | |___ 
  |_| |_| |_|_____|  \____/_/   \_\_|  |_|_____|""")
facil_texto = (""" _____ __       _ _ 
|  ___/_/_  ___(_) |
| |_ / _` |/ __| | |
|  _| (_| | (__| | |
|_|  \__,_|\___|_|_|""")
medio_texto = (""" __  __   __     _ _       
|  \/  | /_/  __| (_) ___  
| |\/| |/ _ \/ _` | |/ _ \ 
| |  | |  __/ (_| | | (_) |
|_|  |_|\___|\__,_|_|\___/ """)
dificil_texto = (""" ____  _  __ __     _ _ 
|  _ \(_)/ _/_/ ___(_) |
| | | | | |_| |/ __| | |
| |_| | |  _| | (__| | |
|____/|_|_| |_|\___|_|_|""")
regras_texto = ("""
 ____                          
|  _ \ ___  __ _ _ __ __ _ ___ 
| |_) / _ \/ _` | '__/ _` / __|
|  _ <  __/ (_| | | | (_| \__ 
|_| \_\___|\__, |_|  \__,_|___/
           |___/               """)


while jogo_ativado == 1:
    os.system('cls')
    print(cor.LIGHTGREEN_EX+biologia_titulo,"\n")
    input("               Pressione Enter")
    while True:
        jogadores_participando.clear()
        os.system('cls')
        print_bonito(estilo.RESET_ALL+"Quantos jogadores vai jogar (max. 7)?\n")
        qnt_de_jogadores = input()

        if qnt_de_jogadores.isdigit() and 1 <= int(qnt_de_jogadores) <= 7:
            for i in range(int(qnt_de_jogadores)):
                print_bonito(f"Digite o nome do jogador {i+1}: ")
                jogador_nome = input()
                entrada = random.randint(1,7)
                cor_jogador = random.choice(cores_aleatorias)
                pontuacao = 0

                while any(jogador['entrada'] == entrada for jogador in jogadores_participando):
                    entrada = random.randint(1,7)

                while any(jogador['cor'] == cor_jogador for jogador in jogadores_participando):
                    cor_jogador = random.choice(cores_aleatorias)

                jogador = {'nome': jogador_nome, 'entrada': entrada, 'cor':cor_jogador, 'pontuacao':pontuacao}
                jogadores_participando.append(jogador)
            os.system('cls')
            for jogador in jogadores_participando:
                print(jogador['cor']+f"Jogador: {jogador['nome']} |Sua rodada: {jogador['entrada']}" + estilo.RESET_ALL)
            print_bonito("\nOs dados estão corretos?\n")
            print_bonito(cor.YELLOW+("(1. Sim) (2. Não)\n"))
            decisao = input(estilo.RESET_ALL)
            if decisao == "1":
                break
                
                
            
        else:
            input_bonito("Inválido, coloque as quantidade de jogadores novamente (Pressione Enter)")
            os.system('cls')
    jogadores_participando = sorted(jogadores_participando, key=lambda x: x['entrada'])
    gameplay = 1

    os.system('cls')
    print_bonito(f"{cor.CYAN+regras_texto}\n")
    print_bonito(estilo.RESET_ALL+"Cada jogador irá sortear leatoriamente uma pergunta facil, média e difícil \nE então o jogador poderá decidir se vai rolar um dado para multiplicar seus pontos que serão ganhos\n")
    print_bonito("Se o jogador optar por rolar o dado e errar a pergunta, ele não ganhará nenhum ponto, caso contrário ganhará apenas metade dos pontos \nO objetivo é conseguir o máximo de pontos em até 5 rodadas\n")
    input_bonito(f"\nPerguntas {cor.GREEN +"Fáceis"+ estilo.RESET_ALL} = 2 pontos\nPerguntas {cor.YELLOW +"Médias"+ estilo.RESET_ALL} = 4 pontos\nPerguntas {cor.RED +"Difíceis"+ estilo.RESET_ALL} = 6 pontos\n(Pressione Enter)")
    rodadas = 1
    while gameplay == 1:
        for jogador in jogadores_participando:
            os.system('cls')
            rolar_dado = 0
            selecao_de_dificuldade = random.randint(1,4)
            print_bonito(f"A pergunta sorteada possui dificuldade.............\n")
            if selecao_de_dificuldade == 1:
                print(f"{cor.GREEN +facil_texto+ estilo.RESET_ALL}\n")
                pontos_totais = 2
            elif  selecao_de_dificuldade == 2 or selecao_de_dificuldade == 4:
                print(f"{cor.YELLOW +medio_texto+ estilo.RESET_ALL}\n")
                selecao_de_dificuldade = 2
                pontos_totais = 4
            elif selecao_de_dificuldade == 3:
                print(f"{cor.RED +dificil_texto+ estilo.RESET_ALL}\n")
                pontos_totais = 6

            print_bonito(f"Você, jogador {jogador['cor']+jogador['nome'] + estilo.RESET_ALL}, gostaria de rolar um dado para multiplicar seu ganho de pontos?\n")
            print_bonito(cor.YELLOW+"(1. Sim) (2. Não)\n")
            decisao = input(estilo.RESET_ALL)
            os.system('cls')
            if decisao == "1":
                rolar_dado = random.randint(1,6)
                pontos_totais *= rolar_dado
                print_bonito(f"O jogador {jogador['cor']+jogador['nome'] + estilo.RESET_ALL} Rolou um {rolar_dado}\n")
            input_bonito(f"O jogador pode ganhar até {pontos_totais} pontos")
            os.system('cls')
            
            if selecao_de_dificuldade == 1:
                selecao_de_perguntas = random.randint(1, 10) # variavel pra escolher a pergunta
                prevencao_de_pergunta_ingual_facil = []
                while True:
                    if selecao_de_perguntas in prevencao_de_pergunta_ingual_facil:
                        selecao_de_perguntas = random.randint(1, 10)
                    else:
                        prevencao_de_pergunta_ingual_facil.append(selecao_de_perguntas)
                        break
                contar_vetor = len(prevencao_de_pergunta_ingual_facil)
                if contar_vetor == 10:
                    prevencao_de_pergunta_ingual_facil.clear()
            elif  selecao_de_dificuldade == 2:
                selecao_de_perguntas = random.randint(1, 15) # variavel pra escolher a pergunta
                prevencao_de_pergunta_ingual_medio = []
                while True:
                    if selecao_de_perguntas in prevencao_de_pergunta_ingual_medio:
                        selecao_de_perguntas = random.randint(1, 15)
                    else:
                        prevencao_de_pergunta_ingual_medio.append(selecao_de_perguntas)
                        break
                contar_vetor = len(prevencao_de_pergunta_ingual_medio)
                if contar_vetor == 15:
                    prevencao_de_pergunta_ingual_medio.clear()
            elif  selecao_de_dificuldade == 3:
                selecao_de_perguntas = random.randint(1, 15) # variavel pra escolher a pergunta
                prevencao_de_pergunta_ingual_dificil = []
                while True:
                    if selecao_de_perguntas in prevencao_de_pergunta_ingual_dificil:
                        selecao_de_perguntas = random.randint(1, 15)
                    else:
                        prevencao_de_pergunta_ingual_dificil.append(selecao_de_perguntas)
                        break
                contar_vetor = len(prevencao_de_pergunta_ingual_dificil)
                if contar_vetor == 15:
                    prevencao_de_pergunta_ingual_dificil.clear()

            if selecao_de_dificuldade == 1:
                if selecao_de_perguntas == 1:
                    print_bonito(estilo.RESET_ALL+"O que são briofitas?\n")
                    print_bonito(cor.YELLOW+"(1. Plantas não vasculares, como musgos e hepáticas.) \n(2. Plantas vasculares que se reproduzem por esporos, como samambaias.)  \n(3. Plantas vasculares que produzem sementes expostas, como pinheiros.)\n")
                    alternativa_certa = "1"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                    
                elif selecao_de_perguntas == 2:
                    print_bonito(estilo.RESET_ALL+"Quais são os principais exemplos de briofitas?\n")
                    print_bonito(cor.YELLOW+"(1. Samambaias, avencas e licófitas.) \n(2.  Musgos, hepáticas e antóceros.)  \n(3. Coníferas, cicadófitas e ginkgo.)\n")
                    alternativa_certa = "2"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 3:
                    print_bonito(estilo.RESET_ALL+"Como as gimnospermas se reproduzem?\n")
                    print_bonito(cor.YELLOW+"(1. Através de sementes formadas em cones.) \n(2. Através da polinização e formação de frutos.)  \n(3. Por meio de esporos produzidos em esporângios.)\n")
                    alternativa_certa = "1"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 4:
                    print_bonito(estilo.RESET_ALL+"As briofitas possuem raízes verdadeiras?\n")
                    print_bonito(cor.YELLOW+"(1. Sim, possuem raízes verdadeiras que ajudam na absorção de água e nutrientes.) \n(2. Não, pois ela não precisa de nutrientes)  \n(3. Não, elas têm estruturas chamadas rizóides que não absorvem água como raízes verdadeiras.)\n")
                    alternativa_certa = "3"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 5:
                    print_bonito(estilo.RESET_ALL+"Qual é o papel das flores nas angiospermas?\n")
                    print_bonito(cor.YELLOW+"(1. Para armazenar água da chuva e fazer fotossíntese) \n(2. Para criar frutos)  \n(3. Atraem polinizadores e facilitam a reprodução.)\n")
                    alternativa_certa = "3"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 6:
                    print_bonito(estilo.RESET_ALL+"O que são angiospermas?\n")
                    print_bonito(cor.YELLOW+"(1. Organismos unicelulares que habitam ambientes aquáticos.) \n(2. Vegetais que não possuem flores e frutos.)  \n(3. Plantas vasculares que produzem sementes nuas.)\n")
                    alternativa_certa = "3"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 7:
                    print_bonito(estilo.RESET_ALL+"Como as angiospermas se reproduzem?\n")
                    print_bonito(cor.YELLOW+"(1. Exclusivamente por reprodução assexuada.) \n(2. Através da polinização e formação de frutos.)  \n(3. Por meio de esporos, como os fetos.)\n")
                    alternativa_certa = "2"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 8:
                    print_bonito(estilo.RESET_ALL+"O que é a polinização e por que é importante para as angiospermas?\n")
                    print_bonito(cor.YELLOW+"(1. Transferência de pólen de uma flor para outra, essencial para a reprodução.) \n(2. É a produção de hormônios vegetais que regulam o crescimento.)  \n(3. É o processo de formação do solo a partir da decomposição de matéria orgânica.)\n")
                    alternativa_certa = "1"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 9:
                    print_bonito(estilo.RESET_ALL+"Quais são os principais exemplos de pteridófitas?\n")
                    print_bonito(cor.YELLOW+"(1. Coníferas, cicadófitas e ginkgo.) \n(2. Samambaias, avencas e licófitas.)  \n(3. Musgos, hepáticas e antóceros.)\n")
                    alternativa_certa = "2"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 10:
                    print_bonito(estilo.RESET_ALL+"As pteridófitas têm raízes verdadeiras?\n")
                    print_bonito(cor.YELLOW+"(1. Sim, possuem raízes verdadeiras que ajudam na absorção de água e nutrientes.) \n(2. Sim, mas suas raízes são muito pequenas e não absorvem água.)  \n(3. Não, possuem rizóides que não possuem vasos condutores.)\n")
                    alternativa_certa = "1"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                
            elif  selecao_de_dificuldade == 2:
                if selecao_de_perguntas == 1:
                    print_bonito(estilo.RESET_ALL+"Qual é a fase dominante do ciclo de vida das briofitas?\n")
                    print_bonito(cor.YELLOW+"(1. s briófitas não possuem ciclo de vida definido.)\n(2. A fase gametofítica.)\n(3. As fases esporofítica e gametofítica têm a mesma duração.)\n(4. A fase esporofítica.)\n")
                    alternativa_certa = "2"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 2:
                    print_bonito(estilo.RESET_ALL+"Como as briófitas se reproduzem?\n")
                    print_bonito(cor.YELLOW+"(1. Por meio de esporos e reprodução sexual.)\n(2. As briófitas não se reproduzem.)\n(3. Apenas por reprodução assexuada, através de fragmentação.)\n(4. Exclusivamente por meio de sementes.)\n")
                    alternativa_certa = "1"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 3:
                    print_bonito(estilo.RESET_ALL+"Quais são os principais papéis ecológicos das briófitas?\n")
                    print_bonito(cor.YELLOW+"(1. Contribuem para a formação do solo e a retenção de umidade.)\n(2. Não possuem papel ecológico relevante.)\n(3. São a base da cadeia alimentar em todos os ecossistemas.)\n(4.  São os principais produtores de oxigênio nos ecossistemas terrestres.)\n")
                    alternativa_certa = "1"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 4:
                    print_bonito(estilo.RESET_ALL+"O que são esporângios e onde estão localizados nas pteridófitas?\n")
                    print_bonito(cor.YELLOW+"(1. Partes da planta responsáveis pela fotossíntese.)\n(2. Estruturas que absorvem água e nutrientes do solo.)\n(3. Órgãos reprodutivos masculinos, responsáveis pela produção de gametas.)\n(4. Estruturas que produzem esporos, localizadas geralmente na parte inferior das frondes.)\n")
                    alternativa_certa = "4"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 5:
                    print_bonito(estilo.RESET_ALL+"Quais habitats são favoráveis ao crescimento de pteridófitas?\n")
                    print_bonito(cor.YELLOW+"(1. As pteridófitas podem crescer em qualquer tipo de ambiente.)\n(2. Solos salinos e com pouca disponibilidade de água)\n(3. Ambientes úmidos, sombreados e ricos em matéria orgânica.)\n(4. Desertos e regiões áridas, com alta incidência solar.)\n")
                    alternativa_certa = "3"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 6:
                    print_bonito(estilo.RESET_ALL+"Como as pteridófitas contribuem para a biodiversidade?\n")
                    print_bonito(cor.YELLOW+"(1. São a base da cadeia alimentar em todos os ecossistemas.)\n(2. Não possuem papel relevante na manutenção da biodiversidade.)\n(3. São os principais produtores de oxigênio nos ecossistemas terrestres.)\n(4. Fornecem habitat e alimento para diversos organismos.)\n")
                    alternativa_certa = "4"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 7:
                    print_bonito(estilo.RESET_ALL+"Quais são as principais adaptações das pteridófitas?\n")
                    print_bonito(cor.YELLOW+"(1. Raízes profundas para buscar água em locais secos.)\n(2. As pteridófitas não possuem adaptações específicas.)\n(3. Folhas grandes para maximizar a fotossíntese e estruturas que retêm água.)\n(4. Raízes profundas para buscar água em locais secos.)\n")
                    alternativa_certa = "3"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 8:
                    print_bonito(estilo.RESET_ALL+"Qual é a diferença entre gimnospermas e angiospermas?\n")
                    print_bonito(cor.YELLOW+"(1. Gimnospermas são plantas herbáceas, enquanto angiospermas são arbustivas ou arbóreas.)\n(2. Gimnospermas têm sementes expostas; angiospermas têm sementes encerradas em frutos.)\n(3. Gimnospermas produzem flores vistosas, enquanto angiospermas não)\n(4. Gimnospermas não possuem vasos condutores de seiva, enquanto angiospermas possuem.)\n")
                    alternativa_certa = "2"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 9:
                    print_bonito(estilo.RESET_ALL+"Como as angiospermas contribuem para a biodiversidade?\n")
                    print_bonito(cor.YELLOW+"(1. Fornecem habitat e alimento para muitos organismos.)\n(2. Não possuem papel relevante no ecossistema.)\n(3. Aumentam a acidez do solo, prejudicando outros organismos.)\n(4. Causam a extinção de outras plantas.)\n")
                    alternativa_certa = "1"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 10:
                    print_bonito(estilo.RESET_ALL+"Quais ambientes são favoráveis ao crescimento de gimnospermas?\n")
                    print_bonito(cor.YELLOW+"(1. Regiões tropicais com alta umidade.)\n(2. Desertos extremamente secos e quentes.)\n(3. Ambientes aquáticos, como rios e lagos.)\n(4. Climas temperados e frios, muitas vezes em solos pobres.)\n")
                    alternativa_certa = "4"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 11:
                    print_bonito(estilo.RESET_ALL+"Como as gimnospermas influenciam o ecossistema?\n")
                    print_bonito(cor.YELLOW+"(1. Fornecem madeira, abrigo e alimento para várias espécies.)\n(2. Aumentam a acidez do solo, prejudicando outros organismos.)\n(3. São responsáveis pelo efeito estufa.)\n(4. Não possuem papel relevante no ecossistema.)\n")
                    alternativa_certa = "1"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 12:
                    print_bonito(estilo.RESET_ALL+"Quais são as utilidades econômicas das gimnospermas?\n")
                    print_bonito(cor.YELLOW+"(1. Utilizadas como matéria-prima para a produção de plásticos.)\n(2. Usadas para madeira, papel, resinas e ornamentação)\n(3. Não possuem valor econômico.)\n(4. Utilizadas exclusivamente como fonte de alimento.)\n")
                    alternativa_certa = "2"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 13:
                    print_bonito(estilo.RESET_ALL+"Quais são os diferentes tipos de frutos nas angiospermas?\n")
                    print_bonito(cor.YELLOW+"(1. Frutos doces, azedos, salgados e amargos.)\n(2. Frutos secos, carnosos, simples e compostos.)\n(3. Frutos comestíveis e não comestíveis.)\n(4. Frutos grandes, médios e pequenos.)\n")
                    alternativa_certa = "2"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 14:
                    print_bonito(estilo.RESET_ALL+"Qual é a importância das angiospermas para a alimentação humana?\n")
                    print_bonito(cor.YELLOW+"(1. Única fonte de vitamina C para os humanos.)\n(2. Fonte primária de frutas, vegetais e grãos.)\n(3. Importante apenas para a indústria farmacêutica.)\n(4. Principal fonte de proteínas para a dieta humana.)\n")
                    alternativa_certa = "2"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 15:
                    print_bonito(estilo.RESET_ALL+"Como as angiospermas interagem com polinizadores?\n")
                    print_bonito(cor.YELLOW+"(1. Dependem de insetos, aves e vento para a polinização.)\n(2. Repelam os polinizadores através de substâncias químicas.)\n(3. A polinização ocorre exclusivamente pela água.)\n(4. Atraem polinizadores apenas através da cor de suas flores.)\n")
                    alternativa_certa = ""
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                
            elif selecao_de_dificuldade == 3:
                if selecao_de_perguntas == 1:
                    print_bonito(estilo.RESET_ALL+"O que são esporos e como as briófitas os produzem?\n")
                    print_bonito(cor.YELLOW+"(1. Esporos são sementes adaptadas para a dispersão em ambientes secos.)\n(2. Esporos são células haploides que se desenvolvem em gametófitos independentes e de vida longa.)\n(3. Esporos são estruturas vegetativas que se desenvolvem em novas plantas.)\n(4. Esporos são gametas haploides produzidos por mitose em estruturas especializadas chamadas arquegônios.)\n(5. Esporos são células reprodutivas que se desenvolvem em esporângios.)\n")
                    alternativa_certa = "5"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 2:
                    print_bonito(estilo.RESET_ALL+"Como as briofitas se relacionam com outros organismos, como fungos?\n")
                    print_bonito(cor.YELLOW+"(1. )\n(2. Formam associações simbióticas que ajudam na absorção de nutrientes.)\n(3. As briófitas são decompositoras de fungos, auxiliando na ciclagem de nutrientes no ecossistema.)\n(4. As briófitas e os fungos não estabelecem nenhum tipo de relação ecológica.)\n(5. As briófitas e os fungos competem pelos mesmos recursos no ambiente.)\n")
                    alternativa_certa = "2"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 3:
                    print_bonito(estilo.RESET_ALL+"Quais são as adaptações das briófitas a ambientes úmidos?\n")
                    print_bonito(cor.YELLOW+"(1. Frutos carnosos para dispersão das sementes por animais, caule lenhoso para sustentação e raízes aéreas para absorver umidade do ar.)\n(2. Raízes profundas para absorver água do solo, cutícula espessa para evitar a perda de água e estômatos para realizar trocas gasosas.)\n(3. Folhas largas para aumentar a área de absorção de luz, sementes dispersas pelo vento e flores coloridas para atrair polinizadores.)\n(4. Rizoides para fixação, ausência de vasos condutores, gametângios protegidos por uma camada de células estéreis e capacidade de fotossíntese em qualquer parte da planta.)\n(5. )\n")
                    alternativa_certa = "4"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 4:
                    print_bonito(estilo.RESET_ALL+"Qual é a importância das briofitas na medicina?\n")
                    print_bonito(cor.YELLOW+"(1. As briófitas são a principal fonte de medicamentos para doenças cardíacas e câncer.)\n(2. As briófitas são utilizadas na produção de biocombustíveis, como o etanol.)\n(3. Algumas são usadas em remédios tradicionais e para fins farmacêuticos)\n(4. As briófitas são a base da cadeia alimentar em todos os ecossistemas terrestres.)\n(5. As briófitas são utilizadas como fertilizantes naturais, aumentando a produtividade agrícola.)\n")
                    alternativa_certa = "3"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 5:
                    print_bonito(estilo.RESET_ALL+"Como as pteridófitas se reproduzem assexuadamente?\n")
                    print_bonito(cor.YELLOW+"(1. Por meio de fragmentação ou rizomas.)\n(2. Exclusivamente por esporos, produzidos em estruturas especializadas chamadas soros.)\n(3. Por meio de propagação por estacas, similarmente às plantas com flores.)\n(4. Através de partenogênese, onde óvulos se desenvolvem em novos indivíduos sem fecundação.)\n(5. Através de sementes dispersas pelo vento ou por animais.)\n")
                    alternativa_certa = "1"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 6:
                    print_bonito(estilo.RESET_ALL+"Como as pteridófitas lidam com a desidratação?\n")
                    print_bonito(cor.YELLOW+"(1. Perdem suas folhas durante a estação seca, entrando em dormência.)\n(2. Realizam fotossíntese CAM, um mecanismo adaptativo para economizar água.)\n(3. Armazenam grandes quantidades de água em seus tecidos, semelhante às plantas suculentas.)\n(4. Possuem raízes profundas que alcançam lençóis freáticos, garantindo o suprimento hídrico.)\n(5. Muitas possuem mecanismos para minimizar a perda de água, como cutícula espessa, estômatos em depressões e folhas reduzidas.)\n")
                    alternativa_certa = "5"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 7:
                    print_bonito(estilo.RESET_ALL+"O que são sifonófitas e como se relacionam com as pteridófitas?\n")
                    print_bonito(cor.YELLOW+"(1. Um grupo de animais que se alimentam de pteridófitas.)\n(2. Fungos que formam associações mutualísticas com as raízes das pteridófitas.)\n(3. Um grupo de algas que deu origem às primeiras plantas terrestres, incluindo as pteridófitas.)\n(4. Organismos relacionados que também têm características vasculares, mas são mais simples.)\n(5. Um grupo de plantas com flores que evoluiu a partir das pteridófitas.)\n")
                    alternativa_certa = "4"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 8:
                    print_bonito(estilo.RESET_ALL+"Como as gimnospermas lidam com pragas e doenças?\n")
                    print_bonito(cor.YELLOW+"(1. A reprodução rápida e abundante das gimnospermas garante a sobrevivência da espécie, mesmo com altas taxas de mortalidade por doenças.)\n(2. As gimnospermas possuem um sistema imunológico complexo que permite a produção de anticorpos contra patógenos.)\n(3. Desenvolvem resinas e compostos químicos como defesa.)\n(4. As gimnospermas eliminam substâncias voláteis que atraem predadores naturais das pragas.)\n(5. Através de relações mutualísticas com outros organismos, como bactérias e fungos, as gimnospermas obtêm proteção contra patógenos.)\n")
                    alternativa_certa = "3"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 9:
                    print_bonito(estilo.RESET_ALL+"O que são resinas e qual a sua importância nas gimnospermas?\n")
                    print_bonito(cor.YELLOW+"(1. As resinas são utilizadas pelas gimnospermas para atrair polinizadores.)\n(2. Substâncias produzidas como defesa contra patógenos e pragas.)\n(3. As resinas não possuem função ecológica importante para as gimnospermas.)\n(4. As resinas são produzidas exclusivamente pelas raízes das gimnospermas.)\n(5. As resinas são utilizadas pelas gimnospermas para armazenar água e nutrientes.)\n")
                    alternativa_certa = "2"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 10:
                    print_bonito(estilo.RESET_ALL+"Como as angiospermas se adaptam a diferentes ambientes?\n")
                    print_bonito(cor.YELLOW+"(1. Desenvolvem várias morfologias e estratégias de crescimento.)\n(2. As angiospermas estabelecem relações simbióticas com outros organismos, como fungos e bactérias, o que facilita sua adaptação a diferentes ambientes.)\n(3. As angiospermas possuem um crescimento indeterminado, o que permite que se adaptem a qualquer tipo de ambiente.)\n(4. Através de mutações genéticas aleatórias, as angiospermas adquirem rapidamente as adaptações necessárias para sobreviver em novos ambientes.)\n(5. As angiospermas não possuem mecanismos de adaptação, sendo encontradas apenas em ambientes específicos.)\n")
                    alternativa_certa = "1"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 11:
                    print_bonito(estilo.RESET_ALL+"Qual é o ciclo de vida das angiospermas?\n")
                    print_bonito(cor.YELLOW+"(1. Ciclo de vida semelhante ao das briófitas, com a fase gametofítica dominante.)\n(2. Ciclo de vida direto, sem alternância de gerações.)\n(3. Ciclo de vida haplonte, com a fase gametofítica sendo a fase dominante.)\n(4. Ciclo de vida haplodiplonte, com fases esporofítica e gametofítica independentes e de mesma duração.)\n(5. Alternância de gerações, com predominância da fase esporofítica.)\n")
                    alternativa_certa = "5"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 12:
                    print_bonito(estilo.RESET_ALL+"Como as angiospermas ajudam na conservação do solo?\n")
                    print_bonito(cor.YELLOW+"(1. As angiospermas são a principal causa da desertificação.)\n(2. As angiospermas contribuem para a compactação do solo, dificultando a infiltração da água.)\n(3. As angiospermas competem com outras plantas por nutrientes, esgotando o solo.)\n(4. Suas raízes previnem a erosão, mantêm a umidade do solo e contribuem para a formação do húmus, melhorando a fertilidade do solo.)\n(5. As angiospermas liberam substâncias tóxicas no solo, impedindo o crescimento de outras plantas e causando a erosão.)\n")
                    alternativa_certa = "4"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 13:
                    print_bonito(estilo.RESET_ALL+"Quais são as características que distinguem angiospermas de gimnospermas?\n")
                    print_bonito(cor.YELLOW+"(1. As angiospermas não possuem raízes, enquanto as gimnospermas possuem raízes profundas.)\n(2. As angiospermas são plantas herbáceas, enquanto as gimnospermas são arbustivas ou arbóreas.)\n(3. Presença de flores e frutos, dupla fecundação, vasos condutores mais eficientes e sementes encerradas em frutos nas angiospermas.)\n(4. As gimnospermas não possuem sementes, enquanto as angiospermas possuem sementes nuas.)\n(5. As gimnospermas possuem flores mais vistosas e coloridas que as angiospermas.)\n")
                    alternativa_certa = "3"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 14:
                    print_bonito(estilo.RESET_ALL+"Como as angiospermas influenciam a economia global?\n")
                    print_bonito(cor.YELLOW+"(1. As angiospermas são a principal fonte de madeira para a construção civil.)\n(2. São fundamentais para a agricultura, indústria e medicina.)\n(3. As angiospermas são utilizadas apenas na produção de papel.)\n(4. As angiospermas não possuem valor econômico.)\n(5. As angiospermas são utilizadas exclusivamente como plantas ornamentais.)\n")
                    alternativa_certa = "2"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                elif selecao_de_perguntas == 15:
                    print_bonito(estilo.RESET_ALL+"Qual a importância da coevolução entre angiospermas e animais polinizadores?\n")
                    print_bonito(cor.YELLOW+"(1. A coevolução entre angiospermas e animais polinizadores levou ao desenvolvimento de diversas adaptações, como flores coloridas e perfumadas, néctar e frutos, beneficiando ambas as partes.)\n(2. Os animais polinizadores não se beneficiam da relação com as angiospermas, pois possuem outras fontes de alimento.)\n(3. As angiospermas não dependem de animais para a polinização, sendo capazes de se auto-polinizar.)\n(4. Os polinizadores prejudicam as angiospermas, consumindo o néctar e o pólen sem realizar a polinização.)\n(5. A relação entre angiospermas e polinizadores é puramente acidental, sem benefícios para nenhuma das partes.)\n")
                    alternativa_certa = "1"
                    alternativa_pergunta_slafodase(alternativa_certa, jogador, pontos_totais)
                
                
            print_bonito(f"O jogador {jogador['nome']} possui {jogador['pontuacao']}\n")
            input("Pressione Enter para continuar")
            os.system('cls')
        for jogador in jogadores_participando:
            print(f"Pontuação de {jogador['cor']+jogador['nome']}: {jogador['pontuacao']}")
            if rodadas == 1:
                os.system('cls')
                jogadores_participando.sort(key=lambda x: x['pontuacao'], reverse=True)
                jogador_vencedor = jogadores_participando[0]
                print_bonito(f"Parabéns {jogador_vencedor['cor']+jogador_vencedor['nome'] + estilo.RESET_ALL}! \nVocê venceu o jogo com {jogador_vencedor['pontuacao']} pontos!\n\n")
                print_bonito("Pontuação final:\n")
                print(f"Pontuação de {jogador_vencedor['cor']+jogador['nome']}: {jogador['pontuacao']}")
                gameplay = 0
        rodadas += 1
        input()