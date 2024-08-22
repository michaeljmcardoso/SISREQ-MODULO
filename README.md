# SISREQ - Sistema de Regularização Quilombola

## Descrição

<p>
  Um sistema de banco de dados é um software que gerencia e organiza dados, permitindo que os usuários armazenem, acessem, atualizem e consultem essas informações de forma eficiente e segura. Ele é composto por um banco de dados (onde os dados são armazenados) e um sistema de gerenciamento de banco de dados (SGBD), que controla o acesso e garante a integridade dos dados.

  Assim, o programa [SISREQ](https://github.com/michaeljmcardoso/SISREQ-MODULO/blob/desenvolvimento/README.md) (Sistema de Regularização Quilombola) é um sistema de gerenciamento de processos, projetado para auxiliar em demandas que requerem análise, acompanhamento e controle de informações. Vejamos a seguir, uma descrição de suas funcionalidades:

  1. **Cadastro de Processos:** O SISREQ permite cadastrar processos com informações relevantes, como número do processo, município, fase do processo, data de entrada, entre outros campos essenciais.

  2. **Banco de Dados:** O programa possui um banco de dados onde todos os registros de processos são armazenados. Isso permite que as informações sejam consultadas, atualizadas e recuperadas de forma eficiente.

  3. **Consultas e Filtros:** O sistema permite realizar consultas e filtrar os processos com base em diferentes critérios. Por exemplo, é possível buscar processos por número, município, fase, data, entre outros atributos.

  4. **Relatórios e Gráficos:** O SISREQ possui funcionalidades para gerar relatórios e gráficos com base nos dados armazenados. Isso possibilita a análise e visualização de informações relevantes, como a quantidade de processos por município, a distribuição dos processos por fase, entre outros.

  5. **Atualização e Alteração de Dados:** O programa permite atualizar as informações dos processos, como alterar a fase, atualizar datas ou fazer anotações adicionais. Isso garante que as informações estejam sempre atualizadas e precisas.

  6. **Controle de Acesso:** Futuramente podem ser implementados recursos de controle de acesso para garantir que apenas usuários autorizados tenham permissão para visualizar, inserir ou alterar determinados dados.

  7. **Interface Amigável:** O SISREQ possui uma interface gráfica amigável, permitindo que os usuários interajam com o sistema de forma intuitiva, facilitando o cadastro e consulta de informações.

  8. **Backup e Segurança:** Outro aspecto pensado e ainda não efetivado, será a implementação de recursos de backup, para evitar perda de dados em caso de falhas ou problemas técnicos. Além disso, poderá haver medidas de segurança para proteger informações sensíveis, se houver.

  9. **Recursos Avançados:** No futuro, dependendo da complexidade do sistema, poderão ser implementados recursos avançados, como notificações automáticas, integração com outros sistemas, inteligência artificial, entre outros.

  Em resumo, o SISREQ é um sistema versátil que permite o gerenciamento eficiente de processos, facilitando o acesso às informações, a geração de relatórios, possibilitando tomada de decisões com base em dados atualizados e organizados. A lógica do programa é focada em fornecer uma solução completa para o controle e acompanhamento de processos de forma eficaz e simplificada.
  [Projeto](https://github.com/michaeljmcardoso/SISREQ-MODULO/blob/desenvolvimento/Projeto.md)
  </p>

## Step by step do desenvolvimento do programa

<p>
  Para concepção do programa utilizamos as seguintes bibliotecas:

   - `sqlite3` para manipulação do banco de dados SQLite.
   - `PySimpleGUI` para criar a interface gráfica.
   - `pandas` para manipulação de dados e exportação para planilha.
   - `Seaborn` e `Matplotlib` para criar e plotar as visualizações gráficas.
</p>
  
<p>
  Primeiro passo é criar ou conectar-se a um banco de dados SQLite e obter um cursor para executar comandos SQL.
  
  Em seguida criamos a tabela SISREQ, caso ela não exista no banco de dados. A tabela possui várias colunas, que são as nossas váriaveis.
  
  O passso seguinte é a definação das variáveis constantes para os campos do formulário que terão opões de múltipla escolha ou escolha única.

  Definimos o tema e o layout da janela principal. A janela possui campos de entrada para o cadastro de processos, botões para inserir, consultar e extrair planilha, uma tabela para exibir os registros cadastrados e um botão para consultar e outro para alterar um registro selecionado.
 
  Criada a janela com o layout definido, damos continuidade construindo as funções para inserir dados, consultar registros, pesquisar por nome da comunidade, pesquisa por município, pesquisar por número do processo, extrair planilha, alterar um registro dentre outras funções para consulta e exibição de gráficos. Dentro da segunda janela de consulta definimos outra função para extrair um extrato de um ou mais registros.

  No Loop principal para capturar eventos da janela, quando um evento ocorre (por exemplo, clique em um botão), a função correspondente é chamada.
  Finalmente, fechamos a conexão com o banco de dados e encerramos o programa.

  [SISREQ](https://github.com/michaeljmcardoso/SISREQ-MODULO/tree/desenvolvimento)

</p>