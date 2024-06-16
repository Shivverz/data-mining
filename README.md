# data-mining
Este repositório contém o material relativo à construção do trabalho prático da unidade curricular de Data Mining, inserida no primeiro ano do Mestrado em Engenharia Informática.

Realizado por :
  - **Alexandre Fernandes- PG53606**
  - **Henrique Fernandes- A95323**
  - **Hugo Martins- A95125**
  - **João Escudeiro- A96075**


## Conteúdo do repositório
  1. **Files** - Contém os ficheiros txt criados com a informação sobre o campeonato.
  2. **Final_Files** - Contém os ficheiros pdf criados a partir dos ficheiros txt.
  3. **Frontend** - Contém o material utilizado para a construção do Frontend em streamlit.
  4. **MD** - Contém os scripts em GO para a realização dos pedidos API à plataforma.
  5. **Scripts** - Contém os scripts em Python utilizados para converter a informação armazenada no mongoDB para um formato textual.
  6. **Docs** - Contém osficheiros resultantes do armazenamento dos ficheiros na base de dados.
  7. **DataMining-Presentation.pdf** - Apresentação utilizada na apresentação do TP.
  8. **documents.py**- Ficheiro auxiliar para o processamento dos documentos.
  9. **documents_load.py**-Ficheiro auxiliar para o load dos documentos.
  10. **main.py**- Código utilizado para a construção da LLM.
  11. **DataMining_Relatorio.pdf**- Contém o relatório da elaboração do FutProBot, que contém a explicação passo a passo de todas as etapas realizadas até chegar ao produto final.
  12. **/imgs**- Imagens utilizadas para a elaboração do ReadMe


## Objetivos do trabalho prático
Foi-nos proposto a especialização de uma LLM à nossa escolha, num tema do nosso interesse. Assim, e tendo em conta que é um tema que é do nosso interesse, decidimos avançar para a implementação do **FutProBot**, um chat que será especializado em fornecer  comentários com base em estatísticas, classificações, resultados, lineups e a forma recente das equipas. Sempre que for questionado sobre uma equipa, ele será capaz de fornecer estatísticas relevantes, bem como classificações das  ́ultimas temporadas.

## Dados
### Obtenção
Após pesquisarmos sobre várias plataformas, encontramos o Sportmonks, uma plataforma que contém todo o tipo de estatísticas das principais ligas europeias, desde 2005. Entramos em contacto com a plataforma, pelo que nos foi fornecido um token gratuito que permite fazer pedidos ilimitados.

Construimos scripts em GO, que são responsáveis por fazer os pedidos à API e armazenar os dados numa base de dados MongoDBAtlas.

### Tratamento
Após obtermos os dados armazenados numa base de dados em MongoDB, o passo seguinte foi articular os dados em formas textuais, para que o bot fosse capaz de consumir melhor a informação.
Como resultado deste tratamento obtivemos os seguintes ficheiros:


- **Champions - Campeões da Liga Portuguesa**
  - "In the 2000/2001 season the champion was Boavista."

- **Events - Eventos durante um jogo**
  - "The game Vitória SC vs Sporting Braga of the season 2023/2024 at minute 90, Rony Lopes scored a goal for team Sporting Braga."

- **Formations - Esquemas táticos das equipas num jogo**
  - "In the game Sporting CP vs Portimonense of the season 2023/2024 the away team was Portimonense and played in a 4-3-3 formation and the home team was Sporting CP and played in a 3-4-3 formation."

- **Intro - Informação sobre um jogo**
  - "The game between Benfica and Vitória SC of the season 2019/2020 took place in 2020-07-14 and started at 20:30:00 and Benfica won after full-time."

- **Cup Winners - Vencedores da Taça de Portugal**
  - "In the 2005/2006 season, the Portuguese Cup winner was Porto."

- **Referees - Árbitros de um jogo**
  - "The game Benfica vs Arouca of the season 2023/2024 was refereed by Fábio Oliveira Melo, André Filipe Nogueira Dias and António Ricardo de Mesquita Moreira."

- **Seasons - Estatísticas da época**
  - "In Season 2023/2024 the top goalscorer was Viktor Gyökeres with 29 goals."

- **Standings - Classificações finais**
  - "In Season 2019/2020 Porto was champion with 82 points."

- **Statistics - Estatísticas de um jogo**
  - "In game Porto vs Boavista of the season 2023/2024 Boavista have 27 Throw-ins."

- **Teams - Informação sobre os plantéis das equipas**
  - "Marcos Leonardo Santos Almeida, 177.0 tall, is a centre forward for Benfica with the 36 jersey number."


## Modo de Funcionamento
As etapas ultrapassadas para a realização do chat foram:
1. **Carregamento dos Ficheiros de Dados**
2. **Configuração do Divisor do Texto**
3. **Criação dos Embeddings**
4. **Armazenamento dos Ficheiros numa Base de Dados Vetorial**
5. **Integração com o Modelo**
6. **Criação do FrontEnd**

Na figura abaixo é apresentado de uma forma simplificada o modo de funcionamento do chat.

![Modo de Trabalho](https://github.com/Shivverz/data-mining/raw/main/imgs/WorkMode.png)

### Exemplo prático com perguntas
Na figura abaixo está representado o front-end desenvolvido, incorporado com as respostas do ChatBot. 
![FrontEnd](https://github.com/Shivverz/data-mining/blob/main/imgs/frontend.png)

## Análise de desempenho
Decidimos realizar algumas perguntas e observar as respostas, de modo a analisar o desempenho do ChatBot
| **Pergunta** | **Resposta** | **Observação** |
|--------------|--------------|----------------|
| What was the most used formation by Sporting in the 2023/2024 season? | In the 2023/2024 season, Sporting CP played in two different formations: a 3-4-3 and a 3-5-2 formation. However, it appears that they used the 3-4-3 formation more frequently as it was their choice against Rio Ave and Sporting Braga at home. The exact number of games played in each formation is not specified in the provided data, but based on the matches mentioned, it can be inferred that the 3-4-3 formation was used more often by Sporting CP during this season. | Resposta Certa |
| Who was the champion for the 2023/2024 season? | The champion of the 2023/2024 season was Sporting CP, as they finished with a total of 87 points. This achievement marked their success in that particular season, surpassing other teams such as Benfica (second place with 79 points) and Porto (third place with 69 points). The remaining top five teams were Sporting Braga (fourth place with 68 points), Vitória SC (fifth place with 60 points), Moreirense (sixth place with 52 points), Arouca (seventh place with 46 points), Famalicão (eighth place with 42 points), Farense (ninth place with 37 points), Gil Vicente (tenth place with 36 points), Rio Ave (eleventh place with 36 points), Casa Pia (twelfth place with 35 points), Estoril (thirteenth place with 33 points), Boavista (fourteenth place with 31 points), Estrela Amadora (fifteenth place with 30 points), Portimonense (sixteenth place with 29 points), Vizela (penultimate place with 25 points), and Chaves (last place with 23 points). | Resposta correta (os dados foram retirados no fim da penúltima jornada) |
| Can you give me the league standings for the 2022/2023 season? | In the 2022/2023 season, the Portuguese Primeira Liga standings were as follows: 1. Benfica - 87 points; 2. Porto - 85 points; 3. Sporting Braga - 78 points; 4. Sporting CP - 74 points; 5. Arouca - 54 points; 6. Vitória SC - 53 points; 7. Chaves - 46 points; 8. Boavista - 44 points; 9. Famalicão - 44 points; 10. Casa Pia - 41 points; 11. Rio Ave - 40 points; 12. Vizela - 40 points; 13. Gil Vicente - 37 points; 14. Estoril - 35 points; 15. Portimonense - 34 points; 16. Marítimo - 26 points; 17. Paços de Ferreira - 23 points; 18. Santa Clara - 22 points; 19. Belenenses - Not available (they were last in the previous season with 26 points); | Resposta parcialmente correta, erro na inclusão do Belenenses, que está a mais |
| Who is the team with the most cup wins? | The team with the most Portuguese Cup wins, based on the data provided for seasons up to 1989/1990 and from Season 2023/2024, is Benfica. They have won the Portuguese Cup a total of 10 times: in the 1969/1970, 1970/1971, 1971/1972, 1980/1981, 1981/1982, 1984/1985, 1985/1986, 1986/1987, and twice in the 2023/2024 season. Porto follows closely with 7 victories: in the 1967/1968, 1976/1977, 1988/1989, 1990/1991, 1991/1992, and twice in the 2023/2024 season. Sporting has won the Portuguese Cup 5 times: in the 1973/1974, 1977/1978, 1982/1983, and twice in the 2023/2024 season. Boavista has also won the cup twice, in the 1974/1975 and 1992/1993 seasons. | Resposta errada|


## Trabalho futuro
Como possíveis melhorias ao nosso trabalho no futuro temos:
  - Integração de dados de outras fontes, de modo a tornar o LLM mais robusto.
  - Integração de histórico na interface.
  - Atualização de dados automática.
  - Integração de pedidos automáticos à plataforma, mediante a query, ao invés de manter os dados armazenados localmente.

Link Para apresentação: https://www.canva.com/design/DAGBRTKA3yA/iDEKjXOwCy31-Iw2Wih_3g/edit?utm_content=DAGBRTKA3yA&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
