let sizeSelected = $('#id_size').val();
let petNumSelected = $('#id_pet_num').val();
let mediaSelected = $('#id_media').val();

$('#id_size option[value=" "]').prop('disabled', true);
if (sizeSelected == " ") {
    $('#id_size').css('color', '#aab7c4');
}
$('#id_size').change(function () {
    sizeSelected = $(this).val();
    if (sizeSelected == " ") {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', 'black')
    }
});


$('#id_pet_num option[value=" "]').prop('disabled', true);
if (petNumSelected == " ") {
    $('#id_pet_num').css('color', '#aab7c4');
}
$('#id_pet_num').change(function () {
    petNumSelected = $(this).val();
    if (petNumSelected == " ") {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', 'black')
    }
});


$('#id_media option[value=" "]').prop('disabled', true);
if (mediaSelected == " ") {
    $('#id_media').css('color', '#aab7c4');
}
$('#id_media').change(function () {
    mediaSelected = $(this).val();
    if (mediaSelected == " ") {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', 'black')
    }
});
