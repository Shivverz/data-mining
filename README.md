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

![Modo de Trabalho](https://github.com/Shivverz/data-mining/raw/main/imgs/WorkMode.png)



## Trabalho futuro
Como possíveis melhorias ao nosso trabalho no futuro temos:
  - Integração de dados de outras fontes, de modo a tornar o LLM mais robusto.
  - Integração de histórico na interface.
  - Atualização de dados automática.
  - Integração de pedidos automáticos à plataforma, mediante a query, ao invés de manter os dados armazenados localmente.

Link Para apresentação: https://www.canva.com/design/DAGBRTKA3yA/iDEKjXOwCy31-Iw2Wih_3g/edit?utm_content=DAGBRTKA3yA&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
