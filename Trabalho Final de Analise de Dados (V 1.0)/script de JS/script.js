const buttom = document.querySelector("#send")

buttom.addEventListener("click", function (event) {
    //event.preventDefault();
    const name = document.querySelector("#search")
    const value = name.value 
    console.log(value)
    let blob = new Blob([value], {
        type: "text/plain;charset=utf-8"
    });
    
    saveAs(blob, "pesquisa.txt")
    
})

