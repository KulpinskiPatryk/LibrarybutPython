const searchField = document.querySelector("#searchBook");
const tableOutput = document.querySelector(".table-output");
const appTable = document.querySelector(".app-table");
const paginationContainer = document.querySelector(".pagination");
tableOutput.style.display = "none";
const noResults = document.querySelector(".no-results");
const tbody = document.querySelector(".table-body");

searchField.addEventListener("keyup", (e) => {
  const searchValue = e.target.value;

if (searchValue.trim().length > 0) {
    console.log("searchValue", searchValue);
    paginationContainer.style.display = "none";
    appTable.style.display = "none";
    tbody.innerHTML = "";
    fetch("/searchBook", {
      body: JSON.stringify({ searchText: searchValue }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("data", data);

        tableOutput.style.display = "block";

        console.log("data.length", data.length);

        if (data.length == 0) {
          noResults.style.display = "block";
          tableOutput.style.display = "none";
        } else {
          noResults.style.display = "none";
          data.forEach((item) => {
            tbody.innerHTML += `
                <tr>
                <td>1</td>
                <td>${item.title}</td>
                <td>${item.pages}</td>
                <td>${item.author_id}</td>
                <td>${item.genre_id}</td>
                </tr>`;
          });
        }
      });
  } else {
    tableOutput.style.display = "none";
    appTable.style.display = "block";
    paginationContainer.style.display = "block";
  }
});