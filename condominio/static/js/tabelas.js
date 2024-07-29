const input = document.getElementById("search");
  const filter = document.getElementById("myTable");
  const currentPage = document.getElementById("page-info");
  const prevButton = document.getElementById("prev");
  const nextButton = document.getElementById("next");
  let currentRow = 0;
  let rowsPerPage = 9;

  input.addEventListener("keyup", function (event) {
    let filterValue = event.target.value.toUpperCase();
    let trs = filter.getElementsByTagName("tr");
    for (let i = 1; i < trs.length; i++) {
      let tds = trs[i].getElementsByTagName("td");
      let isVisible = false;
      for (let j = 0; j < tds.length; j++) {
        if (tds[j].textContent.toUpperCase().indexOf(filterValue) > -1) {
          isVisible = true;
          break;
        }
      }
      if (isVisible) {
        trs[i].style.display = "";
      } else {
        trs[i].style.display = "none";
      }
    }
  });

  function updatePageInfo() {
    currentPage.textContent = `. ${Math.ceil(currentRow / rowsPerPage) + 1} de ${Math.ceil(filter.rows.length / rowsPerPage)}`;
  }

  prevButton.addEventListener("click", () => {
    if (currentRow > 0) {
      currentRow -= rowsPerPage;
      if (currentRow < rowsPerPage) {
        prevButton.disabled = true;
      }
      nextButton.disabled = false;
    }
    updateTable();
    updatePageInfo();
  });

  nextButton.addEventListener("click", () => {
    currentRow += rowsPerPage;
    if (currentRow + rowsPerPage >= filter.rows.length) {
      nextButton.disabled = true;
    }
    prevButton.disabled = false;
    updateTable();
    updatePageInfo();
  });

  function updateTable() {
    for (let i = 1; i < filter.rows.length; i++) {
      filter.rows[i].style.display = "none";
      if (i >= currentRow && i < currentRow + rowsPerPage) {
        filter.rows[i].style.display = "";
      }
    }
  }

  // Add click event listener to each list item (table row)
  const tableBody = document.getElementById("myTableBody");
  tableBody.addEventListener("click", (event) => {
    if (event.target.tagName === "TR") {
      const rowIndex = event.target.rowIndex - 1; // Subtract 1 to exclude table header
      currentRow = rowIndex - (rowIndex % rowsPerPage);
      updateTable();
      updatePageInfo();
    }
  });

  updateTable();
  updatePageInfo();