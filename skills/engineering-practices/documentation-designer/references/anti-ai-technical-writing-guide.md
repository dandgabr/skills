# ✍️ Guia Canônico de Prosa Técnica Humana & Anti-AI Writing (Craft Docs)

Este guia prático fornece regras editoriais, tabelas comparativas de transformação ("Antes vs Depois") e um checklist de auditoria para eliminar o "AI Idiolect" e produzir documentação técnica humana, direta e de alta densidade.

---

## 1. Tabela Comparativa: Transformando AI Slop em Prosa Humana

| Antes (Vício de IA / AI Slop) | Depois (Prosa Humana / Craft Writing) | Por que a Mudança Funciona |
| :--- | :--- | :--- |
| *"No mundo dinâmico e em constante evolução do desenvolvimento de software, é crucial alavancar uma abordagem holística para mitigar riscos."* | *"Para evitar falhas em produção, teste cada integração antes do deploy."* | Elimina chavões vazios (*mundo dinâmico*, *alavancar*, *holístico*, *crucial*). Vai direto à ação e à consequência real. |
| *"Este framework não é apenas uma biblioteca utilitária; é um testemunho vivo do poder transformador da arquitetura orientada a microsserviços."* | *"O framework fornece mensageria assíncrona com confirmação de entrega via RabbitMQ."* | Elimina o *Contrastive Reframe* e a adjetivação hiperbólica (*testemunho vivo*, *poder transformador*). Descreve o fato técnico exato. |
| *"Mergulhe a fundo na tapeçaria intrincada de nossos endpoints RESTful para desbloquear sinergias sem precedentes."* | *"Consulte os endpoints em `/v1/orders` para criar e cancelar pedidos."* | Elimina metáforas grandiosas (*mergulhe a fundo*, *tapeçaria*, *sinergias*). Usa linguagem direta e acessível. |
| *"É importante ressaltar e ter em mente que o arquivo de configuração `.env` deve ser mantido em absoluto segredo para garantir a segurança."* | *"Nunca versione o arquivo `.env`. Adicione-o ao `.gitignore`."* | Corta preâmbulo frouxo (*é importante ressaltar que*). Usa comando no imperativo direto. |
| *"Em suma, pudemos concluir ao longo deste abrangente documento que a ferramenta desempenha um papel fundamental para os desenvolvedores."* | *(Removido completamente)* | Documentação técnica não precisa de conclusão de redação escolar. Quando a instrução técnica acaba, o texto termina. |

---

## 2. A Lei do Ritmo na Prática (Gary Provost)

### ❌ Exemplo de Ritmo Monótono de IA (Frases de mesmo tamanho):
> *"O gateway de pagamentos recebe a requisição criptografada do cliente web. O serviço de autenticação valida os cabeçalhos de segurança do token JWT. O motor de risco calcula a pontuação probabilística de fraude da transação. O banco de dados relacional registra o evento de autorização financeira. A resposta formatada em JSON retorna para a aplicação consumidora."*
*(Todas as frases têm cerca de 15 palavras. O leitor desliga o cérebro por tédio rítmico).*

### ✅ Exemplo de Ritmo Humano com Variação Dinâmica:
> *"A requisição chega. O gateway intercepta o payload, valida o JWT e delega o scoring ao antifraude em menos de 10ms. Se o risco for aceitável, o banco grava a transação e a API responde imediatamente com `201 Created`. Caso contrário, o pagamento é recusado antes de onerar os serviços centrais."*
*(Alternância cirúrgica entre frases curtas de 3 palavras, frases médias de fluxo e frases condicionais compostas. A leitura flui com música e energia).*

---

## 3. Checklist de Auditoria Anti-IA para Documentações

Antes de publicar qualquer documentação, execute este checklist de inspeção:

1. **[ ] O primeiro parágrafo começa imediatamente com valor técnico?**
   - Elimine qualquer introdução do tipo: *"Neste documento abordaremos..."* ou *"Com a crescente complexidade dos sistemas..."*.
2. **[ ] A lista negra de palavras de IA foi banida?**
   - Zero ocorrências de: *delve*, *leverage*, *streamline*, *tapestry*, *landscape*, *crucial*, *vital*, *holistic*, *paradigm*, *foster*, *unleash*, *synergy*, *alavancar*, *cenário atual*, *fundamental*.
3. **[ ] Há variação consciente no tamanho das frases?**
   - Verifique se não há mais de três frases seguidas com o mesmo número de palavras.
4. **[ ] O documento respeita a pureza do Diátaxis?**
   - Se for um **How-To**, há passos claros sem explicações teóricas gigantes?
   - Se for uma **Referência**, os parâmetros estão organizados de forma neutra sem narrativa prolixa?
5. **[ ] Os exemplos de código são 100% testáveis e sem placeholders mágicos?**
   - Todos os imports e variáveis necessários para rodar o snippet estão declarados?
6. **[ ] Os diagramas Mermaid usam aspas em rótulos com caracteres especiais e evitam a palavra `end` solta?**
