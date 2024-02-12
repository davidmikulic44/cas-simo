$(document).ready(() => {
    $('.alert-info-roulette').hide();
    let messageContent = $('.alert').text();
    $('.wheel').removeClass('wheel-spin');
    let match = messageContent.match(/number (\d+)/);

    if (match) {
        const number = match[1];
        
        const id = "#slice_"+number;
        console.log(id);
        const totalSlices = 37;
        const degreesPerSlice = 360 / totalSlices;
        const rotationDegree = (totalSlices - number) * degreesPerSlice;
        
        let rotation = "rotate(" + rotationDegree + "deg)";
        $('.wheel').css({'transform' : rotation})
        $(id).addClass('winning-slice');
    } else {
        $('.alert-info-roulette').show();
    }

    
    $('#roulette-choice-color').click(() => {
        $('.roulette-color').show();
        $('.roulette-number').hide();
        $('#id_condition').val('color');
    });

    $('#roulette-choice-number').click(() => {
        $('.roulette-color').hide();
        $('.roulette-number').show();
        $('#id_condition').val('number');
    });

    $('#roulette-choice-all').click(() => {
        $('.roulette-number').show();
        $('.roulette-color').show();
        $('#id_condition').val('all');
    });

    $('.wheel-container').click(() => {
        $('.wheel').addClass('wheel-spin');
        $('.slice').removeClass('winning-slice');
        setTimeout(() => {
            $('#rouletteForm').submit();
        },3000);
    });
});
