function voiceRec(){
    // var {PythonShell} = require('python-shell')
    // var path = require('path')

    // var opcoes = {
    //     scriptPath: path.join(__dirname, '../_engine/')
    // }

    // var rec = new PythonShell('voice_rec.py', opcoes)

    // rec.on("message", function(message){
    //     alert(message)
    // })
    var child_process = require('child_process');
    child_process.exec("start cmd.exe /C python3 script/qwert_hertz.py");
    
}
// child_process.exec("start cmd.exe /K cd /D C:/test");