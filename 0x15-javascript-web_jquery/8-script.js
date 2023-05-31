$.get("https://swapi-api.alx-tools.com/api/films/?format=json",
      function (data, status) {

	  const eps = data.results;
	  eps.forEach(ep => $("UL#list_movies").append(`<li>${ep.title}</li>`));
      });
