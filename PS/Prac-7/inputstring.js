function search(){
    let text=document.forms["form"]["inputText"].value;
    Div=document.getElementById("output");
    if(isNaN(text))
    {
        isString(text);
    }
    else
    {
        if(Number.isInteger(parseFloat(text)))
        {
            isNumber(parseInt(text));
        }
        else{
            Div.innerHTML="Entered input is not an integer";
        }
    }
}
function isString(text){
    let str=text;
    for(let i=0;i<str.length;i++)
    {
        if(str[i]=="a" || str[i]=="A" || str[i]=="e" || str[i]=="E" || str[i]=="i" || str[i]=="I" || str[i]=="o" || str[i]=="O" || str[i]=="u" || str[i]=="U")
        {
            Div.innerHTML="First Vowel from leftmost side is \""+str[i]+"\" at position: "+(i+1);
            break;
        }
        else if(i==str.length-1)
        {
            Div.innerHTML="This Sting does not contains any vowels";
        }
    }
}
function isNumber(text){
    let reverse=0,n=text;
    let flag=0,a;
    if(n<0)
    {
        flag=1;
        n=n*(-1);
    }
    while(n>0)
    {
        a=n%10;
        reverse=(reverse*10)+a;
        n=Math.floor(n/10);
    }
    if(flag==1)
    {
        reverse=reverse*(-1);
    }
    Div.innerHTML="Reversed number is "+reverse;
}