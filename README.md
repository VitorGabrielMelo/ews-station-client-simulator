# Sistema de Alerta Antecipado: Simulador de Estação Fluvial

Um aplicativo/script cliente escrito em Python para simular estações de monitoramento do nível da água em rios.

O cliente de água usa multiprocessamento para criar vários processos. Cada um deles gera um nível de água aleatório. Esse nível é armazenado junto com a hora da leitura e o ID do processo. Esses dados são exibidos na tela com Tkinter, uma biblioteca incluída no Python para criar interfaces gráficas. Os dados também são convertidos para JSON e enviados ao servidor principal pela API REST. Cada processo atualiza seu nível de água em intervalos variáveis e reenvia os dados para a tela e para o servidor principal.

**NOTA:** atualmente, é preciso ter o servidor EWS em execução para rodar este aplicativo. Configure o endereço do servidor e confirme que ele está chamando a API `/reading`.
