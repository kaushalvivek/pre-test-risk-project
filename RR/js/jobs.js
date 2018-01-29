var high_risk_sal = [150, 165, 170, 178, 190];
var low_risk_sal = [110, 115, 125, 120, 130];
var high_risk_req = [8, 7, 8, 7, 8];
var low_risk_req = [3, 3, 4, 3, 3];
var performance_score = [8, 5, 7, 9, 8]

var responses = []
var state = 0;
var net_worth = 0;
var chosen = -1;

function selected1() {
    if (chosen > 0) {
        return
    }
    $('#job2').hide();
    $('#job1').css('left', '36%');
    responses.push(1);
    chosen = 1;
    if (high_risk_req[state - 1] > performance_score[state - 1]) {
        net_worth -= 200;
    } else {
        net_worth += high_risk_sal[state - 1];
    }
}

function selected2() {
    if (chosen > 0) {
        return
    }
    $('#job1').hide();
    $('#job2').css('left', '36%');
    responses.push(2);
    chosen = 2;
    if (low_risk_req[state - 1] > performance_score[state - 1]) {
        net_worth -= 200;
    } else {
        net_worth += low_risk_sal[state - 1];
    }
}

function generate() {
    if (chosen == -1) {
        return
    } else if (chosen == 0) {
        job_manager();
        return
    } else if (chosen == 1) {
        performance_cutoff = high_risk_req[state - 1];
    } else {
        performance_cutoff = low_risk_req[state - 1];
    }
    $("#job1").hide();
    $("#job2").hide();
    $('#worth').hide();
    $("#instruction").hide();
    $("#instruction").html('Your performance score for the year is:');
    $("#instruction").addClass('fadeIn');
    $("#instruction").show();
    $("#generator").hide();
    $('#score').html(performance_score[state - 1]);
    window.setTimeout(
        function() {
            $('#score').removeClass('fadeOut');
            $('#score').addClass('fadeIn');
            $('#score').show();
        }, 1000
    )
    if (performance_score[state - 1] < performance_cutoff) {
        $('#main_title').html('Sorry, you got fired.')
    } else {
        $('#main_title').html('Congratulations! You kept your job.')
    }
    $('#worth').html('Net Worth: $' + net_worth + ',000');
    window.setTimeout(
        function() {
            $('#main_title').removeClass('fadeOut');
            $('#main_title').addClass('fadeIn');
            $('#main_title').show();
            $('#worth').removeClass('fadeOut');
            $('#worth').addClass('fadeIn');
            $('#worth').show();
        }, 2000
    )
    window.setTimeout(
        function() {
            $('#generator').html('Proceed');
            chosen = 0;
            $('#generator').removeClass('fadeOut');
            $('#generator').addClass('fadeIn');
            $('#generator').css('left', '45%');
            $('#generator').show();
        }, 3000
    )

}

function reset() {
    $('#job1').show();
    $('#job2').show();
    $('#job1').css('left', '20%');
    $('#job2').css('left', '50%');
}

function intro() {
    $("#job1").hide();
    $("#job2").hide();
    $("#worth").hide();
    $("#score").hide();
    $("#instruction").hide();
    $("#generator").hide();
    window.setTimeout(
        function() {
            $('#main_title').addClass('fadeOut');
        }, 2000)
    window.setTimeout(
        function() {
            $("#job1").addClass('fadeIn');
            $("#job2").addClass('fadeIn');
            $("#worth").addClass('fadeIn');
            $("#instruction").addClass('fadeIn');
            $("#generator").addClass('fadeIn');
            $("#job1").show();
            $("#job2").show();
            $("#worth").show();
            $("#instruction").show();
            $("#generator").show();
            job_manager();
        }, 3000)
}


function job_manager() {
    chosen = -1;
    $('#main_title').hide();
    $('#score').hide();
    $('#instruction').html('Choose One of the following Jobs');
    $('#generator').html('See Your Performance Score');
    $('#generator').css('left', '40%');
    if (state == 5) {
        return
    }
    $('#job1').html('Salary: $' + high_risk_sal[state] + ',000<br/><br/>Required Performance: ' + high_risk_req[state])
    $('#job2').html('Salary: $' + low_risk_sal[state] + ',000<br/><br/>Required Performance: ' + low_risk_req[state])
    state += 1;
    reset();
}

intro();

/*
Funtions need to be written for:
- Selecting Job
- Storing selected job
- Generating Performance Cutoff
- Maintaining score
*/