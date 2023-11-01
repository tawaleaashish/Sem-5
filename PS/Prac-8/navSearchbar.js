function filter(){
    var inputText=document.getElementById("searchValue").value;
    inputText=inputText.toLowerCase();
    list=document.getElementsByClassName("animal")
    for(var i=0;i<list.length;i++)
    {
        if(list[i].innerHTML.toLowerCase().includes(inputText))
        {
            list[i].style.display="list-item";
        }
        else
        {
            list[i].style.display="none";
        }
    }
}