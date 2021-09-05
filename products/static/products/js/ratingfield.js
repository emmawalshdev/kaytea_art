let ratingSelected = $('#id_review_rating').val();
$('#div_id_review_rating option[value=" "]').prop('disabled', true);
if (ratingSelected == " ") {
    $('#id_review_rating').css('color', '#aab7c4');
}
$('#id_review_rating').change(function () {
    ratingSelected = $(this).val();
    if (ratingSelected == " ") {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', 'black')
    }
});
