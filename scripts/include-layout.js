document.addEventListener("DOMContentLoaded", function () {
  const loadHTML = (selector, file) => {
    fetch(file)
      .then(response => response.text())
      .then(data => {
        document.querySelector(selector).innerHTML = data;
      });
  };

  loadHTML("#header-placeholder", "../../partials/header.html");
  loadHTML("#footer-placeholder", "../../partials/footer.html");
});
