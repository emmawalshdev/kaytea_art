$('#new-image').change(function() {
    var file = $('#new-image')[0].files[0];
    $('#filename').text(`Image will be set to: ${file.name}`);
});

let optionSelected = ""
$( "select option:first-child" ).attr("disabled","disabled");

if (optionSelected == "") {
    $('select').css('color', '#aab7c4');
}

$('select').change(function () {
    optionSelectedDropdown = $(this).val();
    if (optionSelectedDropdown == "") {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', 'black')
    }
});