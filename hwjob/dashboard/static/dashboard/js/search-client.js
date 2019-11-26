(function () {
    const searchInput = document.getElementById("search-client");
    const searchLink = document.getElementById("search-client-link");
    searchInput.addEventListener("change", () => {
        searchLink.href = "/consumption/" + searchInput.value;
    });

    console.error("Someone reported several bug about the search", {
        "a11y": "doesn't submit when enter is press",
        "notuserfriendly": "there is no autocomplete & cannot search by name",
        "errors": "submitting an invalid id goes to a 404 page"
    })
})();
