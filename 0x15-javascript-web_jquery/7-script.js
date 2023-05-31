$.get("https://swapi-api.alx-tools.com/api/people/5/?format=json",
      function (data, status) {
	  const charac = data;
	  $("DIV#character").text(charac.name);
      });
