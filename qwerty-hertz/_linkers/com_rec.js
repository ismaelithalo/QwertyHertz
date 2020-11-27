function comRec(){

    var child_process = require('child_process');
    child_process.exec("start cmd.exe /C python3 script/command_rec.py");
    
}
// child_process.exec("start cmd.exe /K cd /D C:/test");