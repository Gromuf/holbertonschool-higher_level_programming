const movies = document.querySelector("#list_movies");
fetch("https://swapi-api.hbtn.io/api/films/?format=json")
  .then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  })
  .then((data) => {
    data.results.forEach((film) => {
      const listItem = document.createElement("li");
      listItem.textContent = film.title;
      movies.appendChild(listItem);
    });
  })
  .catch((error) => {
    console.error("There was a probleme with the fetch operation:", error);
  });
