function intro() {
    $("#button_1").hide();
    $("#button_2").hide();
    $("#instructions").hide();
    $("#instructions_p").hide();
    window.setTimeout(
        function() {
            $('#main_title').addClass('fadeOut')
        }, 2000)
    window.setTimeout(
        function() {
            $("#main_title").html('Welcome to this Research Survey.')
            $("#main_title").removeClass('fadeOut')
        }, 2800)
    window.setTimeout(
        function() {
            $('#button_1').show()
            $("#button_1").addClass('fadeIn')
        }, 3700)
}

function temp() {
    $('#button_1').hide()
    $("#button_2").hide();
    $("#instructions").hide();
    $("#instructions_p").hide();
    $('#main_title').addClass('fadeOut')

    window.setTimeout(
        function() {
            $("#main_title").html('Coming Soon')
            $("#main_title").removeClass('fadeOut')
        }, 1500)
}

function instruction() {
    $('#button_1').hide()
    $('#main_title').addClass('fadeOut')

    window.setTimeout(
        function() {
            $('#instructions').addClass('fadeIn')
            $("#instructions").show()
        }, 1000)
    window.setTimeout(
        function() {
            $('#instructions_p').addClass('fadeIn')
            $("#instructions_p").show()
        }, 2000)

    window.setTimeout(
        function() {
            $("#button_2").addClass('fadeIn')
            $('#button_2').show()
        }, 3000)
}

intro();