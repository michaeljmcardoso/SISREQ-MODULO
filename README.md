# SISREQ - Sistema de Regularização Quilombola

<p>
 O programa em questão é um sistema de gerenciamento de registros para a regularização quilombola. Ele utiliza as bibliotecas Sqlite3 para criar e manipular um banco de dados SQLite, Pandas para manipulação de dados e exportação para planilha, Matplotib e Seaborn para gerar visualizações gráficas, e PySimpleGUI para criar a janela. Basicamente, a interface gráfica permite ao usuário inserir novos registros, consultar registros existentes, pesquisar registros por nome de comunidade, alterar registros selecionados e extrair os registros para uma planilha Excel. No geral, o SISREQ é um sistema versátil que permite o gerenciamento eficiente de processos, facilitando o acesso às informações, a geração de relatórios e a tomada de decisões com base em dados atualizados e organizados. A lógica do programa é focada em fornecer uma solução completa para o controle e acompanhamento de processos de forma eficaz e simplificada.
</p>

## Step by step

<p>
  Para concepção do programa utilizamos as seguintes bibliotecas:

   - `sqlite3` para manipulação do banco de dados SQLite.
   - `PySimpleGUI` para criar a interface gráfica.
   - `pandas` para manipulação de dados e exportação para planilha.
   - `Seaborn` e `Matplotlib` para criar e plotar as visualizações gráficas.
</p>
  
<p>
  Primeiro passo é criar ou conectar-se a um banco de dados SQLite chamado "sisreq.db" e obter um cursor para executar comandos SQL.
  
  Em seguida criamos a tabela "sisreq", caso ela não exista no banco de dados. A tabela possui as seguintes colunas: 
  
  **ID,
    Numero TEXT,
    Data_Abertura DATE,
    Comunidade TEXT,
    Municipio TEXT,
    Area_ha NUMERIC,
    Num_familias NUMERIC,
    Fase_Processo TEXT,
    Etapa_RTID TEXT,
    Edital_DOU TEXT,
    Edital_DOE TEXT,
    Portaria_DOU DATE,
    Decreto_DOU DATE,
    Titulo TEXT,
    PNRA TEXT,
    Relatorio_Antropologico TEXT,
    Certidao_FCP TEXT,
    Data_Certificacao DATE,
    Sobreposicao TEXT,
    Analise_de_Sobreposicao TEXT,
    Acao_Civil_Publica TEXT,
    Data_Decisao DATE,
    Teor_Decisao_Prazo_Sentença TEXT,
    Outras_Informacoes TEXT.**
  
  O passso seguinte é a definação das opções para os campos **Sobreposição, Etapa_RTID, Fase_Processo, Certidao_FCP, Acao_Civil_Publica e Relatório Antropológico.**

  Definimos o tema da janela utilizando o PySimpleGUI e layout da janela principal. A janela possui campos de entrada para os dados do registro, botões para inserir, consultar e extrair planilha, uma tabela para exibir os registros e um botão para alterar um registro selecionado.

 Para alguns botões, foi aplicado uma cor diferente como um atributo pre-atentivo, dando algum destaque para a função.
  
  Criada a janela com o layout definido, damos continuidade construindo as funções para inserir dados, consultar registros, pesquisar por nome da comunidade, extrair planilha, alterar um registro dentre outras funções para consulta e exibição de gráficos. Dentro da segunda janela de consulta da definimos outra função para extrair um extrato de um único registro.
  No Loop principal para capturar eventos da janela, quando um evento ocorre (por exemplo, clique em um botão), a função correspondente é chamada.
  Finalmente, fechamos a conexão com o banco de dados e encerramos o programa.
</p>

## Descrição da lógica do programa

<p>
  O programa SISREQ (Sistema de Regularização Quilombola) é um sistema de gerenciamento de processos, projetado para auxiliar em demandas que requerem análise, acompanhamento e controle de informações. Vejamos a seguir, uma descrição da lógica do programa SISREQ:

1. **Cadastro de Processos:** O SISREQ permite cadastrar processos com informações relevantes, como número do processo, município, fase do processo, data de entrada, entre outros campos essenciais.

2. **Banco de Dados:** O programa possui um banco de dados onde todos os registros de processos são armazenados. Isso permite que as informações sejam consultadas, atualizadas e recuperadas de forma eficiente.

3. **Consultas e Filtros:** O sistema permite realizar consultas e filtrar os processos com base em diferentes critérios. Por exemplo, é possível buscar processos por número, município, fase, data, entre outros atributos.

4. **Relatórios e Gráficos:** O SISREQ possui funcionalidades para gerar relatórios e gráficos com base nos dados armazenados. Isso possibilita a análise e visualização de informações relevantes, como a quantidade de processos por município, a distribuição dos processos por fase, entre outros.

5. **Atualização e Alteração de Dados:** O programa permite atualizar as informações dos processos, como alterar a fase, atualizar datas ou fazer anotações adicionais. Isso garante que as informações estejam sempre atualizadas e precisas.

6. **Controle de Acesso:** Futuramente podem ser implementados recursos de controle de acesso para garantir que apenas usuários autorizados tenham permissão para visualizar, inserir ou alterar determinados dados.

7. **Interface Amigável:** O SISREQ possui uma interface gráfica amigável, permitindo que os usuários interajam com o sistema de forma intuitiva, facilitando o cadastro e consulta de informações.

8. **Backup e Segurança:** Outro aspecto pensado e ainda não efetivado, será a implementação de recursos de backup, para evitar perda de dados em caso de falhas ou problemas técnicos. Além disso, poderá haver medidas de segurança para proteger informações sensíveis.

9. **Recursos Avançados:** No futuro, dependendo da complexidade do sistema, poderão ser implementados recursos avançados, como notificações automáticas, integração com outros sistemas, entre outros.

Em resumo, o SISREQ é um sistema versátil que permite o gerenciamento eficiente de processos, facilitando o acesso às informações, a geração de relatórios e a tomada de decisões com base em dados atualizados e organizados. A lógica do programa é focada em fornecer uma solução completa para o controle e acompanhamento de processos de forma eficaz e simplificada.
</p>

# SISREQ-MODULO
Versão modulada do programa.

A verssão inicial do projeto SISREQ começou com um script pequeno porém, ao longo do desenvolvimento, houve necessidade de implementar mais fucnionalidades, tornando o código cada vez mais complexo, prejudicando a legibilidade e manutenção. Ao final do projeto o script ficou com mais de 3 mil limhas de código num único arquivo. Isso também impactou na hora de distribuir a aplicação. Pois a compilação de um arquivo muito longo em um executável, elevou o tempo de abertura do programa para cerca de 10 a 12 segundos.

Desse modo, prezando por melhores práticas de programação, resolvemos implementar alterações para modular o programa e torná-lo um código mais limpo.

A modularidade é um princípio fundamental de design de software que envolve dividir um programa em componentes menores e independentes chamados módulos. Cada módulo é responsável por uma tarefa específica e pode ser desenvolvido, testado e mantido separadamente.

Existem várias vantagens em ter um programa modular:

Reutilização de código: Os módulos podem ser reutilizados em vários programas, reduzindo a duplicação de código e economizando tempo e esforço de desenvolvimento.

Manutenção aprimorada: Os módulos são mais fáceis de manter e depurar, pois podem ser isolados e testados individualmente. Isso reduz o tempo de inatividade e os custos de manutenção.

Flexibilidade: Os programas modulares são mais flexíveis e adaptáveis a mudanças nos requisitos. Novos módulos podem ser adicionados ou removidos facilmente para atender a novas funcionalidades ou alterações de negócios.

Colaboração aprimorada: A modularidade facilita a colaboração entre vários desenvolvedores, pois eles podem trabalhar em módulos diferentes simultaneamente.

Teste aprimorado: Os módulos podem ser testados isoladamente, o que melhora a cobertura de teste e reduz o risco de defeitos.

Desenvolvimento mais rápido: Os programas modulares podem ser desenvolvidos mais rapidamente, pois os módulos podem ser desenvolvidos e testados paralelamente.

Melhor legibilidade: Os programas modulares são mais fáceis de ler e entender, pois o código é organizado em módulos lógicos.

Escalabilidade aprimorada: Os programas modulares são mais escaláveis, pois novos módulos podem ser adicionados para lidar com cargas de trabalho crescentes ou novos recursos.

Em resumo, os programas modulares são essenciais para o desenvolvimento de software de alta qualidade, pois oferecem maior reutilização de código, manutenção aprimorada, flexibilidade, colaboração aprimorada, teste aprimorado, desenvolvimento mais rápido, melhor legibilidade e escalabilidade aprimorada.
