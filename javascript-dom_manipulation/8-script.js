document
  .addEventListener("DOMContentLoaded", () => {
    fetch("https://hellosalut.stefanbohacek.dev/?lang=fr");
  })
  .then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  })
  .then((data) => {
    const hello = document.querySelector("#hello");
    hello.textContent = data.hello;
  })
  .catch((error) => {
    console.error("There was a probleme with the fetch operation:", error);
    const hello = document.querySelector("#hello");
    hello.textContent = "Error fetching data";
  });
