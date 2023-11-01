let op1=0,op2=0,flagfloat=false,flagop="",flagnum=true,value="";
let data = document.getElementById("display");

function clearDisplay() 
{
    op1=0;
    op2=0;
    flagfloat=false;
    flagop="";
    flagnum=true;
    value="";
    data.innerHTML="";
}

function appendSym(symbol) {
    if (symbol=="." && !flagfloat) 
    {
        data.innerHTML+=symbol;
        flagfloat=true;
        value+=symbol;
    } 
    else if (symbol!=".") 
    {
        if (flagnum) 
        {
            op1=parseFloat(value+symbol);
        } 
        else
        {
            op2=parseFloat(value+symbol);
        }
        data.innerHTML+=symbol;
        value+=symbol;
    }
}

function operate(sign) 
{
    if (value!="") {
        if(op2!=0)
        {
            calculateResult();
        }
        value="";
        flagnum=!flagnum;
        flagop=sign;
        data.innerHTML+=sign;
        flagfloat=false;
    }
}

function calculateResult() 
{
    if (flagnum && value!="") 
    {
        op1=parseFloat(value);
    } 
    else if (!flagnum && value !="") 
    {
        op2=parseFloat(value);
    }
    let result=0;
    if (flagop=='+') {
        result=op1+op2;
    } else if (flagop=='-') {
        result=op1-op2;
    } else if (flagop=='x') {
        result=op1*op2;
    } else if (flagop=='/') {
        result=op1/op2;
    } else if (flagop=='%') {
        result=op1%op2;
    }
    data.innerHTML=result;
    op1=result;
    value=op1.toString();
    op2=0;
    flagfloat=false;
    flagnum=true;
    flagop="";
}