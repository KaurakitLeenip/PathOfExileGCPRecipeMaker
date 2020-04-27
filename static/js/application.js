$(document).ready(function(){
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    var status = [];


    //get details
    socket.on('newstatus', function(msg){
        if(msg.line != ""){
            console.log('recieved msg ' + msg.line)
            $('#log').append("<p>" + msg.line + "</p>");
        }
    })

    $('form#input').submit(function(event){
        console.log('asdfasdf')
        socket.emit('form_submit', {
            POESESSID: $('#sess').val(),
            league: $("#league").val(),
            max: $("#max").val()
            })
        return false
    })


})


function update_status(){
    jQuery.get('set_progress/', function(data){
        $('#log').append("<p>" + data + "</p>")
        setTimeout(update_status, 1000)
    })
}

