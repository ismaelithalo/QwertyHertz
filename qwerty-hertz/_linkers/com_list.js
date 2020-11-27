function comList(){
    var {PythonShell} = require('python-shell')             // Conexão com python
    var path = require('path')                              // Configura variável de caminho

    var opcoes = {
        scriptPath: path.join(__dirname, '../_engine/')     // Preenche caminho com diretório dos códigos python
    }

    var t = document.getElementById('listaComandos');       // Seleciona a div que será preenchida com os comandos

    var rec = new PythonShell('command_list.py', opcoes)    // Pega o arquivo python do diretório selecionado

    rec.on("message", function(message){                    // Monitora a variável de conexão com python
        // alert(message)
        t.innerHTML += message+'<br>'                       // Caso haja output, coloque no seguinte formato
    })
}