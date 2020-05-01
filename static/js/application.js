$(document).ready(function(){
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    var status = [];
    var timer;

    //get details
    socket.on('newstatus', function(msg){
        if(msg.line != ""){
            console.log('recieved msg ' + msg.line)
            $('#log').append("<p>" + msg.line + "</p>");
        }
    })

    $('form#input').submit(function(event){
    timer = setInterval(update_status, 1000)
        jQuery.post('/', $('form#input').serialize(), function(data) {
            clearTimeout(timer)
        })
        event.preventDefault()
    })


})


function update_status(){
    jQuery.get('set_progress/', function(data){
        $('#log').empty();
        $('#log').append("<p>" + data + "</p>")
    })
}


