# auto-editor-patrimonio

Esse pequeno programa foi feito para agilizar a edição de um documento word para a impressão de etiquetas que tem como objetivo identificarem equipamentos da empresa provedora de internet em que estagiei.

Toda a lógica se baseia em automaticamente clicar nas caixas de texto que estão com valores em branco no arquivo word e digitar os valores com a biblioteca pyautogui sendo a principal ferramenta para isso.

A primeira versão foi feita usando um método se movia em cada posição para poder editar, o que deu muito trabalho para pegar as posições onde o mouse deveria ir.

Então foi criado um pequeno arquivo python, como um script, para facilitar a identificação das posicoes de onde o mouse deveria ir.

Na versão final (v2), as posições são acessadas com a própria biblioteca apertando a tecla 'tab'; nesta versão também foi colocada outra biblioteca, a pysimplegui, que ficou responsável da interface grafica e interação com o usuário. Na mesma, também foi feito um método para recuperar o ultimo valor digitado na última execução do programa; um simples arquivo txt, colocado na mesma pasta, é lido dentro do programa e os dados desse arquivo são sobrescritos e salvos para a recuperação do valor na próxima execução.
