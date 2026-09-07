# 📚 Enciclopédia Canônica dos 24 Estilos de Design de Páginas

Este documento é a referência canônica completa de direção de arte, história, atributos formais, tokens de design e aplicações práticas dos 24 estilos de design de páginas.

---

## 🏛️ Família 1: Movimentos Históricos & Vanguardas (1890 – 1980)

### 1. Bauhaus & Modernismo Funcional (1919–1933)
* **Origem Histórica**: Escola fundada por Walter Gropius em Weimar/Dessau.
* **Filosofia**: A forma segue rigorosamente a função. Destruição do ornamento burguês superficial. A arte e a tecnologia fundidas em produção utilitária em massa.
* **Atributos Formais**:
  - Geometria elementar: círculo perfeito, triângulo equilátero, quadrado.
  - Paleta estrita: Vermelho primário (`#D92525`), Amarelo primário (`#F2B705`), Azul cobalto (`#0D47A1`), Preto puro (`#000000`) e Branco (`#FFFFFF`).
  - Sem sombras, sem gradientes, sem cantos arredondados (`border-radius: 0px`).
* **Tipografia**: Fontes sem serifa puramente geométricas (Futura, Archivo Black, Bayer Universal). Títulos com grande peso e entrelinha justa.
* **Exemplo de Tokens**:
  ```css
  --color-primary: #d92525;
  --color-secondary: #0d47a1;
  --color-accent: #f2b705;
  --color-surface: #ffffff;
  --color-text: #000000;
  --border-width: 3px;
  --radius: 0px;
  --font-display: 'Futura', 'Archivo Black', sans-serif;
  ```

### 2. Swiss Style / Estilo Tipográfico Internacional (1950s)
* **Origem Histórica**: Suíça (Zurique e Basileia), liderada por Josef Müller-Brockmann, Armin Hofmann e Emil Ruder.
* **Filosofia**: Apresentação visual clara, objetiva e universal da informação. O designer atua como mediador invisível do conteúdo.
* **Atributos Formais**:
  - Grid modular estrito (12 ou 16 colunas) matematicamente calibrado.
  - Assimetria lógica: o alinhamento é estritamente à esquerda com margem direita não justificada (*ragged right*).
  - Espaços em branco generosos tratados como elemento arquitetural ativo.
  - Fotografia documental monocromática de alto contraste em vez de ilustrações.
* **Tipografia**: Grotescas puras e neutras (Neue Haas Grotesk, Helvetica, Akzidenz-Grotesk, Univers).
* **Exemplo de Tokens**:
  ```css
  --color-bg: #f4f4f4;
  --color-text: #111111;
  --color-accent: #ff3b30;
  --grid-columns: 12;
  --gutter: 24px;
  --radius: 0px;
  --font-sans: 'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif;
  ```

### 3. De Stijl / Neoplasticismo (1917–1931)
* **Origem Histórica**: Holanda, fundado por Theo van Doesburg e imortalizado pelas pinturas de Piet Mondrian.
* **Filosofia**: Expressão de uma nova harmonia espiritual universal através da abstração radical e da redução às leis primárias da geometria.
* **Atributos Formais**:
  - Apenas linhas ortogonais pretas (horizontais e verticais) com espessura marcante (3px a 6px).
  - Blocos retangulares preenchidos com cores primárias saturadas e não-cores (branco, cinza claro e preto).
  - Ausência total de curvas, diagonais, sombras e texturas.
* **Tipografia**: Tipografia sem serifa em caixas de texto com contornos rígidos.

### 4. Art Déco (1920s–1930s)
* **Origem Histórica**: Paris (Exposition Internationale des Arts Décoratifs et Industriels Modernes, 1925).
* **Filosofia**: O glamour do progresso tecnológico, velocidade, riqueza industrial e luxo moderno da Era do Jazz.
* **Atributos Formais**:
  - Simetria bilateral exata e ornamentações geométricas refinadas.
  - Formas escalonadas (zigurates), leques, raios de sol e arcos metálicos.
  - Paleta: Dourado polido (`#D4AF37`), bronze, preto ébano (`#0A0A0A`) e azul petróleo.
* **Tipografia**: Fontes display decorativas com hastes alongadas, cintura alta e linhas finas elegantes (Poiret One, Broadway, Park Lane).

### 5. Art Nouveau & Arts and Crafts (1890–1914)
* **Origem Histórica**: Europa (França, Bélgica, Inglaterra com William Morris e Alphonse Mucha).
* **Filosofia**: Resistência humanista e estética contra a desumanização e a frieza da Revolução Industrial mecânica.
* **Atributos Formais**:
  - Linhas curvas dinâmicas e fluidas inspiradas na flora (videiras, folhas, caules, ondas).
  - Molduras ilustradas à mão com bordas orgânicas e detalhes botânicos.
  - Paleta terrosa: verde-oliva, terracota, mostarda suave, papel envelhecido e ouro fosco.
* **Tipografia**: Serifas expressivas com ligaduras caligráficas complexas e detalhes florais.

### 6. Memphis Design (1981–1987)
* **Origem Histórica**: Milão, fundado por Ettore Sottsass e o grupo Memphis.
* **Filosofia**: Reação divertida e iconoclasta contra o minimalismo austero e o funcionalismo modernista rígido.
* **Atributos Formais**:
  - Padrões de ziguezague (*squiggles*), bolinhas espalhadas, listras diagonais e triângulos flutuantes.
  - Paleta pós-moderna: combinação intencionalmente berrante de cores pastel com toques neon (rosa choque, amarelo canário, turquesa, menta).
  - Assimetria dinâmica, formas assimétricas e bom humor visual.
* **Tipografia**: Tipografia descontraída, display com traços grossos e alegres.

---

## 💾 Família 2: A Era Digital Inicial & Nostalgia Retrô (1980 – 2012)

### 7. Retro-Computing / 8-bit & 16-bit
* **Origem**: Início da computação pessoal e consoles clássicos (Commodore 64, NES, Game Boy, Apple II).
* **Filosofia**: Poética das limitações de memória e resolução gráfica do início da era dos microprocessadores.
* **Atributos Formais**:
  - Resolução intencionalmente pixelada, paletas indexadas reduzidas (CGA de 4 cores, EGA de 16 cores).
  - Linhas de varredura CRT sutis (*scanlines*) e leve distorção de tubo de raios catódicos.
  - Janelas com barras chanfradas estilo Windows 95 ou Mac OS System 7.
* **Tipografia**: Fontes bitmap e pixeladas (Press Start 2P, Silkscreen, VT323).

### 8. CLI / Terminal / Text-based UI (TUI)
* **Origem**: Terminais VT100 e sistemas operacionais orientados a texto (UNIX, DOS).
* **Filosofia**: Eficiência máxima, eliminação de intermediários gráficos e transparência dos dados.
* **Atributos Formais**:
  - Fundo monocromático preto ou carvão profundo (`#121212`).
  - Cores monocromáticas em fósforo verde (`#00FF66`) ou âmbar quente (`#FFB000`).
  - Molduras, divisórias e tabelas construídas exclusivamente com caracteres Unicode ASCII (`┌─┐│└─┘`).
  - Cursor em bloco piscante no final da linha ativa.
* **Tipografia**: Fontes monospaçadas rigorosas (JetBrains Mono, Fira Code, IBM Plex Mono).

### 9. Brutalismo Web Clássico / Raw HTML
* **Origem**: A Web dos anos 90 e o brutalismo digital dos anos 2010.
* **Filosofia**: A verdade dos materiais da web: hipertexto e links em estado bruto, sem fingir ser papel ou revista.
* **Atributos Formais**:
  - Tags HTML padrão renderizadas sem classes CSS decorativas.
  - Hiperlinks azuis sublinhados nativos (`#0000EE`) e roxos visitados (`#551A8B`).
  - Tabelas nativas com bordas pretas de 1px sem espaçamento interno complexo.
* **Tipografia**: Times New Roman nativo em escala de cabeçalhos HTML pura (`<h1>` a `<h6>`).

### 10. Y2K Futurism (1998–2003)
* **Origem**: Cultura da virada do milênio, rave e o otimismo da bolha pontocom.
* **Filosofia**: Euforia com a chegada do século XXI e com o ciberespaço sem fronteiras.
* **Atributos Formais**:
  - Metal líquido derretido, cromado 3D brilhante, orbes translúcidas.
  - Gradientes iridescentes, ciano elétrico, prata metálica e detalhes de circuitos eletrônicos.
* **Tipografia**: Fontes arredondadas em bolha (*bubble fonts*), tipografia cibernética esticada.

### 11. Frutiger Aero / Web 2.0 Gloss (2004–2013)
* **Origem**: Windows Vista/7 Aero, Mac OS X Aqua e consoles Nintendo Wii/DS.
* **Filosofia**: Utopismo tecnológico limpo: a fusão harmoniosa entre tecnologia de ponta, natureza e ecologia.
* **Atributos Formais**:
  - Superfícies de vidro polido com brilho horizontal branco (*glossy reflection*).
  - Céus azuis com nuvens brancas fofas, água translúcida cristalina, folhas verdes com orvalho e peixes tropicais.
  - Orbes tridimensionais com efeito de bolha, bokeh fotográfico e clarões de lente (*lens flare*).
* **Tipografia**: Fontes humanistas limpas e polidas (Segoe UI, Frutiger, Myriad Pro).

### 12. Skeuomorphism Clássico (2007–2012)
* **Origem**: Apple iOS 1 a 6 e OS X Mavericks.
* **Filosofia**: Facilitação da curva de aprendizado touchscreen através de metáforas táteis de objetos cotidianos.
* **Atributos Formais**:
  - Imitação fiel de texturas reais: couro costurado, madeira de nogueira, papel linho e feltro verde de mesa de bilhar.
  - Botões plásticos volumosos com gradientes de três pontos, chanfros e sombras projetadas multicamadas.
* **Tipografia**: Helvetica Neue com sombras internas e chanfros de relevo.

---

## 📐 Família 3: Minimalismo Moderno & Design Systems (2012 – 2023)

### 13. Flat Design 1.0 (2012–2015)
* **Origem**: Windows Phone Metro UI, iOS 7 e Windows 8.
* **Filosofia**: Rejeição radical da simulação de materiais físicos em telas eletrônicas.
* **Atributos Formais**:
  - Eliminação total de sombras, reflexos, gradientes e relevos.
  - Blocos de cores sólidas e saturadas em arranjo puramente bidimensional.
* **Tipografia**: Fontes sem serifa puras em caixas de diálogo simples.

### 14. Flat 2.0 & Material Design / Material You (2015–Presente)
* **Origem**: Google Material Design (M1, M2 e Material You / M3).
* **Filosofia**: Metáfora física do "papel digital quântico" com elevações lógicas e física de transição.
* **Atributos Formais**:
  - Elevações lógicas em z-index (1dp a 24dp) gerando sombras suaves e realistas.
  - Curvas de aceleração e desaceleração física em todas as animações.
  - Paletas tonais dinâmicas extraídas do ambiente do usuário (M3).
* **Tipografia**: Roboto e Google Sans.

### 15. Neumorphism / Soft UI (2019–2020)
* **Origem**: Tendência conceitual no Dribbble.
* **Filosofia**: A interface esculpida como relevo na mesma matéria contínua do plano de fundo.
* **Atributos Formais**:
  - O elemento possui exatamente a mesma cor do canvas de fundo.
  - O volume é moldado por duas sombras opostas: sombra escura no canto inferior direito e luz branca no canto superior esquerdo.
  ```css
  background: #e0e5ec;
  box-shadow: 9px 9px 16px #a3b1c6, -9px -9px 16px #ffffff;
  border-radius: 16px;
  ```

### 16. Glassmorphism (2020–2023)
* **Origem**: macOS Big Sur e Windows 11 Fluent Design.
* **Filosofia**: Profundidade espacial e hierarquia através de camadas de vidro fosco semitransparente.
* **Atributos Formais**:
  - `backdrop-filter: blur(16px)` com fundo semi-transparente `rgba(255, 255, 255, 0.1)`.
  - Borda de 1px com gradiente translúcido simulando o brilho da quina de um vidro lapidado.
  - Elementos de cores vivas no plano de fundo para destacar o desfoque.

### 17. Claymorphism (2021–2023)
* **Origem**: Web 3D amigável e design lúdico.
* **Filosofia**: Aconchego tátil e acolhimento através de formas fofas e amigáveis de argila modelada.
* **Atributos Formais**:
  - Cantos muito arredondados (`rounded-3xl` ou `rounded-full`).
  - Sombra interna suave no topo para dar sensação de inflamento e sombra externa difusa com cor colorida.
  - Cores pastel adocicadas.

---

## 🚀 Família 4: Vanguarda Contemporânea & Estilos Anti-IA (2024 – 2026+)

### 18. Bento Grid (Modularidade & Densidade)
* **Origem**: Apple promo pages, Linear, Raycast.
* **Filosofia**: Alta densidade de informação apresentada de forma limpa, escaneável e compartimentalizada.
* **Atributos Formais**:
  - Grade modular com células de proporções variadas (1x1, 2x1, 1x2, 2x2).
  - Cantos arredondados contidos (8px a 16px) e bordas sutis com baixa opacidade.
  - Cada célula conta uma micro-narrativa visual com gráficos dedicados.

### 19. Tactile Brutalism & Engineered Minimalism
* **Origem**: Linear, Stripe Press, Vercel.
* **Filosofia**: A arquitetura de software tratada como artesanato de alta precisão.
* **Atributos Formais**:
  - Fundo quase preto (*near-black* `#080A0A`).
  - *Hairline borders* de 1px semi-transparentes (`rgba(255, 255, 255, 0.06)`).
  - Elevações através de *surface ladders* (luminância sutil em vez de sombras pesadas).
  - Micro-tipografia técnica de 10px-11px mono uppercase com tracking alargado.
  - Filosofia *single-accent* (uma única cor de destaque vibrante usada com extrema moderação).

### 20. Neo-Brutalism / Nu-Brutalism
* **Origem**: Figma, Gumroad, Retool, Substack.
* **Filosofia**: Rejeição à frieza e esterilidade corporativa; afirmação de confiança crua e atitude.
* **Atributos Formais**:
  - Bordas pretas sólidas de 2px a 4px.
  - Sombras duras offset com zero blur (`box-shadow: 4px 4px 0px #000000`).
  - Cores ultra-saturadas em alto contraste.
  - Botões que afundam fisicamente no hover/active (`transform: translate(2px, 2px)` com redução da sombra).

### 21. Editorial / Archive Luxury
* **Origem**: Kinfolk, Readymag, revistas de moda independente, Stripe Press.
* **Filosofia**: A lentidão e o prestígio da publicação impressa transposta para a experiência digital.
* **Atributos Formais**:
  - Margens assimétricas generosas que deixam o conteúdo respirar.
  - Notas de rodapé numeradas, capitulares imponentes e números romanos.
  - Serifas monumentais display (*Instrument Serif*, *Fraunces*, *Editorial New*) combinadas com sans-serif neutra.
  - Fotografia autoral em grande escala com direção de arte personalizada.

### 22. Organic / Solarpunk / Biophilic Design
* **Origem**: Movimentos de design ecológico e regenerativo contemporâneos.
* **Filosofia**: O digital como reflexo dos padrões orgânicos da natureza e da calma biológica.
* **Atributos Formais**:
  - Formas fluidas em curva orgânica, ausência de cantos retos afiados.
  - Paletas de cores botânicas: verdes musgo, terracota, mostarda terrosa, off-white cru (`#F9F8F6`).
  - Texturas imperfeitas sutis: papel reciclado, linho e madeira clara.
  - Microinterações lentas e suaves que reduzem a ansiedade cognitiva.

### 23. Cyberpunk / Dark Sci-Fi HUD
* **Origem**: Interfaces ficcionais de ficção científica (FUI), jogos como Cyberpunk 2077.
* **Filosofia**: A estética de alta tecnologia futurista e vigilância de sistemas avançados.
* **Atributos Formais**:
  - Fundo preto absoluto (`#000000`).
  - Detalhes de HUD militar: cantos chanfrados a 45 graus, miras de calibração nos vértices dos cards.
  - Cores neon ácidas de altíssimo contraste: ciano elétrico (`#00F0FF`) e magenta (`#FF003C`).
  - Linhas de telemetria e elementos monospaçados com dados de sistema.

### 24. Acid Graphics / Deconstructivist Anti-Design
* **Origem**: Cultura rave dos anos 90 revisitada pela vanguarda pós-internet (David Carson, underground digital).
* **Filosofia**: Quebra proposital de qualquer grade e padrão de bom gosto convencional em nome da pura expressividade visual.
* **Atributos Formais**:
  - Tipografia deformada, liquefeita (*liquid chrome*) e esticada.
  - Colagens digitais caóticas em camadas sobrepostas sem contenção em caixas.
  - Mistura de fontes góticas medievais (Blackletter) com fontes mono e símbolos esotéricos.
