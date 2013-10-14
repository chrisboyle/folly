$(function(){
$("a.addfavicon").each(function() {
    $(this).before('<img class="favicon" src="http://g.etfv.co/http://' + this.hostname + '/" />');
});})
