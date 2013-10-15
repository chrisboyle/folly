$(function(){
$("a.addfavicon").each(function() {
    $(this).before('<img class="favicon" src="https://getfavicon.appspot.com/http://' + this.hostname + '/" />');
});})
