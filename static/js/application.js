$(document).ready(function(){
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    var status = [];

    //get details
    socket.on('newstatus', function(msg){
        console.log('recieved msg ' + msg.line)
        $('#log').append("<p>" + msg.line + "</p>");
    })

    $('form#input').submit(function(event){
        socket.emit('form_submit', {
            POESESSID: $('#sess').val(),
            league: $("#league").val(),
            max: $("#max").val()
            })
        return false
    })

})