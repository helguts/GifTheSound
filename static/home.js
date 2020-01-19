function validURL(str) {
  var pattern = new RegExp('^(https?:\\/\\/)?'+ // protocol
    '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+ // domain name
    '((\\d{1,3}\\.){3}\\d{1,3}))'+ // OR ip (v4) address
    '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ // port and path
    '(\\?[;&a-z\\d%_.~+=-]*)?'+ // query string
    '(\\#[-a-z\\d_]*)?$','i'); // fragment locator
  return !!pattern.test(str);
}

function showGifsForText(searchText) {
    $('#gifdiv').empty();
     $.post('/load_gifs', { search_text: searchText },
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
     });
 };

$(function() {
  $('#btSentence').click(function(event) { showSentence(); });
  $('#btSearchGifForText').click(function(event) { showGifsForText($('#searchtext').val()); });
  return true;
 });