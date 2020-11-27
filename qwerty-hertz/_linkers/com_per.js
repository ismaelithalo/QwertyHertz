function comEdit(){

    var child_process = require('child_process');                           // Configura variável de conexão com terminal
    child_process.exec("start cmd.exe /C python3 script/command_edit.py");  // Comando de shell script que executa comando e fecha terminal
    
}
function comDel(){

    var child_process = require('child_process');                           // Configura variável de conexão com terminal
    child_process.exec("start cmd.exe /C python3 script/command_del.py");   // Comando de shell script que executa comando e fecha terminal
    
}
// child_process.exec("start cmd.exe /K cd /D C:/test");