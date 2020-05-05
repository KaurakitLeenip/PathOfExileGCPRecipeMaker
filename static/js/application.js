var timer;

$(document).ready(function(){
    var status = [];
    $('#load-bar').hide();


    $('form#input').submit(function(event){
        $('#load-bar').show();
        $('#submit').prop('disabled', true);

        $('#status-bar').html("Pulling Stash Data...")
        timer = setInterval(update_status, 500)
        jQuery.post('/', $('form#input').serialize(), function(data) {
        })
        event.preventDefault()
        })
})


function update_status(){
    jQuery.get('set_progress/', function(data){
        console.log(data)
        if (data != ""){
            if (data == "DONE"){
                $('#load-bar').hide();
                $('#submit').prop('disabled', false);
                clearInterval(timer);
                jQuery.get('results', function(data) {
                    $('#results').html(data)

                })
            }
            $('#status-bar').html(data + '...');
        }
    })
}


