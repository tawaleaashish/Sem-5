var i = document.getElementById("text");
        var currentSize = 5;
        increaseText();
        function increaseText() {
            if (currentSize <= 50) {
                i.innerHTML="TEXT-GROWING";
                i.style.fontSize = currentSize + "pt";
                i.style.color="Red";
                currentSize += 1;
                setTimeout(increaseText, 100);
            } 
            else {
                decreaseText();
            }
        }
        function decreaseText() {
            if (currentSize >= 5) {
                i.innerHTML="TEXT-SHRINKING"
                i.style.fontSize = currentSize + "pt";
                i.style.color="Blue";
                currentSize -= 1;
                setTimeout(decreaseText, 100);
            }
            else{
                increaseText();
            }
        }