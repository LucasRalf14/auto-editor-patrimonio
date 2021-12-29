# auto-editor-patrimonio

Esse pequeno programa foi feito para agilizar a edição de um documento word para a impressão de etiquetas que tem como objetivo identificarem equipamentos da empresa provedora de internet.

Toda a lógica se baseia em automaticamente clicar nas caixas de texto e digitar os valores com a biblioteca pyautogui sendo a principal ferramenta para isso.

A primeira versão foi feita usando um método ia em cada posição para poder editar, o que deu muito trabalho para pegar as posições onde o mouse deveria ir.

Então foi criado um pequeno arquivo, como um script, para facilitar a identificação das posicoes de onde o mouse deveria ir.

A versão final (v2), as posições são acessadas com a própria biblioteca apertando a tecla 'tab'; nesta versão também foi colocada outra biblioteca, a pysimplegui, que ficou responsável da interface grafica e interação com o usuário.
