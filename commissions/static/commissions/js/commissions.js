$('#new-image').change(function() {
    var file = $('#new-image')[0].files[0];
    $('#filename').text(`Image will be set to: ${file.name}`);
});

let sizeSelected = $('#id_size').val();
let petNumSelected = $('#id_pet_num').val();
let mediaSelected = $('#id_media').val();

let optionSelected = ""
$( "select option:first-child" ).attr("disabled","disabled");

if (optionSelected == "") {
    $('select').css('color', '#aab7c4');
}

$('select').change(function () {
    optionSelected2 = $(this).val();
    if (optionSelected2 == "") {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', 'black')
    }
});