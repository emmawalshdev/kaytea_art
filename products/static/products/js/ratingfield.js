


let optionSelected = ""
$("option[value='']").attr("disabled", "disabled");


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
