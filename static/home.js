function validURL(str) {
  var pattern = new RegExp('^(https?:\\/\\/)?'+ // protocol
    '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+ // domain name
    '((\\d{1,3}\\.){3}\\d{1,3}))'+ // OR ip (v4) address
    '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ // port and path
    '(\\?[;&a-z\\d%_.~+=-]*)?'+ // query string
    '(\\#[-a-z\\d_]*)?$','i'); // fragment locator
  return !!pattern.test(str);
}

function showGifsForText(options) {
    var start = new Date();
    $("#btSearchGifForText").attr("disabled", true);
    var onSuccessShowGifs = function(jsonGifs) {
            var obj = jsonGifs;

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
            $('#gifdiv').prepend('<p><span> request took ' + totalSeconds + 's for ' + $('.giffortext').length + 'gifs.</span></p>');
            $("#btSearchGifForText").attr("disabled", false);
     };
    $('#gifdiv').empty();

    // use ajax instead of .post() to set content type to json for "reuqest.json()" in flask
    $.ajax({
      url:'/load_gifs',
      type:"POST",
      data: JSON.stringify(options),
      contentType:"application/json; charset=utf-8",
      dataType:"json",
      success: onSuccessShowGifs
    });
 };

$(function() {
  $('#btSentence').click(function(event) { showSentence(); });
  $('#btSearchGifForText').click(function(event) {
    var searchText = $('#searchtext').val();
    var doFastSearch = $('#cbFastSearch').is(":checked");
    var wordTypes = {
        "nouns": $('#wordTypeNouns').is(":checked"),
        "adverbs": $('#wordTypeAdverbs').is(":checked"),
        "verbs": $('#wordTypeVerbs').is(":checked"),
        "adjectives": $('#wordTypeAdjectives').is(":checked")
    };
    var options = {
    "searchText": searchText,
    "doFastSearch": doFastSearch,
    "wordTypes": wordTypes
    };
    showGifsForText(options);
  });
  return true;
 });