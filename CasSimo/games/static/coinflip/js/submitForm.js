$(document).ready(function() {
    let messageContent = $('.alert').text();
    
    if(messageContent.includes("Tails")) {
        $('#coin').addClass('tails-still');
    }
    else if (messageContent.includes("Heads")){
        $('#coin').removeClass();
    }
    else {
        $('#coin').removeClass();
    }
    
});

function submitForm(option) {
    $('#' + option).prop('checked', true);

    $('#coin').removeClass();
    $('#coin').addClass('spin');



    setTimeout(function () {
        $('#coinFlipForm').submit();
    }, 3000);
}

