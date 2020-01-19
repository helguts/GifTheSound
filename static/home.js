function validURL(str) {
  var pattern = new RegExp('^(https?:\\/\\/)?'+ // protocol
    '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+ // domain name
    '((\\d{1,3}\\.){3}\\d{1,3}))'+ // OR ip (v4) address
    '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ // port and path
    '(\\?[;&a-z\\d%_.~+=-]*)?'+ // query string
    '(\\#[-a-z\\d_]*)?$','i'); // fragment locator
  return !!pattern.test(str);
}

function showGifsForText(searchText, doFastSearch) {
    var start = new Date();
    $('#gifdiv').empty();
    $.post('/load_gifs', { search_text: searchText, do_fast_search: doFastSearch},
        function(jsonGifs) {
            var obj = jQuery.parseJSON(jsonGifs);

            var markups = '';
            $.each(obj, function(word,gifURL) {
              if (validURL(gifURL.url)) {
                var divMarkup = '<div class="divforgif">'
                var imgMarkup = '<img class="giffortext" src=' + gifURL.url + ' />';
                var spanMarkup = '<span>' + gifURL.word + '</span>';
                var markup = divMarkup + spanMarkup + imgMarkup + '</div>';
                markups += markup ;
               }
            });
            $('#gifdiv').append(markups);

            // print timer!
            var end = new Date();
            var milliseconds = end - start;
            var totalSeconds = parseInt(milliseconds/ 1000);
            $('#gifdiv').prepend('<p><span> request took: ' + totalSeconds + 's</span></p>')
     });
 };

$(function() {
  $('#btSentence').click(function(event) { showSentence(); });
  $('#btSearchGifForText').click(function(event) {
    var searchText = $('#searchtext').val();
    var doFastSearch = $('#cbFastSearch').is(":checked");
    showGifsForText(searchText, doFastSearch);
  });
  return true;
 });