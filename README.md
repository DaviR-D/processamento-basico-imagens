### 1. `binarizacao.py`
**Função:** Converte uma imagem em tons de cinza em uma imagem binária.

- **Processo:**
  1. Carrega uma imagem em tons de cinza (`imagem_cinza.jpg`).
  2. Cria uma nova imagem binária.
  3. Itera por cada pixel da imagem em tons de cinza.
  4. Se o valor do pixel for maior ou igual ao limiar (100), define o pixel correspondente na imagem binária como 1 (branco); caso contrário, define como 0 (preto).
  5. Exibe a imagem binária.

### 2. `media.py`
**Função:** Aplica um filtro de média em uma imagem em tons de cinza.

- **Processo:**
  1. Carrega uma imagem em tons de cinza (`imagem_cinza.jpg`).
  2. Cria uma nova imagem para o resultado filtrado pela média.
  3. Para cada pixel na imagem em tons de cinza (excluindo os pixels das bordas), calcula o valor médio do pixel e seus 8 vizinhos.
  4. Define o valor médio calculado para o pixel correspondente na nova imagem.
  5. Exibe a imagem filtrada pela média.

### 3. `mediana.py`
**Função:** Aplica um filtro de mediana em uma imagem em tons de cinza.

- **Processo:**
  1. Carrega uma imagem em tons de cinza (`imagem_cinza.jpg`).
  2. Cria uma nova imagem para o resultado filtrado pela mediana.
  3. Para cada pixel na imagem em tons de cinza (excluindo os pixels das bordas), coleta os valores dos pixels do pixel central e seus 8 vizinhos.
  4. Ordena os valores coletados e seleciona o valor mediano.
  5. Define o valor mediano para o pixel correspondente na nova imagem.
  6. Exibe a imagem filtrada pela mediana.

### 4. `separacao_canais.py`
**Função:** Separa os canais vermelho, verde e azul de uma imagem e cria três novas imagens, cada uma representando um canal de cor em tons de cinza.

- **Processo:**
  1. Carrega uma imagem (`imagem.jpg`).
  2. Cria três novas imagens para os canais vermelho, verde e azul.
  3. Para cada pixel na imagem, extrai os valores vermelho, verde e azul.
  4. Define o pixel correspondente em cada uma das três novas imagens com o valor respectivo da cor.
  5. Exibe as três imagens com os canais separados.

### 5. `tons_de_cinza.py`
**Função:** Converte uma imagem colorida em uma imagem em tons de cinza.

- **Processo:**
  1. Carrega uma imagem (`imagem.jpg`).
  2. Cria uma nova imagem em tons de cinza.
  3. Para cada pixel na imagem, calcula o valor em tons de cinza usando a fórmula: `gray_value = 0.299 * R + 0.587 * G + 0.114 * B`.
  4. Define o valor em tons de cinza calculado para o pixel correspondente na nova imagem.
  5. Exibe a imagem em tons de cinza.

### 6. `girar_90.py`
**Função:** Gira uma imagem 90 graus no sentido horário.

- **Processo:**
  1. Carrega uma imagem (`imagem.jpg`).
  2. Cria uma nova imagem com dimensões de largura e altura trocadas.
  3. Para cada pixel na imagem original, define o pixel correspondente na nova imagem na posição correta girada.
  4. Exibe a imagem girada.

### 7. `inverter_horizontal.py`
**Função:** Inverte uma imagem horizontalmente.

- **Processo:**
  1. Carrega uma imagem (`imagem.jpg`).
  2. Cria uma nova imagem do mesmo tamanho.
  3. Para cada pixel na imagem original, define o pixel correspondente na nova imagem na posição invertida horizontalmente.
  4. Exibe a imagem invertida horizontalmente.

### 8. `inverter_vertical.py`
**Função:** Inverte uma imagem verticalmente.

- **Processo:**
  1. Carrega uma imagem (`imagem.jpg`).
  2. Cria uma nova imagem do mesmo tamanho.
  3. Para cada pixel na imagem original, define o pixel correspondente na nova imagem na posição invertida verticalmente.
  4. Exibe a imagem invertida verticalmente.
