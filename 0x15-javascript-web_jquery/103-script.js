$(function() {
    function fetchAndDisplayGreeting() {
        var languageCode = $('#language_code').val();
        var url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode;

        $.get(url, function(data) {
            $('#hello').text(data.hello);
        }).fail(function() {
            console.error("Failed to fetch greeting");
        });
    }

    $('#btn_translate').click(fetchAndDisplayGreeting);

    $('#language_code').keypress(function(event) {
        if (event.which === 13) {
            fetchAndDisplayGreeting();
        }
    });
});
