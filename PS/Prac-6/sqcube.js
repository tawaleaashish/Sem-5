insertdata();
function insertdata(){
    for(let i=0;i<=10;i++)
    {
        let table=document.getElementById("insertData");
        let row=table.insertRow();
        let cell1=row.insertCell(0);
        let cell2=row.insertCell(1);
        let cell3=row.insertCell(2);
        cell1.innerHTML=i;
        cell2.innerHTML=i**2;
        cell3.innerHTML=i**3;
    }
}