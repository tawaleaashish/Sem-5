var form = document.querySelector("form");

        form.addEventListener("submit", function (e) {
            var search = form.querySelector("input[name=q]");
            var searchTerm = search.value;
            var googleSearchUrl = "https://www.google.com/search?q=" + encodeURIComponent(searchTerm);
            window.open(googleSearchUrl, "_blank");
            e.preventDefault();
        });
        let index = 0;
        displayImages();
        function displayImages() {
            let i;
            const images = document.getElementsByClassName("image");
            for (i = 0; i < images.length; i++) {
                images[i].style.display = "none";
            }
            index++;
            if (index > images.length) {
                index = 1;
            }
            images[index - 1].style.display = "block";
            setTimeout(displayImages, 5000);
        }