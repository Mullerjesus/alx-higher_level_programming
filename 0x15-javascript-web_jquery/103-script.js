$(document).ready(function(){
    $('#btn_translate').click(function(){
        let languageCode = $('#language_code').val();
        $.get('https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode, function(data){
            $('#hello').text(data.hello);
        });
    });

    $('#language_code').keypress(function(e){
        if(e.which == 13){
            let languageCode = $('#language_code').val();
            $.get('https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode, function(data){
                $('#hello').text(data.hello);
            });
        }
    });
});
