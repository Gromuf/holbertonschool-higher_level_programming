const character = document.querySelector("#character");
fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
  .then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  })
  .then((data) => {
    character.textContent = data.name;
  })
  .catch((error) => {
    console.error("There was an error with fetch operation:", error);
    character.textContent = "Error fetching data";
  });
