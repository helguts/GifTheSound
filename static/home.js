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



function showWord(wordType) {
     $.post('/load_words', { word_type: wordType },
        function(returnedWord) {
        $('#theword').text(wordType + ": " + returnedWord);
        showGif(returnedWord);
    });
}

function showGif(word) {
     $.post('/load_gif', { search_term: word },
        function(returnedGifUrl) {
            if (!returnedGifUrl) {
                return false;
             }

            if (validURL(returnedGifUrl)) {
                $('#thegif').attr("src", returnedGifUrl);
            }
            else {
                alert(returnedGifUrl + " is not a valid url!");
            }
    });
}

function showSentence() {
    $.post('/get_sentence',
        function(data) {
        $('#thesentence').text(data)
    });
}

$(function() {
  $('#btNouns').click(function(event) { showWord("noun"); });
  $('#btAdj').click(function(event) { showWord("adj"); });
  $('#btAdv').click(function(event) { showWord("adv"); });
  $('#btVerbs').click(function(event) { showWord("verb"); });

  $('#btSentence').click(function(event) { showSentence(); });
  $('#btSearchGifForText').click(function(event) { showGifsForText($('#searchtext').val()); });
  return true;
 });