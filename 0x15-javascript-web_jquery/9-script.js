$.ajax({
    url:"https://fourtonfish.com/hellosalut/?lang=fr",
    jsonp: "callback",
    dataType : 'jsonp',
    data: {
	format: "json",
    },
    success: function (data) {
	$("DIV#hello").text(data.hello);
    }});
